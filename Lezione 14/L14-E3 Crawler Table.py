'''

Visita https://www.w3schools.com/html/html_tables.asp
Estrai i dati dalla prima tabella sulla pagina e stampali in formato leggibile

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
driver.get("https://www.w3schools.com/html/html_tables.asp")
driver.maximize_window()

time.sleep(3)

search_bar = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[1]/div[3]/div/table/tbody")



companies = driver.find_elements(By.XPATH, "/html/body/div[5]/div[1]/div[1]/div[3]/div/table/tbody/tr[1]/th[1]")
contacts = driver.find_elements(By.XPATH, "/html/body/div[5]/div[1]/div[1]/div[3]/div/table/tbody/tr[1]/th[2]")
countries = driver.find_elements(By.XPATH, "/html/body/div[5]/div[1]/div[1]/div[3]/div/table/tbody/tr[1]/th[3]")

for company, contact, country in zip(companies, contacts, countries):
    print(company.text + " " + contact.text + " " + country.text)

driver.quit()