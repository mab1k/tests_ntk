import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import Select
import time
import os
import random


PATH_CHROME = '/home/user/selenium/chrome-linux64/chrome'
PATH_CHROME_DRIVER = '/usr/local/bin/chromedriver'
PROXY = '--proxy-server=http://192.168.4.219:3130'
URL = "http://192.168.4.17/newdesign_old/ntk/"
FILE_PATH = "/home/user/selenium/test.txt"

@pytest.fixture(scope="module")
def driver():
    service = Service(PATH_CHROME_DRIVER)

    chrome_options = Options()
    chrome_options.binary_location = PATH_CHROME
    #chrome_options.add_argument(PROXY) 
    chrome_options.add_argument('--no-sandbox') 
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    
    yield driver
   
    driver.quit()
    
def login(driver):
    try:
        driver.get(URL)  

        button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "siteAuto"))
        )
        button.click()

        login_input = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, "floatingInput"))
        )
        login_input.send_keys("pupa")

        password_input = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, "floatingPassword"))
        )
        password_input.send_keys("123")

        button_auth = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "authBtn"))
        )
        button_auth.click()
    except Exception:
        pytest.fail("Авторизация прошла не успешно")
        
   
def test_registration(driver):
    login(driver)
    
    time.sleep(1)

def test_ntk(driver):
    try:
        driver.get(URL)  
        
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form.mt-4 input[type='submit']"))
        )
        
    
        button.click()
        time.sleep(7)
        select_element = Select(driver.find_element(By.CSS_SELECTOR, '.floating > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(2) > select:nth-child(1)'))

        options = select_element.options

#Здесь можем сделать рандомно если надо
        random_index = 1


        select_element.select_by_index(random_index)
        
        select_element1 = Select(driver.find_element(By.CSS_SELECTOR, 'div.field:nth-child(3) > select:nth-child(1)'))
        options1 = select_element1.options
        random_index1 = random.randint(1, len(options1) - 1)
        select_element1.select_by_index(random_index)
        
        select_element2 = Select(driver.find_element(By.CSS_SELECTOR, 'div.field:nth-child(4) > select:nth-child(1)'))
        options2 = select_element2.options
        random_index2 = random.randint(1, len(options2) - 1)
        select_element2.select_by_index(random_index)
        
        select_element3 = Select(driver.find_element(By.CSS_SELECTOR, 'div.field:nth-child(5) > select:nth-child(1)'))
        options3 = select_element3.options
        random_index3 = random.randint(1, len(options3) - 1)
        select_element3.select_by_index(random_index)
        
        select_element4 = Select(driver.find_element(By.CSS_SELECTOR, 'div.field:nth-child(6) > select:nth-child(1)'))
        options4 = select_element4.options
        random_index4 = random.randint(1, len(options4) - 1)
        select_element4.select_by_index(random_index)
        
       
        
        select_element_theme = Select(driver.find_element(By.CSS_SELECTOR, '.floating > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > form:nth-child(1) > div:nth-child(3) > div:nth-child(2) > select:nth-child(1)'))
        options_theme = select_element_theme.options
        random_index_theme = random.randint(1, len(options_theme) - 1)
        select_element_theme.select_by_index(random_index_theme)
        
        name = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input.form-control"))
        )
        name.send_keys("Name")
        
        thesises = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea.form-control"))
        )
        
        thesises.send_keys("Thesises")
        
        
        
        upload_element = WebDriverWait(driver, 30).until(
             EC.visibility_of_element_located((By.CSS_SELECTOR, "div.secondary-block:nth-child(5) > input:nth-child(2)"))
        )    

        file_path = os.path.abspath(FILE_PATH)
        if not os.path.exists(file_path):
             pytest.fail(f"Файл не найден: {file_path}")

        upload_element.send_keys(file_path)
        
        
        upload_element1 = WebDriverWait(driver, 30).until(
             EC.visibility_of_element_located((By.CSS_SELECTOR, "div.secondary-block:nth-child(6) > input:nth-child(1)"))
        )    

        file_path1 = os.path.abspath(FILE_PATH)
        if not os.path.exists(file_path1):
             pytest.fail(f"Файл не найден: {file_path1}")

        upload_element1.send_keys(file_path1)
        
        upload_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.btn.btn-info[value='Добавить доклад']"))
        )

        driver.execute_script("arguments[0].scrollIntoView();", upload_button)
        time.sleep(4)

        upload_button.click()
        
    
        
        element_name = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(((By.XPATH, "//div[@class='mt-4 ntkCustTitle' and normalize-space(text())='Name']")))
        )
        
        element_thesis = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='mt-3 ntkCustContent' and normalize-space(text())='Thesises']"))
        )
        #Здесь проверка на авторов, можно добавить если будет выбираться не рандомно
        #element_author = WebDriverWait(driver, 20).until(
           # EC.presence_of_element_located((By.XPATH, "//div[@class='mt-4 ntkCustTitle' and contains(translate(., 'А.&nbsp;С.&nbsp;Абрамов', 'А С Абрамов'), 'А С Абрамов')]"))
       # )
        
        if element_name.text.strip() != "Name" or element_thesis.text.strip() != 'Thesises':
            pytest.fail("Элемент не соответствует ожидаемому тексту. name = ", element_name.text, " thesis = ", element_thesis.text)

        time.sleep(5)
        

        
    except Exception:
        pytest.fail("Авторизация прошла не успешно")
        
   
