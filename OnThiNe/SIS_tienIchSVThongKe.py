import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from tabulate import tabulate

driver = webdriver.Chrome(service=Service("venv/chromedriver.exe"))

driver.get("https://www.google.com.vn/?hl=vi")
search = driver.find_element(By.NAME, "q")
search.send_keys("sis ou")
search.submit()

results = driver.find_elements(By.CSS_SELECTOR, ".g h3")

for r in results:
    print(r.text)

# Click vào link tiện ích sinh viên
driver.implicitly_wait(3)
driver.find_element(By.CSS_SELECTOR, "div#rso > div:nth-child(1) div.g a").click()

driver.implicitly_wait(3)
# Click vào nút đăng nhập trong web tiện ích sinh viên
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success.ng-star-inserted").click()

# Nó mở ra thêm 1 tab :) nên bắt cái tab đó xài
driver.switch_to.window(driver.window_handles[1])

# Lấy cái Select chọn loại tài khoản
select_user_type = Select(driver.find_element(By.ID, "form-usertype"))
select_user_type.select_by_index(0)

# Lấy ô nhập tài khoản với mật khẩu
taiKhoan = driver.find_element(By.ID, "form-username")
matKhau = driver.find_element(By.ID, "form-password")

with open("data/account.json", encoding="utf-8") as file:
    accountCuaTuanTran = json.load(file)
    taiKhoan.send_keys(accountCuaTuanTran["username"])
    matKhau.send_keys(accountCuaTuanTran["password"])

# CLick đăng nhập
driver.find_element(By.CSS_SELECTOR, ".btn.m-loginbox-submit-btn.btn-block.btn-flat").click()

# Lấy list chức năng ra show lên
listChucNangTienIch = driver.find_elements(By.CSS_SELECTOR,
                                           "div.card.shadow-lg > div.card-body.py-0.px-1 div.ng-star-inserted > ul")

# for l in listChucNangTienIch:
#     print(l.text)

# Tìm cái nút xem điểm click dô
# Thậm chí cái thẻ <a> nó còn không có href hay onlick gì để chuyển trang luôn sao mà click :)
xemDiem = driver.find_element(By.CSS_SELECTOR,
                              "div.card.shadow-lg > div.card-body.py-0.px-1 div.ng-star-inserted > ul:nth-child(8)")
xemDiem1 = driver.find_element(By.CSS_SELECTOR,
                               "div.card.shadow-lg > div.card-body.py-0.px-1 div.ng-star-inserted > ul:nth-child(8) a").get_attribute("title")

print("Tại sao tìm đc nút này mà không click được? = " + xemDiem.text)
print("Tại sao tìm đc nút này mà không click được? = " + xemDiem1)

# Méo click được nên get luôn nó luôn cho rồi :)
driver.get("https://tienichsv.ou.edu.vn/#/diem")
driver.implicitly_wait(15)

# Lăn chuột xuống chụp cái ảnh cho uy tín
driver.execute_script("window.scrollTo(0, 500)")
driver.save_screenshot("tienIch1.png")

# Lấy các thông tin trong trang xem điểm

hocKy = driver.find_elements(By.CSS_SELECTOR, "#excel-table > tbody > tr.table-primary.ng-star-inserted")
soThuTu = driver.find_elements(By.CSS_SELECTOR,
                               "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(1)")
maMonHoc = driver.find_elements(By.CSS_SELECTOR,
                                "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(2)")
maNhomTo = driver.find_elements(By.CSS_SELECTOR,
                                "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(3)")
tenMonHoc = driver.find_elements(By.CSS_SELECTOR,
                                 "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(4)")
soTinChi = driver.find_elements(By.CSS_SELECTOR,
                                "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(5)")
diemQuaTrinh = driver.find_elements(By.CSS_SELECTOR,
                                    "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(7)")
diemThi = driver.find_elements(By.CSS_SELECTOR,
                               "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(8)")
diemHe10 = driver.find_elements(By.CSS_SELECTOR,
                                "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(10)")
diemHe4 = driver.find_elements(By.CSS_SELECTOR,
                               "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(11)")
diemChu = driver.find_elements(By.CSS_SELECTOR,
                               "#excel-table > tbody >tr.text-center.ng-star-inserted > td:nth-child(12)")
ketQua = driver.find_elements(By.CSS_SELECTOR,
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
        # print(check)

# for kq in listKetQua:
#     print(kq)

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

# for tc in listSoTinChi:
#     print(tc)
#
# for d4 in listDiemHe4:
#     print(d4)

print("Số tín chỉ = " + str(len(listSoTinChi)))
print("Số điểm hệ 4 = " + str(len(listDiemHe4)))
print(len(listDiemHe4) == len(listSoTinChi))

# Tính điểm GPA

diem = 0
tongTinChi = 0

for i in range(len(listSoTinChi)):
    diem += float(listDiemHe4[i]) * float(listSoTinChi[i])
    tongTinChi += float(listSoTinChi[i])

GPA = float(diem / tongTinChi)

print("GPA của Tuấn là = " + str(GPA))

# Xài tabulate để xuất bảng cho đẹp :) Còn không ưng thì ngồi kẻ tay coi nó đẹp k :)

listThongKe = []

for i in range(len(soThuTu)):
    if soThuTu[i].text == "1":
        listThongKe.append((hocKy[0].text, "", "", "", "", "", "", "", "", "", ""))

    listThongKe.append((soThuTu[i].text, maMonHoc[i].text, maNhomTo[i].text, tenMonHoc[i].text, soTinChi[i].text,
                        diemQuaTrinh[i].text, diemThi[i].text, diemHe10[i].text, diemHe4[i].text, diemChu[i].text,
                        listKetQua[i]))

print(tabulate(listThongKe, headers=["STT", "Mã MH", "Mã nhóm / tổ", "Tên môn học", "Số tín chỉ",
                                     "Điểm quá trình", "Điểm thi", "Điểm TK hệ 10", "Điểm TK hệ 4", "Điểm chữ",
                                     "Kết quả"]))

driver.quit()
