from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# --- Setup ---
driver = webdriver.Chrome()
driver.fullscreen_window()
driver.get("https://safely-move.web.app/login")
time.sleep(2)

# --- Login ---
driver.find_element(By.ID, "email").send_keys("deliveryman99@gmail.com")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("Deliveryman99")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[type='submit'], input[type='submit']").click()
time.sleep(2)

# --- Click SweetAlert "Continue" ---
continue_btn = driver.find_element(By.CSS_SELECTOR, "button.swal-button--confirm")
continue_btn.click()
time.sleep(2)

# --- Go to Dashboard -> MyProfile ---
dashboard_link = driver.find_element(By.LINK_TEXT, "Dashboard")
dashboard_link.click()
time.sleep(10)

print("✅ Parcel booked successfully!")
# driver.quit()
