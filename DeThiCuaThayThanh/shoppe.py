from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("venv/chromedriver.exe"))

driver.get("https://shopee.vn/")

driver.implicitly_wait(3)
# driver.find_element(By.CSS_SELECTOR, "div.home-popup div.home-popup__close-area > div.shopee-popup__close-btn").click()

driver.implicitly_wait(5)

driver.execute_script("window.scrollTo(0, 200)")

driver.find_element(By.CSS_SELECTOR, "ul.image-carousel__item-list > li:nth-child(3) a:nth-child(1)").click()
driver.save_screenshot("vl.png")
driver.execute_script("window.scrollTo(0, 400)")

driver.implicitly_wait(5)
driver.save_screenshot("vl1.png")
banChay = driver.find_element(By.CSS_SELECTOR, "div.shopee-sort-bar > div.shopee-sort-by-options > div.shopee-sort-by-options__option:nth-child(3)")
print(banChay.text)
banChay.click()
driver.execute_script("window.scrollTo(0, 600)")

tenSanPham = driver.find_elements(By.CSS_SELECTOR, "div.row.shopee-search-item-result__items > div.col-xs-2-4.shopee-search-item-result__item > a > div > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div")
print(len(tenSanPham))
# for tenSP in tenSanPham:
#     print(tenSP.text)

for i in range(5):
    print(tenSanPham[i].text)
driver.save_screenshot("vl3.png")

for i in range(5):
    driver.implicitly_wait(5)
    # banChay = driver.find_element(By.CSS_SELECTOR, "ul.image-carousel__item-list > li:nth-child(3) a:nth-child(1)")
    # print(banChay.text)
    # banChay.click()

    driver.implicitly_wait(10)
    # driver.execute_script("window.scrollTo(0, 300)")
    clickVaoSanPham = driver.find_element(By.CSS_SELECTOR, "div.shopee-search-item-result > div.row.shopee-search-item-result__items > div:nth-child(" + str(i + 1) + ") > a")

    clickVaoSanPham.click()
    driver.implicitly_wait(5)
    nameSP = driver.find_element(By.CSS_SELECTOR, "div.product-briefing.flex.card.s9-a-0 > div:nth-child(3) > div > div:nth-child(1) > span").text
    print(" =============================================== ĐÃ VÀO TRANG SẢN PHẨM = " + nameSP + " ===============================================")
    driver.implicitly_wait(10)
    driver.execute_script("window.scrollTo(0, 4000)")
    driver.implicitly_wait(10)
    driver.save_screenshot("vl4.png")
    listBinhLuan = driver.find_elements(By.CSS_SELECTOR, "div.product-ratings__list > div.shopee-product-comment-list > div.shopee-product-rating > div.shopee-product-rating__main > div:nth-child(4) > div:nth-child(4)")

    for bl in listBinhLuan:
        print(bl.text)
    driver.implicitly_wait(5)
    driver.back()
    driver.implicitly_wait(5)
