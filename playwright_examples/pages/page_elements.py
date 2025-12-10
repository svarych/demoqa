from playwright.sync_api import Page


class PageElements:
    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://demoqa.com/elements'
        self.group = '//div[.="{}"]//ancestor::div[@class="element-group"]'

    def open(self) -> None:
        if not self.page.url == self.url:
            self.page.goto(self.url)

    def is_loaded(self) -> bool:
        return self.page.is_visible(self.group.format('Elements'))

    def navigate_to_group(self, group_name: str) -> None:
        self.page.locator(self.group.format(group_name)).click()
