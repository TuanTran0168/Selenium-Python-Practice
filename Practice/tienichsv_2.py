from tabulate import tabulate
from selenium import webdriver
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

driver.save_screenshot("tienich2.png")

bug = WebDriverWait(driver, 20).until(
    ec.presence_of_element_located((By.CSS_SELECTOR,
                                    "div.ng-star-inserted > ul:nth-child(8) > li > div.text-cus > a:nth-child(1)"))
)

# xemDiem = driver.find_element(By.CSS_SELECTOR, "div.ng-star-inserted > ul:nth-child(8) > li > div.text-cus")
# driver.implicitly_wait(3)
# print(xemDiem.text)
# xemDiem.click()

driver.get("https://tienichsv.ou.edu.vn/#/diem")

driver.implicitly_wait(5)

driver.save_screenshot("tienich3.png")
driver.implicitly_wait(5)

listBug = WebDriverWait(driver, 10).until(
    ec.presence_of_all_elements_located((By.CSS_SELECTOR, "div.text-center > p"))
)
driver.save_screenshot("tienich4.png")
test = driver.find_elements(By.CSS_SELECTOR, "div.text-center > p")
driver.implicitly_wait(10)
for t in listBug:
    print(t.text)

driver.implicitly_wait(10)
driver.save_screenshot("tienich5.png")

hocKy = driver.find_elements(By.CSS_SELECTOR, "table#excel-table > tbody > tr.table-primary.ng-star-inserted")
soTTMonHoc = driver.find_elements(By.CSS_SELECTOR,
                                  "table#excel-table > tbody > tr.text-center.ng-star-inserted > td:nth-child(1)")
tenMonHoc = driver.find_elements(By.CSS_SELECTOR,
                                 "table#excel-table > tbody > tr.text-center.ng-star-inserted > td.align-middle.text-left")
soTinChi = driver.find_elements(By.CSS_SELECTOR,
                                "table#excel-table > tbody > tr.text-center.ng-star-inserted > td.align-middle:nth-child(5)")
diemQuaTrinh = driver.find_elements(By.CSS_SELECTOR,
                                    "table#excel-table > tbody > tr.text-center.ng-star-inserted > td.align-middle:nth-child(7)")
diemThi = driver.find_elements(By.CSS_SELECTOR,
                               "table#excel-table > tbody > tr.text-center.ng-star-inserted > td.align-middle:nth-child(8)")
diemHe10 = driver.find_elements(By.CSS_SELECTOR,
                                "table#excel-table > tbody > tr.text-center.ng-star-inserted > td.align-middle:nth-child(10)")
diemHe4 = driver.find_elements(By.CSS_SELECTOR,
                               "table#excel-table > tbody > tr.text-center.ng-star-inserted > td.align-middle:nth-child(11)")
diemChu = driver.find_elements(By.CSS_SELECTOR,
                               "table#excel-table > tbody > tr.text-center.ng-star-inserted > td.align-middle:nth-child(12)")
hocKyVaMonHoc = driver.find_elements(By.CSS_SELECTOR,
                                     "table#excel-table > tbody > tr.ng-star-inserted:not(.m-0.ng-star-inserted)")

listDiemCacMonHoc = []

for i in range(len(soTTMonHoc)):
    if soTTMonHoc[i].text == "1":
        listDiemCacMonHoc.append((hocKy[0].text, "", "", "", "", "", "", ""))
    listDiemCacMonHoc.append((soTTMonHoc[i].text, tenMonHoc[i].text, soTinChi[i].text,
                              diemQuaTrinh[i].text, diemThi[i].text, diemHe10[i].text, diemHe4[i].text,
                              diemChu[i].text))

print(tabulate(listDiemCacMonHoc,
               headers=["STT", "Tên môn học", "Số tín chỉ", "Điểm quá trình", "Điểm thi", "Điểm hệ 10", "Điểm thang 4",
                        "Điểm chữ"]))

driver.quit()
