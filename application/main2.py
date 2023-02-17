from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

def titre():
    driver = webdriver.Chrome()
    driver.get("https://www.reddit.com/")
    title = driver.title
    print(title)
    driver.close()
    return title

# def titreArticle():
#     driver.get("https://wikiroulette.co/")
#     titleArticle = driver.find_element(by=By.ID, value="firstHeading")
#     print(titleArticle)

titre()

