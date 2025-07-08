from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://gmail.com")

usuario = driver.find_element(By.ID, "identifierId")
usuario.send_keys("danielajimiranda@gmail.com")
usuario.send_keys(Keys.ENTER)
time.sleep(3)

clave = driver.find_element(By.NAME, "Passwd")
clave.send_keys("Jersey2025")
clave.send_keys(Keys.ENTER)