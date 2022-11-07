
import unittest # Importa o módulo unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # Importando o módulo Keys
from selenium.webdriver.common.by import By # Importando o módulo By
import time

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\Descargas\chromedriver_win32\chromedriver.exe") #valor de regreso "self"
    
    def test_buscar(self):
        driver = self.driver
        driver.get("https://www.google.com")
        self.assertIn("Google", driver.title) #Validando si "google" está en el titulo
        elemento= driver.find_element(By.NAME,"q")
        elemento.send_keys("Selenium") #Simulando el ingreso de datos
        elemento.send_keys(Keys.RETURN) 
        time.sleep(5) #Espera de 5 segundos
        assert "No se encontró el elemento:" not in driver.page_source #Validando si el elemento no está en la página

    def tearDown(self):     #cerrar unitest
        self.driver.close() #cerrar navegador
        
if __name__ == '__main__': #Ejecutar unitest
    unittest.main() 
