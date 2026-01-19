from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Start browser
driver = webdriver.Chrome()

# 2. Maximize the window (full screen)
driver.maximize_window()

# 3. Open your website
driver.get("https://safely-move.web.app/")  # change to your login page

# 4. Wait for page load
time.sleep(10)

# 5. Input Email & Password
email_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "password")

email_input.send_keys("deliveryman99@gmail.com")
password_input.send_keys("Deliveryman99")
time.sleep(2)
# 6. Click Login Button
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit'], input[type='submit']")
login_button.click()

# 7. Wait to see result
time.sleep(5)

print("Logged in, current URL:", driver.current_url)

# driver.quit()   # uncomment to close browser
