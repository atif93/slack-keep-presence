import sys
import time
from selenium import webdriver

driver = webdriver.Chrome(sys.argv[2])
driver.get(sys.argv[1])
while(True):
    time.sleep(600)
    driver.refresh()