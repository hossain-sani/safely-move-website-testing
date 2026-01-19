from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Start browser
driver = webdriver.Firefox()

# 2. Maximize window
driver.maximize_window()

# 3. Open website
driver.get("https://safely-move.web.app/")
time.sleep(6)   # wait for page load

# 4. Click Login button (Home page)
login_btn = driver.find_element(By.XPATH, "//button[text()='Login']")
login_btn.click()
time.sleep(5)

# 5. Input Email & Password
email_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "password")

email_input.send_keys("deliveryman99@gmail.com")
password_input.send_keys("Deliveryman99")
time.sleep(2)

# 6. Click Login submit button
submit_btn = driver.find_element(
    By.CSS_SELECTOR, "button[type='submit'], input[type='submit']"
)
submit_btn.click()

time.sleep(5)

print("✅ Login test completed successfully")
# driver.quit()
