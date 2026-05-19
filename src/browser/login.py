from selenium.webdriver.common.by import By
import time
from src.browser.driver import create_driver

def login(username, password):
    driver = create_driver()

    driver.get("https://www.racingpost.com")

    time.sleep(3)

    # NOTA: estos selectores probablemente se ajustan luego
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)

    driver.find_element(By.XPATH, "//button[contains(text(),'Log')]").click()

    time.sleep(5)

    return driver
