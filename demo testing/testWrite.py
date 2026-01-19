from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

v = Options()
v.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=v)
driver.get('https://ucam.niter.edu.bd/Security/Login.aspx')

# Wait for the page to load
time.sleep(2)

# Enter username
username_input = driver.find_element(By.NAME, 'logMain$UserName')
username_input.send_keys('Arafat Hossain Sani')

# Enter password
password_input = driver.find_element(By.NAME, 'logMain$Password')
password_input.send_keys('your_password_here')  # Replace with actual password

# Click the Login button
login_button = driver.find_element(By.NAME, 'logMain$btnLogin')
login_button.click()
