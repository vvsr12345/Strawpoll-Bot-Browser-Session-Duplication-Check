from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time
n=int(input("Enter the number of votes : "))
print()
path="C:\\Program Files\\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get("https://strawpoll.com/jhzd6qwjw")
for i in range(0,n+1):
    driver.delete_all_cookies()
    try:
        button=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@value='9c1zz2ugv55r']")))
        driver.execute_script("arguments[0].click();", button)
        buttons=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[@class='button is-primary is-fullwidth']")))
        driver.execute_script("arguments[0].click();", buttons)
    except:
        print()
    try:
        c=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//h1[@class='title']")))
        driver.back()
        print("Vote Successful")
        print()
    except:
        print()
    if i==n-1:
        driver.quit()