from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# --- Setup ---
driver = webdriver.Chrome()
driver.fullscreen_window()
driver.get("https://safely-move.web.app/login")
time.sleep(2)

# --- Login ---
driver.find_element(By.ID, "email").send_keys("normaluser@test.com")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("Normaluser11")
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
time.sleep(2)

# --- Go to "Book A Parcel" ---
book_parcel_link = driver.find_element(By.LINK_TEXT, "Book A Parcel")
book_parcel_link.click()
time.sleep(2)

# --- Fill Booking Form ---
driver.find_element(By.ID, "phoneNumber").send_keys("01700500000")
time.sleep(2)

driver.find_element(By.ID, "parceltype").send_keys("Electronics")
time.sleep(2)

driver.find_element(By.ID, "parcelWeight").send_keys("2.5kg")
time.sleep(2)

driver.find_element(By.ID, "receiverName").send_keys("jonathon Doe")
time.sleep(2)

driver.find_element(By.ID, "receiverPhoneNumber").send_keys("01811111111")
time.sleep(2)

driver.find_element(By.ID, "parcelDeliveryAddress").send_keys("123 Example Street, Dhaka")
time.sleep(2)

driver.find_element(By.ID, "requestedDate").send_keys("20-01-2025")
time.sleep(2)

driver.find_element(By.ID, "latitude").send_keys("23.8103")
time.sleep(2)

driver.find_element(By.ID, "longitude").send_keys("90.4125")
time.sleep(2)

# --- Submit Booking ---
driver.find_element(By.CSS_SELECTOR, "button[type='submit'], input[type='submit']").click()
time.sleep(2)

print("✅ Parcel booked successfully!")
# driver.quit()
