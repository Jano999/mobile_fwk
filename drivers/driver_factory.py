from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.capabilities import get_caps

def create_driver():
    caps = get_caps()

    options = UiAutomator2Options().load_capabilities(caps)

    driver = webdriver.Remote(
        command_executor="http://localhost:4723",
        options=options
    )

    return driver