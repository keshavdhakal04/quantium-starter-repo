import pytest
from selenium.webdriver.chrome.options import Options

@pytest.hookimpl
def pytest_setup_options():
    options = Options()
    # Path to your Brave Browser
    options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    
    # Standard automation flags
    options.add_argument("--headless") 
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    # Cleans up the terminal logs
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    return options