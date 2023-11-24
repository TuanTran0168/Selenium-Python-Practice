from os import terminal_size
from re import search
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class MyClass(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MyClass, self).__init__(*args, **kwargs)
        self.driver = webdriver.Chrome(service=Service("venv/chromedriver.exe"))
        self.driver.get("https://www.google.com.vn/?hl=vi")
    def test_FPT(self):
        search = self.driver.find_element(By.NAME, "q")
        search.send_keys("Dien thoai")
        search.submit()

        self.driver.find_element(By.CSS_SELECTOR, "div#search > div> div > div:nth-child(3) a").click()
        self.driver.implicitly_wait(3)
        # v = Select(driver.find_element(By.CSS_SELECTOR, "div.cdt-dropdown-button"))
        # v.select_by_index(2)
        self.driver.find_element(By.CSS_SELECTOR, "div.cdt-dropdown-button").click()
        self.driver.find_element(By.CSS_SELECTOR, "ul.cdt-dropdown-menu > li:nth-child(4)").click()
        self.driver.implicitly_wait(3)

        self.driver.save_screenshot("giaCao.png")

        tenDienThoai = self.driver.find_elements(By.CSS_SELECTOR, "div.cdt-product > div.cdt-product__info h3")
        giaDienThoai = self.driver.find_elements(By.CSS_SELECTOR, "div.cdt-product > div.cdt-product__info > div.cdt-product__show-promo progress pdiscount2 > div.progress.pdiscount2")

        # for dt in tenDienThoai:
        #     print(dt.text)
        #

        # for i in range(len(tenDienThoai)):
        #     if len(giaDienThoai[i]) == 0:
        #         print("Tên điện thoại = " + tenDienThoai[i].text + " Giá = " + 0)
        #     else:
        #         print("Tên điện thoại = " + tenDienThoai[i].text + " Giá = " + giaDienThoai[i].text)

        countSamsung = 0
        for dt in tenDienThoai:
            if dt.text.__contains__("Samsung"):
                print(dt.text)
                countSamsung = countSamsung + 1;

        print(countSamsung)
        self.assertTrue(countSamsung == 11)

