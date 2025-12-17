from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("http://books.toscrape.com/")

wait = WebDriverWait(driver, 10)

wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "product_pod")))

books_information = []

star_map = {
    'One': 1, 
    'Two': 2,
    'Three': 3,
    'Four':4,
    'Five':5
}


while(True):
    books= driver.find_elements(By.CLASS_NAME, "product_pod")

    for order, book in enumerate(books, start=len(books_information)+1):
        print(f"{order}. book information is being retrieved.")
        book_name = book.find_element(By.TAG_NAME, "h3").text
        book_price = float(book.find_element(By.CLASS_NAME, "price_color").text.strip("£"))
        book_availability = book.find_element(By.CSS_SELECTOR, ".instock.availability").text

        star= book.find_element(By.CLASS_NAME, "star-rating").get_attribute("class").split()
        if star[0] != "star-rating":
            book_star = star_map[star[0]]
        else:
            book_star = star_map[star[1]]

        book_info = {
            "Book Name": book_name,
            "Book Price": book_price,
            "Availability": book_availability,
            "Book Star":book_star
        }
        books_information.append(book_info)
    
    try:
        driver.find_element(By.CSS_SELECTOR, ".next a").click()
        wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "product_pod")))

    except  NoSuchElementException:
        break
print("Data was collected")

driver.quit()

df = pd.DataFrame(books_information)
df.to_excel("books_data.xlsx", index = False)
print("The excel file was successfully created")
