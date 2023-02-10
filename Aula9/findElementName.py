from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\fabio.c\Documents\extrair_dados\Aula3\chromedriver_win32\chromedriver.exe")

driver.get("https://www.imdb.com/")

driver.implicitly_wait(3) # seconds

campoBusca = driver.find_elements_by_name("q")[0] #comando bastante utilizado em campos input, onde se tem ou não um formulário junto com o comando input

campoBusca.send_keys("Titanic") #comando .send_keys serve para enviar letras a determinado local, usado para enviar em dados input 


