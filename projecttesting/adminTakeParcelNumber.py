from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

# Setup
driver = webdriver.Firefox()
# driver.fullscreen_window()
driver.get("https://safely-move.web.app/login")
time.sleep(2)

# Login
email_input = driver.find_element(By.ID, "email")
email_input.send_keys("admin2@gmail.com")
time.sleep(2)

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("Admin123$")
time.sleep(2)

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit'], input[type='submit']")
login_button.click()
time.sleep(2)

# Wait for "Continue" SweetAlert button and click
continue_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".swal-button.swal-button--confirm"))
)
continue_btn.click()
time.sleep(2)

# Go to Dashboard → MyProfile
dashboard_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/dashboard/MyProfile"]'))
)
dashboard_link.click()
time.sleep(2)

# Go to Dashboard → AllParcel
allparcel_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/dashboard/AllParcel"]'))
)
allparcel_link.click()
time.sleep(2)

# Get total parcel number
total_parcel_text = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "h1.text-3xl.font-bold.italic"))
).text

# Extract number from text
match = re.search(r"Total Parcel\s*:\s*(\d+)", total_parcel_text)
if match:
    total_parcel = match.group(1)
    print("📦 Total Parcel Count:", total_parcel)
else:
    print("❌ Could not find parcel count")

# (optional) Close browser
# driver.quit()
