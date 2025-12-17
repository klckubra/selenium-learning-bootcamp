from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://tr.wikipedia.org/")

wait = WebDriverWait(driver, 10)

search_box = driver.find_element(By.ID, "searchInput")
search_box.send_keys("Makaleler")
search_box.send_keys(Keys.ENTER)

wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "mw-search-result-heading")))

links = []
article_titles = driver.find_elements(By.CLASS_NAME, "mw-search-result-heading")

for article in article_titles:
    article_url = article.find_element(By.TAG_NAME, "a")
    link_element = article_url.get_attribute("href")
    links.append(link_element)



print(f"Toplam {len(links)} link toplandı. Şimdi ziyarete başlıyoruz.")

for link in links[:3]:
    print(f"Gidiliyor: {link}")
    driver.get(link)

    first_paragraph = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "p")))

    print(f"Özet: {first_paragraph.text}")
    print("**************************************")


driver.quit()