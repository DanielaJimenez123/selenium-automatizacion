from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
def formulario(driver):
    usuario = driver.find_element(By.ID, "userName" )
    usuario.send_keys("Gustavo Pasiekas")
    correo = driver.find_element(By.ID,"userEmail")
    correo.send_keys("tuti.gusti21@gmail.com")
    direccion = driver.find_element(By.ID,"currentAddress")
    direccion.send_keys("Manuel Maza 2754")
    dirpermanente= driver.find_element(By.ID, "permanentAddress")
    dirpermanente.send_keys("Manuel Maza 2660")
    entregar = driver.find_element(By.ID, "submit")
    time.sleep(2)
    entregar.click()
formulario(driver)

def validar_datos(driver, dato_esperado):
    exito_validaciones = True
    texto_usuario = driver.find_element(By.ID, "name").text
    if texto_usuario != dato_esperado['usuario']:
        print(f"Error en el campo nombre: se esperaba '{dato_esperado['usuario']}'")
        exito_validaciones = False
    correo_texto = driver.find_element(By.ID,"email").text
    if correo_texto != dato_esperado['correo']:
        print(f"Error en el campo correo: se esperaba '{dato_esperado['correo']}'")
        exito_validaciones = False
    direccion_texto = driver.find_element(By.XPATH,'//p[@id= "currentAddress"]').text
    if direccion_texto != dato_esperado['direccion']:
        print(f"Error en el campo dirección: Se esperaba '{dato_esperado['direccion']}'")
        exito_validaciones = False
    dirpermanente_texto= driver.find_element(By.XPATH, '//p[@id= "permanentAddress"]').text
    if dirpermanente_texto != dato_esperado['dirpermanente']:
        print(f"Error en el campo dirección: Se esperaba '{dato_esperado['dirpermanente']}'")
    if exito_validaciones == True:
        print("Todas las validaciones fueron correctas")
datos = {
    'usuario': 'Name:Gustavo Pasieka',
    'correo': 'Email:tuti.gusti21@gmail.com',
    'direccion': 'Current Address :Manuel Maza 2754',
    'dirpermanente': 'Permananet Address :Manuel Maza 2660'
}
validar_datos(driver, datos)







        


