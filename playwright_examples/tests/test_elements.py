from playwright_examples.pages.page_elements import PageElements
from playwright_examples.pages.page_elements_text_box import PageElementsTextBox
from faker import Faker

class TestElements:

    def test_test_box_is_open(self, page):
        elements_page = PageElements(page)
        elements_page.open()
        text_box_page = PageElementsTextBox(page)
        text_box_page.open()
        assert text_box_page.is_loaded()

    def test_full_name(self, page_text_box):
        name = Faker().name()
        page_text_box.set_full_name(name)
        page_text_box.submit()
        assert page_text_box.get_output_name() == name

    def test_email_address(self, page_text_box):
        email_address = Faker().email()
        page_text_box.set_email(email_address)
        page_text_box.submit()
        assert page_text_box.get_output_email() == email_address

    def test_current_address(self, page_text_box):
        current_address = Faker().address().split('\n')[0]
        page_text_box.set_current_address(current_address)
        page_text_box.submit()
        assert page_text_box.get_output_current_address() == current_address

    def test_permanent_address(self, page_text_box):
        permanent_address = Faker().address().split('\n')[0]
        page_text_box.set_permanent_address(permanent_address)
        page_text_box.submit()
        assert page_text_box.get_output_permanent_address() == permanent_address
