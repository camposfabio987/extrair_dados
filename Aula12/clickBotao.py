from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\kikio\Documents\extrair_dados\Aula3\chromedriver_win32\chromedriver.exe")

'''driver.get("https://empresas.americanas.com.br/produto/1611315933/iphone-11-apple-64gb-preto-tela-6-1-4g-camera-12mp-ios?chave=hmem_vitrine_13_2106")
driver.maximize_window()
driver.implicitly_wait(4) # seconds

driver.find_elements_by_xpath("/html/body/div[1]/div/div/main/div[2]/div[2]/div[3]/a")[0].click()
driver.refresh()'''

#Outra forma de fazer, mais organizada e mais detalhada, porém gasta + memórias
#botao = driver.find_element_by_id("btn-buy") 
#botao.click()

driver.get("https://www.imdb.com/")

driver.find_elements_by_name("q")[0].send_keys("Titanic")

driver.implicitly_wait(2) # seconds

driver.find_element_by_id("iconContext-magnify").click()