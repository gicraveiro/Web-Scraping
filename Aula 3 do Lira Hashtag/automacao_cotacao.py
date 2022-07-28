# Exercise:
# Given a prices table, update the exchange rates of dolar, euro and gold comparing to real
# Then update the prices of the products on the chart (both columns purchase price and sale price)

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

browser = webdriver.Firefox()

browser.get("https://www.melhorcambio.com/dolar-hoje")

cotacao_dolar = browser.find_element(By.XPATH,'//*[@id="comercial"]').get_attribute("value")
cotacao_dolar = cotacao_dolar.replace(",",".")
print(cotacao_dolar)

browser.get("https://www.melhorcambio.com/euro-hoje")
cotacao_euro = browser.find_element(By.XPATH,'//*[@id="comercial"]').get_attribute("value")
cotacao_euro = cotacao_euro.replace(",",".")
print(cotacao_euro)

browser.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = browser.find_element(By.XPATH,'//*[@id="comercial"]').get_attribute("value")
cotacao_ouro = cotacao_ouro.replace(",",".")
print(cotacao_ouro)

browser.quit()

# Update prices according to currency
chart = pd.read_excel("Produtos.xlsx")
print(chart,"\n")

chart.loc[chart["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
chart.loc[chart["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
chart.loc[chart["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)
chart["Preço de Compra"] = chart["Cotação"] * chart["Preço Original"]
chart["Preço de Venda"] = chart["Preço de Compra"] * chart["Margem"]

print(chart)
chart.to_excel("Updated Products.xlsx", index=False) #saving
