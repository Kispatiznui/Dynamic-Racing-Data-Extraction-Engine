from selenium import webdriver

def create_driver():
    options = webdriver.ChromeOptions()

    # Puedes activar esto luego para VPS
    # options.add_argument("--headless")

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    return driver
