from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

kw = input("Nhập ngày dò vé số: (Ngày - tháng - năm) = ")
veSo = input("Nhập 6 số trong tờ vé số của bạn = ")

kw = "10-04-2023"
veSo = "331863"
driver = webdriver.Chrome(service=Service("venv/chromedriver.exe"))

driver.get("https://www.xskthcm.com/")
driver.set_window_size(900, 1000)

listSoTien = []

for i in range(9):
    try:
        soTien = driver.find_element(By.CSS_SELECTOR,
                                     "div.slider-item > table.table.table-bordered > tbody > tr:nth-child(" + str(
                                         i + 1) + ") > td:nth-child(1) > div").text
        if i == 0:
            soTien = soTien[9:len(soTien)]
        if i == 1:
            soTien = soTien[9:len(soTien)]
        if i == 2:
            soTien = soTien[9:len(soTien)]
        if i == 3:
            soTien = soTien[9:len(soTien)]
        if i == 4:
            soTien = soTien[8:len(soTien)]
        if i == 5:
            soTien = soTien[8:len(soTien)]
        if i == 6:
            soTien = soTien[9:len(soTien)]
        if i == 7:
            soTien = soTien[10:len(soTien)]
        if i == 8:
            soTien = soTien[14:len(soTien)]

    except:
        print("BUG")
    else:
        listSoTien.append(soTien)

for t in listSoTien:
    print(t)

driver.save_screenshot("chonKQ.png")
clickChonNgay = driver.find_element(By.ID, "s2id_dkw-nav-kqxs-search")
clickChonNgay.click()
driver.save_screenshot("nhapNgay.png")
driver.implicitly_wait(5)
searchNgay = driver.find_element(By.CSS_SELECTOR, "#select2-drop > div.select2-search > input.select2-input")
searchNgay.send_keys(kw)
driver.save_screenshot("nhapNgay1.png")
searchNgay.send_keys(Keys.ENTER)

listTenGiai = []

listSoTrung = []

for i in range(9):
    try:
        tenGiai = driver.find_element(By.CSS_SELECTOR,
                                      "div.slider-item > table.table.table-bordered > tbody > tr:nth-child(" + str(
                                          i + 1) + ") > td:nth-child(1)")

        soTrung = driver.find_element(By.CSS_SELECTOR,
                                      "div.slider-item > table.table.table-bordered > tbody > tr:nth-child(" + str(
                                          i + 1) + ") > td:nth-child(2)")

        # soTien = driver.find_element(By.CSS_SELECTOR,
        #                              "div.slider-item > table.table.table-bordered > tbody > tr:nth-child(" + str(
        #                                  i + 1) + ") > td:nth-child(1) > br")
    except:
        print("BUG")
    else:
        listTenGiai.append(tenGiai.text)
        listSoTrung.append(soTrung.text)

for i in range(len(listSoTrung)):
    print(listTenGiai[i] + " " + listSoTrung[i])

print(veSo[1:6])

countTrung = 0
for i in range(len(listSoTrung)):
    if i == 0 and veSo[4:6].__eq__(listSoTrung[i]):
        print("Các số trúng là = " + listSoTrung[i])
        print("Bạn đã trúng " + listTenGiai[i] + ", số tiền của bạn là = " + listSoTien[i])

    elif i == 1 and veSo[3:6].__eq__(listSoTrung[i]):
        print("Các số trúng là = " + listSoTrung[i])
        print("Bạn đã trúng " + listTenGiai[i] + ", số tiền của bạn là = " + listSoTien[i])

    elif i == 2 and (
            veSo[2:6].__eq__(listSoTrung[i][0:4]) or veSo[2:6].__eq__(listSoTrung[i][7:11]) or veSo[2:6].__eq__(
        listSoTrung[i][15:19])):
        print("Các số trúng là = " + listSoTrung[i][0:4])
        print("Các số trúng là = " + listSoTrung[i][7:11])
        print("Các số trúng là = " + listSoTrung[i][15:19])
        print("Bạn đã trúng " + listTenGiai[i] + ", số tiền của bạn là = " + listSoTien[i])

    elif i == 3 and veSo[2:6].__eq__(listSoTrung[i]):
        print("Bạn đã trúng " + listTenGiai[i] + ", số tiền của bạn là = " + listSoTien[i])

    elif i == 4 and (
            veSo[1:6].__eq__(listSoTrung[i][0:5]) or veSo[1:6].__eq__(listSoTrung[i][8:13]) or veSo[1:6].__eq__(
        listSoTrung[i][16:21])
            or veSo[1:6].__eq__(listSoTrung[i][24:29]) or veSo[1:6].__eq__(listSoTrung[i][32:37]) or veSo[1:6].__eq__(
        listSoTrung[i][40:45])
            or veSo[1:6].__eq__(listSoTrung[i][48:53])
    ):
        print("Các số trúng là = " + listSoTrung[i][0:5])
        print("Các số trúng là = " + listSoTrung[i][8:13])
        print("Các số trúng là = " + listSoTrung[i][16:21])
        print("Các số trúng là = " + listSoTrung[i][24:29])
        print("Các số trúng là = " + listSoTrung[i][32:37])
        print("Các số trúng là = " + listSoTrung[i][40:45])
        print("Các số trúng là = " + listSoTrung[i][48:53])
        print("Bạn đã trúng " + listTenGiai[i] + ", số tiền của bạn là = " + listSoTien[i])

    elif i == 5 and (
            veSo[1:6].__eq__(listSoTrung[i][0:5]) or veSo[1:6].__eq__(listSoTrung[i][8:13]) or veSo[1:6].__eq__(
        listSoTrung[i][16:21])):
        print("Các số trúng là = " + listSoTrung[i][0:5])
        print("Các số trúng là = " + listSoTrung[i][8:13])
        print("Các số trúng là = " + listSoTrung[i][16:21])
        print("Bạn đã trúng " + listTenGiai[i] + ", số tiền của bạn là = " + listSoTien[i])

    elif i == 6 and veSo[1:6].__eq__(listSoTrung[i]):
        print("Các số trúng là = " + listSoTrung[i])
        print("Bạn đã trúng " + listTenGiai[i] + ", số tiền của bạn là = " + listSoTien[i])

    elif i == 7 and veSo[1:6].__eq__(listSoTrung[i]):
        print("Các số trúng là = " + listSoTrung[i])
        print("Bạn đã trúng " + listTenGiai[i] + ", số tiền của bạn là = " + listSoTien[i])

    elif i == 8 and veSo[0:6].__eq__(listSoTrung[i]):
        print("Các số trúng là = " + listSoTrung[i])
        print("Bạn đã trúng " + listTenGiai[i] + ", số tiền của bạn là = " + listSoTien[i])
    else:
        countTrung = countTrung + 1
if countTrung == 9:
    print("Bạn trúng cái nịt")
