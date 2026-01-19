import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://accounts.google.com/v3/signin/identifier?authuser=0&continue=https%3A%2F%2Fmail.google.com%2Fmail&ec=GAlAFw&hl=en&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession")

wait = WebDriverWait(driver, 10)

# Click "Create account"
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Create account']"))).click()

# Click "For my personal use"
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='For my personal use']"))).click()

# Fill first and last name
wait.until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys("Md Arafat")
wait.until(EC.presence_of_element_located((By.ID, "lastName"))).send_keys("Hossain")

# Click Next
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))).click()

# Fill DOB and Gender
# ---- Select Month ----
month_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "month")))
month_dropdown.click()
march_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-value='3']")))
march_option.click()

# ---- Enter Day ----
day_input = driver.find_element(By.ID, "day")
day_input.send_keys("15")

# ---- Enter Year ----
year_input = driver.find_element(By.ID, "year")
year_input.send_keys("1999")

# ---- Select Gender ----
# ---- Open Gender dropdown ----
gender_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "gender")))
gender_dropdown.click()

# ---- Select 'Male' option ----
male_option = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//ul[@role='listbox']//li[@role='option']//span[text()='Male']")
))
male_option.click()


# ---- Click Next button ----
next_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[.//span[text()='Next']]")
))
next_button.click()

# ---- Wait for Username field ----
username_input = wait.until(EC.presence_of_element_located(
    (By.NAME, "Username")
))
username_input.send_keys("arafat1.test123")   # <-- change username as needed

# ---- Click Next button ----
next_button_2 = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[.//span[text()='Next']]")
))
next_button_2.click()

time.sleep(7)
driver.quit()
print("✅ Form filled and Next button clicked successfully!")
