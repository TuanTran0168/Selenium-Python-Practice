import json
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from tabulate import tabulate


class UnitTestCuaTuan(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(UnitTestCuaTuan, self).__init__(*args, **kwargs)
        self.driver = webdriver.Chrome(service=Service("venv/chromedriver.exe"))
        self.driver.get("https://www.google.com.vn/?hl=vi")

    def test_case_cua_Tuan(self):
        search = self.driver.find_element(By.NAME, "q")
        search.send_keys("Tien ich sinh vien ou")
        search.submit()

        results = self.driver.find_elements(By.CSS_SELECTOR, ".g h3")

        # Click vào link tiện ích sinh viên
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.CSS_SELECTOR, "div#rso > div:nth-child(1) div.g a").click()

        # Click vào nút đăng nhập trong web tiện ích sinh viên
        self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success.ng-star-inserted").click()

        # Nó mở ra thêm 1 tab :) nên bắt cái tab đó xài
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Lấy cái Select chọn loại tài khoản
        select_user_type = Select(self.driver.find_element(By.ID, "form-usertype"))
        select_user_type.select_by_index(0)

        # Lấy ô nhập tài khoản với mật khẩu
        taiKhoan = self.driver.find_element(By.ID, "form-username")
        matKhau = self.driver.find_element(By.ID, "form-password")

        with open("data/account.json", encoding="utf-8") as file:
            accountCuaTuanTran = json.load(file)
            taiKhoan.send_keys(accountCuaTuanTran["username"])
            matKhau.send_keys(accountCuaTuanTran["password"])

        # CLick đăng nhập
        self.driver.find_element(By.CSS_SELECTOR, ".btn.m-loginbox-submit-btn.btn-block.btn-flat").click()

        # Lấy list chức năng ra show lên
        listChucNangTienIch = self.driver.find_elements(By.CSS_SELECTOR,
                                                   "div.card.shadow-lg > div.card-body.py-0.px-1 div.ng-star-inserted > ul")

        # Tìm cái nút xem điểm click dô
        # Thậm chí cái thẻ <a> nó còn không có href hay onlick gì để chuyển trang luôn sao mà click :)
        xemDiem = self.driver.find_element(By.CSS_SELECTOR,
                                      "div.card.shadow-lg > div.card-body.py-0.px-1 div.ng-star-inserted > ul:nth-child(8)")
        xemDiem1 = self.driver.find_element(By.CSS_SELECTOR,
                                       "div.card.shadow-lg > div.card-body.py-0.px-1 div.ng-star-inserted > ul:nth-child(8) a").get_attribute(
            "title")
        print("Tại sao tìm đc nút này mà không click được? = " + xemDiem.text)
        print("Tại sao tìm đc nút này mà không click được? = " + xemDiem1)

        # Không click được nên get luôn nó luôn cho rồi :)
        self.driver.get("https://tienichsv.ou.edu.vn/#/diem")
        self.driver.implicitly_wait(15)

        # Lăn chuột xuống chụp cái ảnh cho uy tín
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.driver.save_screenshot("tienIch1.png")

        # Lấy các thông tin trong trang xem điểm

        hocKy = self.driver.find_elements(By.CSS_SELECTOR, "#excel-table > tbody > tr.table-primary.ng-star-inserted")
        soThuTu = self.driver.find_elements(By.CSS_SELECTOR,
                                       "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(1)")
        maMonHoc = self.driver.find_elements(By.CSS_SELECTOR,
                                        "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(2)")
        maNhomTo = self.driver.find_elements(By.CSS_SELECTOR,
                                        "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(3)")
        tenMonHoc = self.driver.find_elements(By.CSS_SELECTOR,
                                         "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(4)")
        soTinChi = self.driver.find_elements(By.CSS_SELECTOR,
                                        "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(5)")
        diemQuaTrinh = self.driver.find_elements(By.CSS_SELECTOR,
                                            "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(7)")
        diemThi = self.driver.find_elements(By.CSS_SELECTOR,
                                       "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(8)")
        diemHe10 = self.driver.find_elements(By.CSS_SELECTOR,
                                        "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(10)")
        diemHe4 = self.driver.find_elements(By.CSS_SELECTOR,
                                       "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(11)")
        diemChu = self.driver.find_elements(By.CSS_SELECTOR,
                                       "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(12)")
        ketQua = self.driver.find_elements(By.CSS_SELECTOR,
                                      "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(13)")

        listKetQua = []
        for kq in ketQua:
            try:
                check = kq.find_element(By.CSS_SELECTOR,
                                        "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(13) > span").get_attribute(
                    "class")
            except:
                print("BUG NHA")
            else:
                if check.__contains__("fa-times"):
                    listKetQua.append("X")
                else:
                    listKetQua.append("V")


        # Đủ dữ liệu rồi thì tính GPA

        listSoTinChi = []
        listDiemHe4 = []

        # # Lọc số tín chỉ ra
        for i in range(len(soTinChi)):
            if soTinChi[i].text.__eq__("0") \
                    or ((soTinChi[i].text.__eq__("0") == False) and (diemHe4[i].text.__eq__(""))) \
                    or ((soTinChi[i].text.__eq__("0") == False) and (diemHe10[i].text.__eq__("M"))):

                pass
            else:
                listSoTinChi.append(soTinChi[i].text)

        # Lọc điểm hệ 4 ra
        for d4 in diemHe4:
            if d4.text.__eq__(""):
                pass
            else:
                listDiemHe4.append(d4.text)

        print("Số tín chỉ = " + str(len(listSoTinChi)))
        print("Số điểm hệ 4 = " + str(len(listDiemHe4)))
        print(len(listDiemHe4) == len(listSoTinChi))

        # Xài tabulate để xuất bảng cho đẹp :) Còn không ưng thì ngồi kẻ tay coi nó đẹp k :)

        listThongKe = []

        for i in range(len(soThuTu)):
            if soThuTu[i].text == "1":
                listThongKe.append((hocKy[0].text, "", "", "", "", "", "", "", "", "", ""))

            listThongKe.append(
                (soThuTu[i].text, maMonHoc[i].text, maNhomTo[i].text, tenMonHoc[i].text, soTinChi[i].text,
                 diemQuaTrinh[i].text, diemThi[i].text, diemHe10[i].text, diemHe4[i].text, diemChu[i].text,
                 listKetQua[i]))

        print(tabulate(listThongKe, headers=["STT", "Mã MH", "Mã nhóm / tổ", "Tên môn học", "Số tín chỉ",
                                             "Điểm quá trình", "Điểm thi", "Điểm TK hệ 10", "Điểm TK hệ 4", "Điểm chữ",
                                             "Kết quả"]))

        # Tính điểm GPA

        diem = 0
        tongTinChi = 0

        for i in range(len(listSoTinChi)):
            diem += float(listDiemHe4[i]) * float(listSoTinChi[i])
            tongTinChi += float(listSoTinChi[i])

        GPA = float(diem / tongTinChi)

        print("===================================================================================")
        print("\n\nGPA của Tuấn Trần là = " + str(GPA))
        print("\n\nGPA của Tuấn Trần là = " + str(round(GPA, 2)))

        # 3.184647302904564 :((((
        self.assertTrue(round(GPA, 2) == "3.19") # ==> FAILED

        self.driver.quit()
