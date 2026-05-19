from selenium.webdriver.common.by import By
from src.browser.waits import wait_for
from src.core.logger import get_logger

logger = get_logger()

def navigate_to_stats(driver, url):
    logger.info(f"Opening: {url}")

    driver.get(url)

    try:
        stats_tab = wait_for(
            driver,
            By.XPATH,
            "//a[contains(text(),'Stats')]"
        )

        stats_tab.click()

        logger.info("Stats tab opened")

    except Exception as e:
        logger.error(f"Navigation error: {e}")
