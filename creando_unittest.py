import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class creando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_buscar(self):
        driver = self.driver
        driver.get("https://www.google.com")
        self.assertGreaterEqual("google", driver.title)
        elemento = driver.find_element(By.NAME, "q")
        elemento.send_keys("selenium")
        elemento.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "No se encontró el elemento" not in driver.page_source
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()

