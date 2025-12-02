import pytest

@pytest.fixture(scope='session')
def page(chromium):
    page = chromium.new_page()
    yield page
