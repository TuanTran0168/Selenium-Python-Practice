import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(service=Service("venv/chromedriver.exe"))

driver.get("https://lms.ou.edu.vn/")

driver.implicitly_wait(2)
driver.find_element(By.CLASS_NAME, "main-btn").click()
driver.find_element(By.CLASS_NAME, "login100-form-btn").click()

select = Select(driver.find_element(By.ID, "form-usertype"))
select.select_by_index(0)

taiKhoan = driver.find_element(By.ID, "form-username")
matKhau = driver.find_element(By.ID, "form-password")

with open("data/account.json", encoding="utf-8") as file:
    user = json.load(file)
    taiKhoan.send_keys(user["username"])
    matKhau.send_keys(user["password"])
driver.implicitly_wait(3)
driver.find_element(By.CSS_SELECTOR, ".btn.m-loginbox-submit-btn.btn-block.btn-flat").click()

driver.implicitly_wait(10)

driver.find_element(By.CSS_SELECTOR, "div.card-deck.dashboard-card-deck > div:first-child > a").click()

driver.implicitly_wait(5)
tenChuong = driver.find_elements(By.CSS_SELECTOR, "div.stateready > ul.flexsections.flexsections-level-0 > li h3")
# tenChuong = driver.find_elements(By.CSS_SELECTOR, "div.stateready > ul.flexsections.flexsections-level-0 li:not(li:first-child) a").__getattribute__("aria-label")

for t in tenChuong:
    print(t.text)