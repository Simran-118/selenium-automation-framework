from utils.driver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_navigation():
    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    # Step 1: Open homepage
    driver.get("https://the-internet.herokuapp.com")

    # Step 2: Click link
    link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Form Authentication"))
    )
    link.click()

    # Step 3: Verify navigation forward
    wait.until(EC.url_contains("login"))
    assert "login" in driver.current_url

    # Step 4: Navigate back
    driver.back()

    # Step 5: Wait for homepage to load
    wait.until(EC.url_contains("herokuapp"))

    # Step 6: Verify back navigation
    assert "herokuapp" in driver.current_url

    driver.quit()