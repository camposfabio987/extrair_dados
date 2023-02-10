from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\kikio\Documents\extrair_dados\Aula3\chromedriver_win32\chromedriver.exe") #faz a comuunicação entre o selenium e o navegador, abrindo o chrome.

driver.get("https://www.google.com") #abre qualquer site dentro do chrome, só buscar a ref