from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser

def ReadFromWebSite(WEBSITE='https://markmanson.net/best-articles'):
    #PATH = 'C:\Program Files (x86)\chromedriver.exe'
    #PATH = "./drivers/chromedriver"
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    #driver = webdriver.Chrome(PATH,options=option)
    driver = webdriver.Chrome(executable_path="/home/abanoub/Downloads/GpTextSummrizer/chromedriver", options=option)
    driver.get(WEBSITE)
    el = driver.find_element_by_tag_name('body')
    text2 = str(el.text)
    return text2