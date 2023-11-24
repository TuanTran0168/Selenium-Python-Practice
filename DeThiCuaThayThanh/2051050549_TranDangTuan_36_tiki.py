
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("venv/chromedriver.exe"))

kw = "Ipad pro"
driver.get("https://tiki.vn/")

driver.implicitly_wait(5)
search = driver.find_element(By.CSS_SELECTOR, "div.FormSearchStyle__FormRevamp-sc-1idbenb-4 > input")
search.send_keys(kw)
search.send_keys(Keys.ENTER)


driver.implicitly_wait(5)

tenSanPham = driver.find_elements(By.CSS_SELECTOR, "div.ProductList__NewWrapper-sc-1dl80l2-0 > div > a > div > span > div.info > div.name > h3")
giaSanPham = driver.find_elements(By.CSS_SELECTOR, "div.ProductList__NewWrapper-sc-1dl80l2-0 > div > a > div > span > div.info div.price-discount__price")
for i in range(5):
        print(tenSanPham[i].text + " " + giaSanPham[i].text)

for i in range(5):
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, "div.ProductList__NewWrapper-sc-1dl80l2-0 > div:nth-child(" + str(i + 1) + ") > a").click()

    driver.implicitly_wait(5)
    driver.save_screenshot("a" + str(i + 1) + ".png")


    driver.implicitly_wait(5)

    driver.execute_script("window.scrollTo(0, 3000)")
    driver.implicitly_wait(5)

    listBinhLuan = driver.find_elements(By.CSS_SELECTOR, "div.style__StyledComment-sc-10ol6xi-5.review-comment > div:nth-child(2) > div.review-comment__content")
    print("====================================== BÌNH LUẬN ======================================================")
    for bl in listBinhLuan:
        print( " - " + bl.text)
    driver.implicitly_wait(5)
    driver.back()

driver.quit()
