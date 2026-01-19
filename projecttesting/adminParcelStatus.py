from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

# ---------------- SETUP ----------------
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://safely-move.web.app/login")

wait = WebDriverWait(driver, 15)

# ---------------- LOGIN ----------------
email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
email_input.send_keys("adminuser@test.com")
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("Ab123123$")
time.sleep(1)

login_button = driver.find_element(
    By.CSS_SELECTOR, "button[type='submit'], input[type='submit']"
)
login_button.click()
time.sleep(2)
# ---------------- SWEET ALERT CONTINUE ----------------
continue_btn = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".swal-button--confirm"))
)
continue_btn.click()
time.sleep(2)

# ---------------- DASHBOARD → MY PROFILE ----------------
myprofile_link = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/dashboard/MyProfile"]'))
)
myprofile_link.click()
time.sleep(7)

# ---------------- DASHBOARD → ALL PARCEL ----------------
allparcel_link = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/dashboard/AllParcel"]'))
)
allparcel_link.click()
time.sleep(7)

# ---------------- CLICK MANAGE BUTTON (FIRST ONE) ----------------
manage_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Manage']"))
)
manage_button.click()
time.sleep(2)
# ---------------- WAIT FOR DIALOG ----------------
wait.until(EC.presence_of_element_located((By.NAME, "deliveryManId")))

# ---------------- SELECT DELIVERY MAN ----------------
delivery_select = Select(driver.find_element(By.NAME, "deliveryManId"))
delivery_select.select_by_visible_text("DeliveryMan99")

# ---------------- SET APPROXIMATE DATE ----------------
date_input = driver.find_element(By.ID, "approximateDate")
date_input.send_keys("2026-01-25")
time.sleep(2)
# ---------------- SUBMIT ----------------
set_btn = driver.find_element(By.XPATH, "//button[text()='Set Delivery Man']")
set_btn.click()

time.sleep(3)

# -------- CLOSE SET DELIVERY MAN DIALOG --------
close_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[.//span[text()='Close']]")
    )
)
close_btn.click()
time.sleep(2)
# -------- CLICK HOME --------
home_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='/']"))
)
home_btn.click()
time.sleep(2)


print("✅ Delivery Man assigned successfully!")

# driver.quit()
