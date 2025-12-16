from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://tr.wikipedia.org/")

search_box = driver.find_element(By.ID, "searchInput")
search_box.send_keys("Makaleler")
search_box.send_keys(Keys.ENTER)

time.sleep(5)

links = []

article_titles = driver.find_elements(By.CLASS_NAME, "mw-search-result-heading")

for article in article_titles:
    article_url = article.find_element(By.TAG_NAME, "a")
    link_element = article.get_attribute("href")
    links.append(link_element)

print(f"Toplam {len(links)} link toplandı. Şimdi ziyarete başlıyoruz.")

for link in links:
    print(f"Gidiliyor: {link}")
    driver.get(link)
    time.sleep(3)
    paragraph = driver.find_element(By.TAG_NAME, "p")
    print(f"Özet: {paragraph.text}")
    print("**************************************")

driver.quit()
