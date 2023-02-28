from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\fabio.c\Documents\extrair_dados\Aula3\chromedriver_win32\chromedriver.exe")

driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

elementoAImagem = driver.find_elements_by_class_name("navbar-brand")[0]
elementoImg = elementoAImagem.find_element_by_tag_name("img") #aqu busca a tag img que está dentro da tagA, fazendo isso, vc restringe a selenium buscar dentro de uma tag específica aquilo q vc precisa.
atributoSrc = elementoImg.get_attribute("src") #comando p buscar atributos dentro de qualquer tag
print(atributoSrc)

driver.get("https://www.melhorcambio.com/dolar-hoje")

elementoCotacao = driver.find_element_by_id("comercial")
valorCotacao = elementoCotacao.get_attribute("value")
classeElemento = elementoCotacao.get_attribute("class")
tipoElemento = elementoCotacao.get_attribute("type")

print(valorCotacao)
print(classeElemento)
print(tipoElemento)

driver.close()