from selene.support.shared import browser
import pytest


@pytest.fixture()
def configure_browser():
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://google.com'
    browser.config.timeout = 2
    browser.config.window_width = 1366
    browser.config.window_height = 768


@pytest.fixture()
def open_browser(configure_browser):
    browser.open('/ncr')