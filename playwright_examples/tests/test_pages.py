from playwright_examples.pages.page_elements import PageElements
from playwright_examples.pages.page_main import PageMain

class TestPages:

    def test_main_page_is_loaded(self, page):
        main_page = PageMain(page)
        main_page.open()
        assert main_page.is_loaded()

    def test_elements_page_is_loaded(self, page):
        elements_page = PageElements(page)
        elements_page.open()
        assert elements_page.is_loaded()
