from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.fullscreen_window()
driver.get("https://safely-move.web.app/login")
time.sleep(4)

# --- Login ---
driver.find_element(By.ID, "email").send_keys("normaluser@test.com")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("Normaluser11")
time.sleep(5)
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

# ---------- Dashboard Tabs ----------
dashboard_links = [
    "/dashboard/BookParcel",
    "/dashboard/Myparcel",
    "/dashboard/payment",
    "/dashboard/Payment-history",
    "/dashboard/MyProfile"
]

for link in dashboard_links:
    driver.get("https://safely-move.web.app" + link)
    time.sleep(4)

# ---------- Back to Home ----------
driver.get("https://safely-move.web.app/")
time.sleep(1)

print("✅ System testing completed successfully!")
# driver.quit()
