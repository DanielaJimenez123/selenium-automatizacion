from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
driver= webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")
desplegar= driver.find_element(By.CLASS_NAME, "css-1wa3eu0-placeholder")
desplegar.click()
seleccion= driver.find_element(By.XPATH,"//div[text()='Grupo 1, opción 2']")
seleccion.click()
