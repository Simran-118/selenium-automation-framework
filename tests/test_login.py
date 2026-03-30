from utils.driver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_success():
    driver = get_driver()

    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CLASS_NAME, "radius").click()

    # Wait until redirected
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("secure"))

    # Assertion (IMPORTANT)
    assert "secure" in driver.current_url

    driver.quit()