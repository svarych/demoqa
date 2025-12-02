from playwright_examples.pages.page_main import PageMainDemoQA


def test_simple(page):
    main_page = PageMainDemoQA(page)
    main_page.open()
    assert main_page.is_loaded()
