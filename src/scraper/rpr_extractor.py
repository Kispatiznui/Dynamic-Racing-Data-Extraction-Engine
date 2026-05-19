from selenium.webdriver.common.by import By

def extract_rpr_data(driver, source_url):
    results = []

    # Espera simple (luego lo mejoramos con WebDriverWait)
    elements = driver.find_elements(By.XPATH, "//*[contains(text(),'RPR')]")

    for el in elements:
        try:
            text = el.text
            link = el.get_attribute("href")

            if text:
                results.append({
                    "source_url": source_url,
                    "text": text,
                    "link": link
                })
        except:
            continue

    return results
