# Importando bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 

email = "pythonautomacaoctrlplay@gmail.com" 
senha = "ctrlplay" 

pesquisa = input("Insira um tema: ") # Input para pegar o que o usuário deseja

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install())) # Abrir o Chrome

driver.get("https://accounts.google.com") # Navegar até o link desejado
time.sleep(5) # Esperar X segundos

# Inserindo email
email_input = driver.find_element(By.ID, "identifierId")
email_input.send_keys(email)
email_input.send_keys(Keys.RETURN)
time.sleep(5)

# Inserindo senha
senha_input = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
senha_input.send_keys(senha)
senha_input.send_keys(Keys.RETURN)
time.sleep(8)

driver.get("https://www.youtube.com")
time.sleep(2)

# Encontrando a barra de pesquisa do youtube
barra_de_pesquisa = driver.find_element(By.NAME, "search_query")

# Limpando barra de pesquisa
barra_de_pesquisa.clear()
barra_de_pesquisa.send_keys(pesquisa)
barra_de_pesquisa.send_keys(Keys.RETURN)
time.sleep(10)