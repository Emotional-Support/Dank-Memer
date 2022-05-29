import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())


def get_zalgo(txt):

    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

    driver = webdriver.Chrome(
        executable_path=os.path.abspath("C:\\Users\\Pratham Sasha\\Downloads\\chromedriver.exe"), chrome_options=chrome_options
    )
    driver.get("https://lingojam.com/FancyTextGenerator")

    item = driver.find_element_by_id("english-text")
    item.click()

    search_field = driver.find_element_by_id("site-search")
    search_field.clear()
    search_field.send_keys(txt)


get_zalgo("yes")
