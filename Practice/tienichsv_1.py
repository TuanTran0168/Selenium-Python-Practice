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
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success.ng-star-inserted").click()

driver.switch_to.window(driver.window_handles[1])
# driver.get('https://id.ou.edu.vn/auth/login')

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

# driver.implicitly_wait(100)
driver.save_screenshot("tienich2.png")
# try:
#     driver.implicitly_wait(100)
#     driver.save_screenshot("tienich3.png")
#     driver.find_element(By.CSS_SELECTOR, "div.ng-star-inserted > ul:nth-child(8) > li > div.text-cus > a:nth-child(2)").click()
#     driver.save_screenshot("tienich4.png")
# except NoSuchElementException:
#     print('Không tìm thấy phần tử HTML')

bug = WebDriverWait(driver, 20).until(
    ec.presence_of_element_located((By.CSS_SELECTOR,
                                    "div.ng-star-inserted > ul:nth-child(8) > li > div.text-cus > a:nth-child(1)"))
)

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

# bug1 = WebDriverWait(driver, 15).until(
#     ec.presence_of_element_located((By.CSS_SELECTOR,
#                                    "div.ng-star-inserted > ul:nth-child(8) > li > div.text-cus > a:nth-child(1)"))
# )
#
# bug1.click()

# for b in bug1:
#     print(b.text)


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

# for h in hocKyVaMonHoc:
#     print(h.text)

for hk in hocKy:
    print(hk.text)

for t in tenMonHoc:
    print(t.text)

for t in diemThi:
    print(t.text)

for t in diemHe10:
    print(t.text)

for t in diemHe4:
    print(t.text)

for t in diemChu:
    print(t.text)

# for i in range(len(tenMonHoc)):
#     if soTTMonHoc[i].text == "1":
#         print("===============================================================================================")
#         print("STT", end="")
#         print("\t\t", end="")
#         print("Tên môn học", end="")
#         print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t", end="")
#         print("Số tín chỉ", end="")
#         print("\t\t", end="")
#         print("Điểm quá trình", end="")
#         print("\t\t", end="")
#         print("Điểm thi", end="")
#         print("\t\t", end="")
#         print("Điểm thang 10", end="")
#         print("\t\t", end="")
#         print("Điểm thang 4", end="")
#         print("\t\t", end="")
#         print("Điểm chữ", end="\n")
#
#     print(soTTMonHoc[i].text, end = "")
#     print("\t\t", end="")
#     print(tenMonHoc[i].text, end="")
#     print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t", end="")
#     print(soTinChi[i].text, end="")
#     print("\t\t", end="")
#     print(diemQuaTrinh[i].text, end="")
#     print("\t\t", end="")
#     print(diemThi[i].text, end="")
#     print("\t\t", end="")
#     print(diemHe10[i].text, end="")
#     print("\t\t", end="")
#     print(diemHe4[i].text, end="")
#     print("\t\t", end="")
#     print(diemChu[i].text, end="\n")

count = 0;
for i in range(len(tenMonHoc)):
    if soTTMonHoc[i].text == "1":
        print("=======================================================================================================================================================")
        print(hocKy[count].text)
        count = count + 1
        print("STT\t\t\t" + "Tên môn học\t\t\t\t\t\t\t\t\t\t\t\t\t\t" + "Số tín chỉ\t\t" +
              "Điểm quá trình\t\t" + "Điểm thi\t\t" + "Điểm hệ 10\t\t" + "Điểm thang 10\t\t" +
              "Điểm thang 4\t\t" + "Điểm chữ")
    print(soTTMonHoc[i].text + "\t\t\t" + tenMonHoc[i].text + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t" + soTinChi[i].text + "\t\t" +
          diemQuaTrinh[i].text + "\t\t\t\t\t" + diemThi[i].text + "\t\t\t\t\t" + diemHe10[i].text + "\t\t\t\t\t" +
          diemHe4[i].text + "\t\t\t\t\t" + diemChu[i].text)



# driver.implicitly_wait(5)
# driver.find_element(By.CSS_SELECTOR, "div.ng-star-inserted > ul:nth-child(8) > span").click()
# # driver.find_element(By.)
# for b in listBug:
#     print(b.text)
#     # b.click()
#
# # try:
# #     # driver.implicitly_wait(100)
# #     driver.save_screenshot("tienich3.png")
# #     driver.find_element(By.XPATH, "div.ng-star-inserted > ul:nth-child(8) > li > div.text-cus > a:nth-child(1)").click()
# #     # driver.find_element(By.CSS_SELECTOR, "div.ng-star-inserted > ul:nth-child(8) > li > div.text-cus > a:nth-child(2)").click()
# #     driver.save_screenshot("tienich4.png")
# # except NoSuchElementException:
# #     print('Không tìm thấy phần tử HTML')

driver.quit()
