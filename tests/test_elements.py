from utils.driver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_elements():
    driver = get_driver()

    driver.get("https://the-internet.herokuapp.com/login")

    wait = WebDriverWait(driver, 10)

    # Wait for elements to be visible
    username = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "radius")))

    # Assertions (REAL TESTING)
    assert username.is_displayed()
    assert password.is_displayed()
    assert button.is_enabled()

    driver.quit()