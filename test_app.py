



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_add_employee():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")              # IMPORTANT
    options.add_argument("--disable-dev-shm-usage")   # IMPORTANT

    driver = webdriver.Chrome(options=options)

    driver.get("http://20.253.141.56:5000")

    driver.find_element(By.NAME, "name").send_keys("haritha")
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(2)

    assert "haritha" in driver.page_source

    driver.quit()
