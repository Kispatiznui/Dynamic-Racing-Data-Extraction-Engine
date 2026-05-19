from src.browser.login import login
from src.browser.navigator import navigate_to_stats
from src.scraper.rpr_extractor import extract_rpr_data
from src.export.excel_exporter import export_to_excel
from src.core.logger import get_logger

logger = get_logger()

def main():
    username = input("Username: ")
    password = input("Password: ")
    urls = input("URLs (comma separated): ").split(",")

    driver = login(username, password)

    all_data = []

    for url in urls:
        url = url.strip()

        navigate_to_stats(driver, url)

        data = extract_rpr_data(driver, url)
        all_data.extend(data)

    export_to_excel(all_data)

    logger.info("Export completed")

    driver.quit()

if __name__ == "__main__":
    main()
