'''

test automazione
https://practicetestautomation.com/practice-test-login/

student /// Password123
inserisci credenziali e poi submit
stampa il messaggio di login effettuato
poi clicca su log out, successivamente stampate il driver.title e chiudete il driver

'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time



driver = webdriver.Firefox()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

time.sleep(3)

search_bar = driver.find_element(By.ID, "username")
search_bar.send_keys("student" + Keys.RETURN)

time.sleep(3)

search_bar = driver.find_element(By.ID, "password")
search_bar.send_keys("Password123" + Keys.RETURN)

time.sleep(3)

search_bar = driver.find_element(By.ID, "submit")
search_bar.send_keys(Keys.RETURN)

time.sleep(3)

search_bar = driver.find_element(By.XPATH, "/html/body/div/div/section/div/div/article/div[2]/div/div/div/a")
titolo = driver.title
print(titolo)
search_bar.send_keys(Keys.RETURN)
driver.close()


