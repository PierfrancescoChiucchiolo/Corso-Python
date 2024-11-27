'''

esercizio selenium


semplice documento html:
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>esempio html</title>
</head>
<body>
    <h1 id="il mio titolo">il mio primo titolo</h1>
    <h2>secondo</h2>
    <h6>terzo</h6>
    <p>paragrafo semplice</p>
    <img src="imagine.jpeg" alt="prima immagine"><br>
    <button >testo</button>
    <table border="1">
        <tr>
            <td class="cella">nome</td>
            <td class="cella">cognome</td>
            <td class="cella">indirizzo</td>
        </tr>
        <tr>
            <td>Tommaso</td>
            <td>Muraca</td>
            <td>via roma</td>
        </tr>
        <tr>
            <td>Giovanni</td>
            <td>Rossi</td>
            <td>via milano</td>
        </tr>
    </table>
</body>
</html>


Visita Wikipedia, cerca "Python (programming language)", e stampa il titolo della pagina dei risultati

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
driver.get("https://www.wikipedia.org")
driver.maximize_window()
titolo = driver.title
print(titolo)

time.sleep(3)

search_bar = driver.find_element(By.ID, "searchInput")
search_bar.send_keys("Python (programming language)" + Keys.RETURN)

time.sleep(3)
titolo = driver.title
print(titolo)

## paragrafo = driver.find_element(By.CLASS_NAME, "mw-page-title-main")
## print(paragrafo)


