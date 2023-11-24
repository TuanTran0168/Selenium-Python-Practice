from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(service=Service("venv/chromedriver.exe"))
driver.get("https://tienichsv.ou.edu.vn/#/home")
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.ng-star-inserted").click()

driver.switch_to.window(driver.window_handles[1])
driver.get('https://id.ou.edu.vn/auth/login')

comboBox = Select(driver.find_element(By.ID, "form-usertype"))
comboBox.select_by_index(0)

taiKhoan = driver.find_element(By.ID, "form-username")
matKhau = driver.find_element(By.ID, "form-password")

driver.save_screenshot("tienich0.png")
with open("data/account.json", encoding="utf-8") as file:
    user = json.load(file)
    taiKhoan.send_keys(user["username"])
    matKhau.send_keys(user["password"])

    driver.save_screenshot("tienich1.png")

driver.find_element(By.CSS_SELECTOR, ".btn.m-loginbox-submit-btn.btn-block.btn-flat").click()

driver.implicitly_wait(100)
driver.save_screenshot("tienich2.png")
try:
    driver.implicitly_wait(100)
    driver.save_screenshot("tienich3.png")
    driver.find_element(By.CSS_SELECTOR, "div.ng-star-inserted > ul:nth-child(8) > li > div.text-cus > a:nth-child(2)").click()
    driver.save_screenshot("tienich4.png")
except NoSuchElementException:
    print('Không tìm thấy phần tử HTML')

# bug = WebDriverWait(driver, 10).until(
#     ec.presence_of_all_elements_located((By.CSS_SELECTOR,
#                                    "div.ng-star-inserted > ul:nth-child"))
# )
driver.quit()
