import pytest

from playwright_examples.pages.page_elements import PageElements
from playwright_examples.pages.page_elements_text_box import PageElementsTextBox


@pytest.fixture(scope='session')
def page(chromium):
    page = chromium.new_page()
    yield page

@pytest.fixture(scope='class')
def page_elements(page):
    page_e = PageElements(page)
    page_e.open()
    yield page_e

@pytest.fixture(scope='class')
def page_text_box(page, page_elements):
    page_tb = PageElementsTextBox(page)
    page_tb.open()
    yield page_tb
