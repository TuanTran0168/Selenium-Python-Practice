from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("venv/chromedriver.exe"))
driver.get("https://tiki.vn/dien-thoai-may-tinh-bang/c1789")

driver.implicitly_wait(5)
banChay = driver.find_element(By.CSS_SELECTOR, "div.Sorter__Tabs-sc-1u1tc3w-3 > div.sort-list > a:nth-child(2)")
print(banChay.text)
banChay.click()

tenTop5SanPham = driver.find_elements(By.CSS_SELECTOR,
                                      "div.CategoryViewstyle__Right-sc-bhstkd-1 > div.inner > div.ProductList__NewWrapper-sc-1dl80l2-0 > div a.product-item span.style__StyledItem-sc-18svp8n-0 div.name")
giaTop5SanPham = driver.find_elements(By.CSS_SELECTOR,
                                      "div.CategoryViewstyle__Right-sc-bhstkd-1 > div.inner > div.ProductList__NewWrapper-sc-1dl80l2-0 > div a.product-item span.style__StyledItem-sc-18svp8n-0 div.price-discount__price")
# countTop5 = 0

# for tenSP in tenTop5SanPham:
#     if countTop5 == 5:
#         break;
#     else:
#         listTop5.append(tenSP)
#         countTop5 = countTop5 + 1
#         print(tenSP.text)

for i in range(5):
    print(tenTop5SanPham[i].text + " " + giaTop5SanPham[i].text)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for i in range(5):
    driver.implicitly_wait(10)
    banChay = driver.find_element(By.CSS_SELECTOR, "div.Sorter__Tabs-sc-1u1tc3w-3 > div.sort-list > a:nth-child(2)")
    print(banChay.text)
    banChay.click()

    driver.implicitly_wait(10)
    sanPham = driver.find_element(By.CSS_SELECTOR,
                                  "div.CategoryViewstyle__Right-sc-bhstkd-1 > div.inner > div.ProductList__NewWrapper-sc-1dl80l2-0 > div:nth-child(" + str(
                                      i + 1) + ") a.product-item")
    driver.implicitly_wait(5)
    sanPham.click()
    driver.implicitly_wait(5)
    tenSP = driver.find_element(By.CSS_SELECTOR,
                                "div.styles__StyledProductContent-sc-1f8f774-0 > div.header h1.title").text
    print("\n===========================================" + tenSP + "===========================================\n")
    driver.save_screenshot(tenSP[0:1] + str(i) + ".png")
    driver.execute_script("window.scrollTo(0,3500)")
    driver.implicitly_wait(10)
    tatCaBinhLuan = driver.find_elements(By.CSS_SELECTOR,
                                         "div.customer-reviews__inner div.review-comment > div:nth-child(2) > div.review-comment__content")
    for bl in tatCaBinhLuan:
        print(bl.text)
    print("\n")
    driver.back()
    driver.implicitly_wait(10)

driver.quit()
