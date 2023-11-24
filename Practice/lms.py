from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import json

driver = webdriver.Chrome(service=Service("venv/chromedriver.exe"))
driver.get("https://lms.ou.edu.vn/")
driver.implicitly_wait(5)
driver.find_element(By.CLASS_NAME, "main-btn").click();

driver.find_element(By.CLASS_NAME, "login100-form-btn").click()

comboBox = Select(driver.find_element(By.ID, "form-usertype"))
comboBox.select_by_index(0)

taiKhoan = driver.find_element(By.ID, "form-username")
matKhau = driver.find_element(By.ID, "form-password")

with open("data/account.json", encoding="utf-8") as file:
    user = json.load(file)
    taiKhoan.send_keys(user["username"])
    matKhau.send_keys(user["password"])
driver.find_element(By.CSS_SELECTOR, ".btn.m-loginbox-submit-btn.btn-block.btn-flat").click()
# driver.find_element(By.CLASS_NAME, "m-loginbox-submit-btn").click()
driver.implicitly_wait(5)


driver.quit()
