from selenium import webdriver

def create_driver():
    options = webdriver.ChromeOptions()

    # VPS option (activar cuando lo uses en servidor)
    # options.add_argument("--headless")

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    return driver
