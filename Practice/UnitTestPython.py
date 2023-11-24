import unittest

from tabulate import tabulate
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MyTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MyTest, self).__init__(*args, **kwargs)
        self.driver = webdriver.Chrome(service=Service("venv/chromedriver.exe"))
        self.driver.get("https://tienichsv.ou.edu.vn/#/home")

    def test_case_1(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.ng-star-inserted").click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get('https://id.ou.edu.vn/auth/login')

        comboBox = Select(self.driver.find_element(By.ID, "form-usertype"))
        comboBox.select_by_index(0)

        taiKhoan = self.driver.find_element(By.ID, "form-username")
        matKhau = self.driver.find_element(By.ID, "form-password")

        self.driver.save_screenshot("tienich0.png")
        with open("data/account.json", encoding="utf-8") as file:
            user = json.load(file)
            taiKhoan.send_keys(user["username"])
            matKhau.send_keys(user["password"])

            self.driver.save_screenshot("tienich1.png")

        self.driver.find_element(By.CSS_SELECTOR, ".btn.m-loginbox-submit-btn.btn-block.btn-flat").click()

        self.driver.save_screenshot("tienich2.png")

        bug = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.CSS_SELECTOR,
                                            "div.ng-star-inserted > ul:nth-child(8) > li > div.text-cus > a:nth-child(1)"))
        )

        self.driver.get("https://tienichsv.ou.edu.vn/#/diem")

        self.driver.implicitly_wait(5)

        self.driver.save_screenshot("tienich3.png")
        self.driver.implicitly_wait(5)

        listBug = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.CSS_SELECTOR, "div.text-center > p"))
        )
        self.driver.save_screenshot("tienich4.png")
        test = self.driver.find_elements(By.CSS_SELECTOR, "div.text-center > p")
        self.driver.implicitly_wait(10)
        for t in listBug:
            print(t.text)

        self.driver.implicitly_wait(10)
        self.driver.save_screenshot("tienich5.png")

        hocKy = self.driver.find_elements(By.CSS_SELECTOR,
                                          "table#excel-table > tbody > tr.table-primary.ng-star-inserted")
        soTTMonHoc = self.driver.find_elements(By.CSS_SELECTOR,
                                               "table#excel-table > tbody > tr.text-center.ng-star-inserted > td:nth-child(1)")
        tenMonHoc = self.driver.find_elements(By.CSS_SELECTOR,
                                              "table#excel-table > tbody > tr.text-center.ng-star-inserted > td.align-middle.text-left")
        soTinChi = self.driver.find_elements(By.CSS_SELECTOR,
                                             "table#excel-table > tbody > tr.text-center.ng-star-inserted > td.align-middle:nth-child(5)")
        diemQuaTrinh = self.driver.find_elements(By.CSS_SELECTOR,
                                                 "table#excel-table > tbody > tr.text-center.ng-star-inserted > td.align-middle:nth-child(7)")
        diemThi = self.driver.find_elements(By.CSS_SELECTOR,
                                            "table#excel-table > tbody > tr.text-center.ng-star-inserted > td.align-middle:nth-child(8)")
        diemHe10 = self.driver.find_elements(By.CSS_SELECTOR,
                                             "table#excel-table > tbody > tr.text-center.ng-star-inserted > td.align-middle:nth-child(10)")
        diemHe4 = self.driver.find_elements(By.CSS_SELECTOR,
                                            "table#excel-table > tbody > tr.text-center.ng-star-inserted > td.align-middle:nth-child(11)")
        diemChu = self.driver.find_elements(By.CSS_SELECTOR,
                                            "table#excel-table > tbody > tr.text-center.ng-star-inserted > td.align-middle:nth-child(12)")
        hocKyVaMonHoc = self.driver.find_elements(By.CSS_SELECTOR,
                                                  "table#excel-table > tbody > tr.ng-star-inserted:not(.m-0.ng-star-inserted)")

        # listUnitTest = []
        # for d in diemHe10:
        #     # self.assertTrue(int(d.text) > 5)
        #     if len(d.text) == 0 or d.text.__eq__("M"):
        #         print("1")
        #     else:
        #         listUnitTest.append(d.text)
        #
        # for u in listUnitTest:
        #     print("C" + u + "C")
        #     self.assertTrue(float(u) > 3)

        listTinChiUnitTest = []
        listDiemThang4UnitTest = []

        for tc in soTinChi:
            if len(tc.text) == 0 or tc.text.__eq__("M") :
                print("1")
            else:
                listTinChiUnitTest.append(tc.text)

        for d in diemHe4:
            if d.text.__eq__("M"):
                print("1")
            else:
                listDiemThang4UnitTest.append(d.text)

        tongDiem = 0
        tongTinChi = 0
        for i in range(len(listTinChiUnitTest)):
            if len(listDiemThang4UnitTest) > 0 and listDiemThang4UnitTest[i] != "" and listTinChiUnitTest[i] != "0":
                tongDiem += float(listDiemThang4UnitTest[i]) * float(listTinChiUnitTest[i])
                tongTinChi += float(listTinChiUnitTest[i])

        diem = tongDiem / tongTinChi
        # round(diem, 2)
        print("Điểm = " + str(round(diem + 0.002, 2)))
        print("Điểm = " + str((diem, 2)))

        self.assertTrue(tongDiem / tongTinChi == 3.19)

        for u in listDiemThang4UnitTest:
            print(u)

        for u in listTinChiUnitTest:
            print(u)

        print("tin chi = " + str(len(listTinChiUnitTest)))
        print("so diem thang 4 = " + str(len(listDiemThang4UnitTest)))

        # listDiemCacMonHoc = []
        #
        # for i in range(len(soTTMonHoc)):
        #     if soTTMonHoc[i].text == "1":
        #         listDiemCacMonHoc.append((hocKy[0].text, "", "", "", "", "", "", ""))
        #     listDiemCacMonHoc.append((soTTMonHoc[i].text, tenMonHoc[i].text, soTinChi[i].text,
        #                               diemQuaTrinh[i].text, diemThi[i].text, diemHe10[i].text, diemHe4[i].text,
        #                               diemChu[i].text))
        #
        # print(tabulate(listDiemCacMonHoc,
        #                headers=["STT", "Tên môn học", "Số tín chỉ", "Điểm quá trình", "Điểm thi", "Điểm hệ 10",
        #                         "Điểm thang 4",
        #                         "Điểm chữ"]))

        self.driver.quit()
