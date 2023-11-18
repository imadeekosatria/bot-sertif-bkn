from selenium import webdriver
# from undetected_chromedriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas
import time
import random


# path = "chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--use_subprocess")
# chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# chrome_options = ChromeOptions.add_argument("--no-sandbox")

browser = webdriver.Chrome(options=chrome_options)
browser.get("https://sertificat.bkn.go.id/")

df =  pandas.read_excel("BIN NTB Excel.xlsx")
for i in df.index:
    nik = str(df['NO REGISTER'][i])[::-1]
    np = str(df['NO PESERTA'][i])

    browser.implicitly_wait(10)
    nik_form = browser.find_element(By.NAME, "nik")
    nik_form.clear()
    nik_form.send_keys(nik[:-1])

    time.sleep(random.randint(5, 10))
    # time.sleep(5)
    noreg_form = browser.find_element(By.NAME, 'np')
    noreg_form.clear()
    noreg_form.send_keys(np)
    # time.sleep(5)
    time.sleep(random.randint(5, 10))

    select = Select(browser.find_element(By.NAME, 'tipe'))
    select.select_by_value("1")
    time.sleep(random.randint(5, 10))
    browser.find_element(By.CLASS_NAME, 'uk-button-primary').click()
    time.sleep(8)

browser.close()