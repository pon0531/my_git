# -*- coding: utf-8 -*-
"""
Created on Fri May 12 12:50:50 2023

@author: USER
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

url ="https://www.thsrc.com.tw/"

driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(3)
driver.get(url)

#　高鐵進站畫面，我同意btn
Confirm_btn =  driver.find_element(By.CLASS_NAME, "swal2-confirm")
Confirm_btn.click()

driver.implicitly_wait(1)

# 高鐵時間，查詢btn
Search_btn =  driver.find_element(By.ID, "start-search")
Search_btn.click()

driver.implicitly_wait(3)
Table_btn =  driver.find_element(By.CLASS_NAME, "tr-table")
Table_btn.click()

driver.implicitly_wait(3)
Table_order =  driver.find_element(By.CLASS_NAME, "order ")
Table_order.click()

driver.implicitly_wait(3)

all_handles = driver.window_handles

driver.switch_to.window(all_handles[1])
cnt = 1
while True:
    print("Try again,")
    print(cnt)
    cnt = cnt+1
    driver.implicitly_wait(2)
    print(driver.current_url)
    print(driver.title)
    if (str(driver.title) == "台灣高鐵網路訂票"):
        break;

url  = driver.current_url
driver.get(url)
print(url)
print("sccuess to next page")

Confirm_right =  driver.find_element(By.ID, "cookieAccpetBtn")
Confirm_right.click()

select_start_station = Select(driver.find_element(By.ID, "BookingS1Form_selectStartStation"))
select_start_station.select_by_value('4')

select_Destination_station = Select(driver.find_element(By.ID, "BookingS1Form_selectDestinationStation"))
select_Destination_station.select_by_value('5')

Submit_btn =  driver.find_element(By.ID, "SubmitButton")
Submit_btn.click()