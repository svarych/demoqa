from playwright.sync_api import Page


class PageElementsTextBox:
    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://demoqa.com/text_box'
        self.header_text_element = '.text-center'
        self.text_box_button = page.locator('//li[contains(@class, "btn")]/span[.="Text Box"]')
        self.user_form = page.locator('#userForm')
        self.full_name_field = page.locator('#userName')
        self.email_field = page.locator('#userEmail')
        self.current_address_field = page.locator('#currentAddress')
        self.permanent_address_field = page.locator('#permanentAddress')
        self.submit_button = page.locator('#submit')
        self.output_block = page.locator('#output')
        self.output_name = page.locator('p#name')
        self.output_email = page.locator('p#email')
        self.output_current_address = page.locator('p#currentAddress')
        self.output_permanent_address = page.locator('p#permanentAddress')


    def open(self) -> None:
        if not self.user_form.is_visible():
            self.text_box_button.click()

    def is_loaded(self) -> bool:
        header_text = self.page.locator(self.header_text_element).inner_text()
        return header_text == 'Text Box' and self.user_form.is_visible()

    def set_full_name(self, full_name: str) -> None:
        self.full_name_field.clear()
        self.full_name_field.fill(full_name)

    def set_email(self, email: str) -> None:
        self.email_field.clear()
        self.email_field.fill(email)

    def set_current_address(self, current_address: str) -> None:
        self.current_address_field.clear()
        self.current_address_field.fill(current_address)

    def set_permanent_address(self, permanent_address: str) -> None:
        self.permanent_address_field.clear()
        self.permanent_address_field.fill(permanent_address)

    def get_output_name(self) -> str:
        name = self.output_name.inner_text()
        return name.split(':')[1]

    def get_output_email(self) -> str:
        email = self.output_email.inner_text()
        return email.split(':')[1]

    def get_output_current_address(self) -> str:
        current_address = self.output_current_address.inner_text()
        return current_address.split(':')[1]

    def get_output_permanent_address(self) -> str:
        permanent_address = self.output_permanent_address.inner_text()
        return permanent_address.split(':')[1]

    def submit(self) -> None:
        self.submit_button.click()
