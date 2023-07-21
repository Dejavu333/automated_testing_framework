from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait


def setup(CHROME_PATH = ChromeDriverManager().install(), URL = "https://www.booking.com/"):
    driver = webdriver.Chrome(executable_path=CHROME_PATH)
    driver.get(URL)
    driver.maximize_window()
    return driver
    
