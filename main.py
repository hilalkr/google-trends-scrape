from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook
import time

driver = webdriver.Chrome()
country_code = "TR" #you can change it according to your country
driver.get(f'https://trends.google.com/trends/trendingsearches/daily?geo={country_code}')
time.sleep(5)
date_title = driver.find_element(By.CLASS_NAME,"content-header-title")

print(date_title.text)

feed_items = driver.find_elements(By.CLASS_NAME, "feed-item")



wb = Workbook()
ws = wb.active
ws.title = "Scraped Data"
ws.append(["Title", "Index", "Search Count", "Search Detail"])


for item in feed_items:
    item_title= item.find_element(By.CLASS_NAME,"title")
    item_index = item.find_element(By.CLASS_NAME,"index")
    item_search_detail = item.find_element(By.CLASS_NAME,"details-bottom")
    item_search_count = item.find_element(By.CLASS_NAME,"search-count")
    print(item_title.text, item_index.text, item_search_count.text, item_search_detail.text)
    ws.append([item_title.text, item_index.text, item_search_count.text, item_search_detail.text])

wb.save(f"{date_title.text}.xlsx")