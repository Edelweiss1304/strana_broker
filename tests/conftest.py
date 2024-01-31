import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import testit
import os


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--headless=new')
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--no-sandbox')
    options.set_capability("pageLoadStrategy", "eager")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_exception_interact(node, call, report):
    if call.when == "call" and report.failed:
        driver = node.funcargs["driver"]
        screenshot_folder = "screens"
        os.makedirs(screenshot_folder, exist_ok=True)
        screenshot_path = os.path.join(screenshot_folder, f"screenshot_{report.nodeid.replace('/', '_')}.png")
        driver.save_screenshot(screenshot_path)
        testit.addAttachments(screenshot_path)
        print(f"Скриншот сохранен: {screenshot_path}")
