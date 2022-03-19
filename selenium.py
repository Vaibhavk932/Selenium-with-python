#  GRIP TASK 6 
#  WEB TESTING WITH SELENIUM
#  LANGUAGE USED :- PYTHON
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome("C:\\Users\\Lenovo ideaPad\\chromedriver.exe")
driver.get("https://www.thesparksfoundationsingapore.org")

# 1) VERIFICATION OF HOME PAGE
try:
    driver.find_element_by_partial_link_text("The Sparks Foundation").click()
    print("Home link is Working.\n")
except NoSuchElementException:
    print("Home link does not exist.\n")

# 2) FINDING "ADVISORS AND PATRONS" FROM ABOUT US SECTION
try:
    driver.find_element_by_link_text('About Us').click()
    time.sleep(2)
    driver.find_element_by_link_text('Advisors And Patrons').click()
    time.sleep(4)
    print('We find Advisors and Patrons from About us section successfully.\n')
except NoSuchElementException:
    print("We did not find any Advisors and Patrons from About us section\n")
    time.sleep(1)



# 3) FINDING "SERVICE QUALITY VALUES " FROM POLICIES AND CODE SECTION
try:
    driver.find_element_by_link_text('Policies and Code').click()
    time.sleep(2)
    driver.find_element_by_link_text('Service Quality Values').click()
    time.sleep(4)
    print('We find Service Quality Values from Policies and Code section successfully.\n')
except NoSuchElementException:
    print("We did not find any Service Quality Values from Policies and Code section.\n")
    time.sleep(1)

# 4) FINDING "CORPORATE PROGRAM " FROM PROGRAMS SECTION
try:
    driver.find_element_by_link_text('Programs').click()
    time.sleep(2)
    driver.find_element_by_link_text('Corporate Programs').click()
    time.sleep(4)
    print('We find Corporate Programs from Programs section successfully.\n')
except NoSuchElementException:
    print("We did not find any Corporate Programs from Programs section successfully\n")
    time.sleep(1)

# 5) FINDING "AI IN EDUCATION" FROM LINKS SECTION
try:
    driver.find_element_by_link_text('LINKS').click()
    time.sleep(2)
    driver.find_element_by_link_text('AI in Education').click()
    time.sleep(4)
    print('We find AI in education from links section successfully.\n')
except NoSuchElementException:
    print("We did not find any AI in education from links section successfully.\n")
    time.sleep(1)

# 6) FINDING "BRAND AMBASSADOR" FROM JOIN US SECTION
try:
    driver.find_element_by_link_text('Join Us').click()
    time.sleep(2)
    driver.find_element_by_link_text('Brand Ambassador').click()
    time.sleep(4)
    print('We find  Brand Ambassador from join us section successfully..\n')
except NoSuchElementException:
    print("We did not find any  Brand Ambassador from join us section successfully.\n")
    time.sleep(1)

# 7) EXAMINING CONTACT US PAGE
try:
    driver.find_element_by_link_text('Contact Us').click()
    time.sleep(4)
    print('Contact Us page exist.\n')
except NoSuchElementException:
    print("Contact us page does not exist.\n")
    time.sleep(1)

# 8) EXAMINING SCROLL TO TOP BUTTON
try:
    driver.find_element_by_id("toTopHover").click()
    print('Scroll to top button is working properly.\n')
    time.sleep(2)
except NoSuchElementException:
    print("Scroll to top button does not work properly as expected.\n")
    time.sleep(1)

# 9) EXAMINING 6th SLIDE OF THE CAROUSEL

try:
    driver.find_element_by_link_text('6').click()
    time.sleep(4)
    print('the 6th slide of the carousel is there.\n')
except NoSuchElementException:
    print("6th slide of the carousel absent.\n")
    time.sleep(1)

#10) EXAMINING STUDENT SCHOLARSHIP PROGRAM
try:
    driver.find_element_by_link_text('Student Scholarship Program').click()
    print('the Student Scholarship Program page is verified.\n')
    time.sleep(4)
except NoSuchElementException:
    print('Student Scholarship Program is absent.\n')

#11) EXAMINING RESUME WRITING
try:
    driver.find_element_by_link_text('Resume Writing').click()
    print('the Resume Writing page is there.\n')
    time.sleep(4)
except NoSuchElementException:
    print('Resume Writing page is absent.\n')
    time.sleep(1)