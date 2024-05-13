from selenium import webdriver
from selenium.webdriver.common.by import By
import asyncio

siteLink = 'https://eksii.com/oyver'
mainpageButtonXpath = "/html/body/div[2]/div/a"
emailInputXpath = "//*[@id=\"eposta\"]"
emailSubmitXpath = "//*[@id=\"post\"]"
yasinXpath = "/html/body/div[2]/div/ul/li[2]/a"
onayXpath = "/html/body/div[1]/div/footer/div/button[1]"

edge_driver_location = "C:/Users/Polat Efe Kaya/Downloads/msedgedriver.exe"



async def start():
    await worker(1, 100000)

async def worker(start, end):
    fService = webdriver.EdgeService(executable_path=edge_driver_location)
    fdriver = webdriver.Edge(service=fService)

    for x in range(start, end):
        fdriver.get(siteLink)
        fdriver.find_element(By.XPATH ,mainpageButtonXpath).click()
        fdriver.find_element(By.XPATH ,emailInputXpath).send_keys(f"polatefekaya+{x}@icloud.com")
        fdriver.find_element(By.XPATH ,emailSubmitXpath).click()
        fdriver.find_element(By.XPATH ,yasinXpath).click()
        fdriver.find_element(By.XPATH, onayXpath).click()

asyncio.run(start())
