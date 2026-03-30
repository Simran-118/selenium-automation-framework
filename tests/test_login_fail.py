from utils.driver_setup import get_driver
from selenium.webdriver.common.by import By
import time

def test_login_fail():
    driver = get_driver()

    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.CLASS_NAME, "radius").click()

    time.sleep(2)

    error = driver.find_element(By.ID, "flash").text

    assert "invalid" in error.lower()

    driver.quit()