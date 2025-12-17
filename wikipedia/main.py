from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://tr.wikipedia.org/")

wait = WebDriverWait(driver, 10)

search_box = driver.find_element(By.ID, "searchInput")
search_box.send_keys("Makaleler")
search_box.send_keys(Keys.ENTER)

wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "mw-search-result-heading")))

datasets = []
article_titles = driver.find_elements(By.CLASS_NAME, "mw-search-result-heading")

temp_list = []

for article in article_titles:
    article_url = article.find_element(By.TAG_NAME, "a")
    link_element = article_url.get_attribute("href")
    temp_list.append({"title": article.text, "link":link_element})



print(f"Toplam {len(temp_list)} link toplandı. Şimdi ziyarete başlıyoruz.")

for list in temp_list[:3]:
    print(f"Gidiliyor: {list['link']}")
    driver.get(list['link'])

    first_paragraph = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "p"))).text

    record = {
        "Title": list['title'], 
        "Link": list['link'], 
        "Summary": first_paragraph
    }
    datasets.append(record)

    print("Data received.")

driver.quit()

df = pd.DataFrame(datasets)
df.to_excel("wikipedia_results.xlsx", index=False)
print("The excel file was successfully created")