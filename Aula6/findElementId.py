from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\kikio\Documents\extrair_dados\Aula3\chromedriver_win32\chromedriver.exe")

driver.get("https://www.infomoney.com.br/")

driver.implicitly_wait(3) # aguarda a página carregar, um delay que é dado em segundos.

dados1 = driver.find_element_by_id("high").text # com o id, é recomendável usar este comando, pois ID é único e esse pega um só.
dados2 = driver.find_elements_by_id("high")[0].text #com este comando, consegue escolher qual texto pegar, com base na ordem do

print(dados1)
print("--------------------------")
print(dados2)

driver.get("https://www.uol.com.br/")

driver.implicitly_wait(3) 

dados3 = driver.find_element_by_id("ldxqr665").text 

print(dados3)