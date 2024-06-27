# AUTOMATION OF BOOKING A APPOINTMENT WITH DOCTOR

# import required libraries and modules
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

# initialise the browser
d=webdriver.Chrome()

# maximize the browser
d.maximize_window()

# Navigate to the url
d.get('https://www.curahospitals.com/')


# Navigate to the book appointment tab and fill the details
d.find_element(By.XPATH,'//*[@id="navbar"]/div/div/div[2]/div[2]/a/img').click()
time.sleep(5)

# Details of patient
d.find_element(By.ID,'ename').send_keys('Tester')
d.find_element(By.ID,'eemail').send_keys('Tester1@gmail.com')
d.find_element(By.ID,'ephone').send_keys('9876543210')
d.find_element(By.ID,'emessage').send_keys('Hi This is tester1 from testing environment reporting.')
ele=Select(d.find_element(By.ID,'ecourse'))
ele.select_by_index(1)

# Handling Captcha
captcha=d.find_element(By.XPATH,'//*[@id="enquiry_form"]/div/span[1]').text
cap_int=str(eval(captcha[:-2]))
d.find_element(By.ID,'capcha1').send_keys(cap_int)
time.sleep(5)

# submit
d.find_element(By.XPATH,'//*[@id="submit"]').click()

time.sleep(5)
d.quit()
