from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com/search?q=software+company+in+bangalore")

divs = driver.find_elements(By.TAG_NAME, "div")

for d in divs[:10]:
    print(d.text)

driver.quit()
