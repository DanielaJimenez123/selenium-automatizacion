from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

usuario = driver.find_element(By.ID, "userName" )
usuario.send_keys("Gustavo Pasieka")
time.sleep(2)
correo = driver.find_element(By.ID,"userEmail")
correo.send_keys("tuti.gusti21@gmail.com")
time.sleep(2)

direccion= driver.find_element(By.ID, "currentAddress")
direccion.send_keys("Castro 3000")
time.sleep(2)

dirpermanente= driver.find_element(By.ID, "permanentAddress")
dirpermanente.send_keys("Ucrania 4670")
time.sleep(2)
entregar = driver.find_element(By.ID, "submit")
entregar.click()

texto_usuario = driver.find_element(By.ID,"name").text
correo_texto= driver.find_element(By.ID, "email").text
direccion_texto = driver.find_element(By.XPATH,'//p[@id= "currentAddress"]').text
dirpermanente_texto = driver.find_element(By.XPATH, '//p[@id= "permanentAddress"]').text

if texto_usuario == "Name:Gustavo Pasieka" and correo_texto == "Email:tuti.gusti21@gmail.com" and direccion_texto== "Current Address : Castro 3000" and dirpermanente_texto == "Permananet Address :Ucrabia 4670":
    print("Todas son correctas")


driver.quit() 

