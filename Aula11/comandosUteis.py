from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\kikio\Documents\extrair_dados\Aula3\chromedriver_win32\chromedriver.exe")

driver.get("https://www.imdb.com/title/tt0120338/?ref_=fn_al_tt_1")

driver.minimize_window() #minimiza a tela caso não esteja 

driver.implicitly_wait(2) # delay

driver.maximize_window() #maximiza a tela caso não esteja

driver.implicitly_wait(2) # delay

driver.get("https://empresas.americanas.com.br/produto/1611315933/iphone-11-apple-64gb-preto-tela-6-1-4g-camera-12mp-ios?chave=hmem_vitrine_13_2106")

driver.back() #simula a seta de voltar do browser

driver.implicitly_wait(5) # delay

driver.forward() #simula a seta de avançar do browser

driver.refresh() #atualiza a página

driver.implicitly_wait(5) #delay

driver.close() #fecha a página
