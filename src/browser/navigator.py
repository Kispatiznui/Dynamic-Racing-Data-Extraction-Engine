from selenium.webdriver.common.by import By
import time

def navigate_to_stats(driver, url):
    driver.get(url)

    time.sleep(5)

    stats_tab = driver.find_element(By.XPATH, "//a[contains(text(),'Stats')]")
    stats_tab.click()

    time.sleep(5)
