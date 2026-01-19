from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# Maximize window
driver.maximize_window()
time.sleep(0.5)
driver.get("https://mini-mart-4242.web.app/Login")

# Login
driver.find_element(By.NAME, "email").send_keys("buyer75@gmail.com")
driver.find_element(By.NAME, "password").send_keys("Buyer12$")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(3)  # wait for login & navbar load

# Click Products using LINK_TEXT
driver.find_element(By.LINK_TEXT, "Products").click()
time.sleep(2)  # wait for products page load


# 🔥 Add first 3 products to cart
# 🔥 Add first 3 products to cart with sleep after each click
add_to_cart_buttons = driver.find_elements(
    By.XPATH, "//button[contains(text(),'Add to Cart')]"
)

for i in range(3):
    add_to_cart_buttons[i].click()
    time.sleep(2)   # ⏱ sleep AFTER each Add to Cart

driver.find_element(By.LINK_TEXT, "Home").click()
time.sleep(2)  # wait for products page load

driver.find_element(
    By.CSS_SELECTOR, "a[href='/dashboard/cart']"
).click()
time.sleep(3)

time.sleep(5)
driver.quit()