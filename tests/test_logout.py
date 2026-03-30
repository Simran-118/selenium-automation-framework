from utils.driver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logout():
    driver = get_driver()

    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CLASS_NAME, "radius").click()

    # Wait for logout button to appear
    wait = WebDriverWait(driver, 10)
    logout_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/logout']"))
    )

    logout_btn.click()

    # Wait until redirected to login page
    wait.until(EC.url_contains("login"))

    assert "login" in driver.current_url

    driver.quit()