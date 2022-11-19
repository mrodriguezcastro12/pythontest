from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#############################################
#Negativo
#given
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://www.python.org")

#assert "Python" in driver.title
#when
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("varible")

boton = driver.find_element(By.ID, "submit")
boton.click
time.sleep(5)

#then
#resultado = driver.find_element_by_xpath("//*[@id='content']/div/section/form/ul/p")
#No results found.
#resultado.

#########################################
#positivo
#given
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://www.python.org")

#assert "Python" in driver.title
#when
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("variable")

boton = driver.find_element(By.ID, "submit")
boton.click
time.sleep(5)

driver.close()