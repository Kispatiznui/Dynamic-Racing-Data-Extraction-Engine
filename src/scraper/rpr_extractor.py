from selenium.webdriver.common.by import By
from src.browser.waits import wait_for
from src.core.logger import get_logger

logger = get_logger()

def extract_rpr_data(driver, source_url):
    logger.info(f"Extracting RPR data from {source_url}")

    results = []

    try:
        # espera a que aparezca algo relacionado con RPR
        container = wait_for(
            driver,
            By.XPATH,
            "//*[contains(.,'RPR')]"
        )

        elements = container.find_elements(By.XPATH, ".//*")

        for el in elements:
            try:
                text = el.text.strip()
                link = el.get_attribute("href")

                if text:
                    results.append({
                        "source_url": source_url,
                        "text": text,
                        "link": link if link else ""
                    })

            except:
                continue

    except Exception as e:
        logger.error(f"Extraction error: {e}")

    return results
