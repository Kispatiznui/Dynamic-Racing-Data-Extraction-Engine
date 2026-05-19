from selenium.webdriver.common.by import By
from src.browser.driver import create_driver
from src.browser.waits import wait_for
from src.core.logger import get_logger

logger = get_logger()

def login(username, password):
    driver = create_driver()

    logger.info("Opening RacingPost...")

    driver.get("https://www.racingpost.com")

    try:
        wait_for(driver, By.NAME, "username").send_keys(username)
        wait_for(driver, By.NAME, "password").send_keys(password)

        wait_for(driver, By.XPATH, "//button[contains(text(),'Log')]").click()

        logger.info("Login successful")

    except Exception as e:
        logger.error(f"Login failed: {e}")
        driver.quit()
        raise

    return driver
