from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
v = Options()
v.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=v)
driver.get('https://ucam.niter.edu.bd/Security/Login.aspx')
c = driver.find_elements(By.NAME,value='logMain$UserName')
print(len(c))
#driver.close()

username_input = driver.find_element(By.NAME, 'logMain$UserName')
username_input.send_keys('CS 2203099')

# Enter password
password_input = driver.find_element(By.NAME, 'logMain$Password')
password_input.send_keys('saniCSE99')

# Click the Login button
login_button = driver.find_element(By.NAME, 'logMain$Button1')
login_button.click()