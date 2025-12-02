import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope='session')
def firefox():
    with sync_playwright() as play:
        browser = play.firefox.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope='session')
def chromium():
    with sync_playwright() as play:
        browser = play.chromium.launch(headless=False)
        yield browser
        browser.close()
