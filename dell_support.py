#!/usr/bin/python3
"""
Dell support request creator
Dylan Graham 2016

Usage: dell_support.py <SERVICE TAG>

Depends on Firefox and Selenium
'pip3 install selenium'

Create 'form_details.py' containing your contact details/support information:

# Primary contact
company = ''
address0 = ''
address1 = ''
city = ''
country = ''    # 2 letter country code, eg: AU
state = ''
zip_code = ''
primary_first_name = ''
primary_last_name = ''
primary_phone_number = ''
primary_email = ''

# Secondary contact
secondary_first_name = ''
secondary_last_name = ''
secondary_phone_number = ''
secondary_email = ''

# Support details, examples provided
problem_details = '900GB 10k SAS6 - hard drive predicted failure'
error_message = 'Predictive failure reported'
troubleshoot = 'Drive replaced with spare.'
incident_type = 'Hard-Drive_Floppy_Zip-Drive'

Incident types can be:
'Audio'
'Audio_Speakers'
'Battery'
'BIOS'
'CD-ROM'
'Connection'
'Damage'
'Driver'
'DVD_CD RW_CD ROM'
'Fan_Temperature'
'Fiber Channel'
'Hard-Drive_Floppy_Zip-Drive'
'iSCSI'
'Keyboard_Mouse'
'MemoryError'
'Modem_FAX'
'Monitor'
'Network'
'Network Adapter'
'No Power'
'OpenManage Software'
'Operating System'
'Other Dont Know'
'Poor Performance'
'Port Replicator'
'Power Supply'
'Printer_Scanner_Camera'
'Processory Error'
'Rack Hardware'
'RAID'
'Reboots_Locksup'
'Tape Backup'
'Update-Software BIOS'
'Upgrade-Hardware'
'Upgrade-Software'
'Video'
'VideoAdapter_LCD'
"""

import form_details
import sys
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

service_tag = sys.argv[1]

# Check service tag format
valid = re.compile(r'^[A-Za-z0-9]{7}$')
if not re.match(valid, service_tag):
    print("Service tag should be 7 alphanumeric characters")
    sys.exit(1)

# If your system Firefox is older than 47.0.1, specify a newer version:
#binary = FirefoxBinary('/home/user/Downloads/firefox/firefox')
binary = FirefoxBinary('firefox')

# Start up web driver
driver = webdriver.Firefox(firefox_binary=binary)
driver.get("http://www.dell.com/support/incidents/au/en/aubsd1/Email/Welcome")
assert "Email Technical Support" in driver.title

elem_tag = driver.find_element_by_id("ServiceTag")
elem_tag.send_keys(service_tag)
elem_tag.send_keys(Keys.RETURN)

WebDriverWait(driver, 10)\
    .until(EC.presence_of_element_located((By.CLASS_NAME, "uif5_btnTxt")))\
    .click()

WebDriverWait(driver, 10)\
    .until(EC.presence_of_element_located((By.ID, "CompanyName")))\
    .send_keys(form_details.company)

driver.find_element_by_id("StreetAddress").send_keys(form_details.address0)
driver.find_element_by_id("StreetAddress1").send_keys(form_details.address1)
driver.find_element_by_id("City").send_keys(form_details.city)
Select(driver.find_element_by_id("NewCountry")).select_by_value(form_details.country)
Select(driver.find_element_by_id("NewState")).select_by_value(form_details.state)
driver.find_element_by_id("Zip").send_keys(form_details.zip_code)
driver.find_element_by_id("PrimaryFirstName").send_keys(form_details.primary_first_name)
driver.find_element_by_id("PrimaryLastName").send_keys(form_details.primary_last_name)
driver.find_element_by_id("PrimaryPhoneNumber").send_keys(form_details.primary_phone_number)
driver.find_element_by_id("PrimaryEmail").send_keys(form_details.primary_email)
driver.find_element_by_id("ConfirmEmail").send_keys(form_details.primary_email)
driver.find_element_by_id("SecondaryFirstName").send_keys(form_details.secondary_first_name)
driver.find_element_by_id("SecondaryLastName").send_keys(form_details.secondary_last_name)
driver.find_element_by_id("SecondaryPhoneNumber").send_keys(form_details.secondary_phone_number)
driver.find_element_by_id("SecondaryEmail").send_keys(form_details.secondary_email)
driver.find_element_by_id("SecondaryConfirmEmail").send_keys(form_details.secondary_email)
driver.find_element_by_id("btnContinue").click()

Select(WebDriverWait(driver, 10)
       .until(EC.presence_of_element_located((By.ID, "IncidentTypeID"))))\
    .select_by_value(form_details.incident_type)

Select(driver.find_element_by_id("NewOperatingSystem")).select_by_value("LINUX - OS")
Select(driver.find_element_by_id("NewOperatingSystemVersion")).select_by_value("LINUX - OS_ALL")
driver.find_element_by_id("ProblemDetails").send_keys(form_details.problem_details)
driver.find_element_by_id("ErrorMessage").send_keys(form_details.error_message)
driver.find_element_by_id("TroubleshootingSteps").send_keys(form_details.troubleshoot)
