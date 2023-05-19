import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# chrome_options = uc.ChromeOptions()
# chrome_options.add_argument("--headless")
driver = uc.Chrome()#options=chrome_options
url='https://chat.openai.com/chat'
driver.get(url)
time.sleep(3)
def login():
    print('Starting .......')
    driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div[1]/div[4]/button[1]/div').click()
    time.sleep(3)
    email = 'Enter your email'

    driver.find_element(By.XPATH,'//*[@id="username"]').send_keys(email)
    print('Email Login .......')
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div/main/section/div/div/div/div[1]/div/form/div[2]/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('Enter the PassWord')
    print('Password Login ......')
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div/main/section/div/div/div/form/div[2]/button').click()


    print('Loged in ......')
    driver.find_element(By.XPATH,'//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button/div').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]/div').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]/div').click()

login()


while True:
    user_input = input("Ask the Questions (or 0 to print all answers): ")
    if user_input == "0":
        break
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[2]/main/div[2]/form/div/div[2]/textarea').send_keys(user_input)
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[2]/main/div[2]/form/div/div[2]/button').click()
html = driver.page_source
bs = BeautifulSoup(html,"lxml")
chat = bs.find_all('a','flex py-3 px-3 items-center gap-3 rounded-md hover:bg-gray-500/10 transition-colors duration-200 text-white cursor-pointer text-sm')
if chat[0].text=='Clear conversations':
    WebDriverWait(driver,50).until(ec.text_to_be_present_in_element((By.XPATH,'//*[@id="__next"]/div[2]/div[2]/main/div[2]/form/div/div[1]/button/div'),'Regenerate response'))
    print(bs.prettify())
else:
    login()

