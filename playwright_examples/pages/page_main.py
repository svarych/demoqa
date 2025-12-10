from playwright.sync_api import Page


class PageMain:
    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://demoqa.com'
        self.home_banner = page.locator('.home-banner')
        self.elements = page.get_by_text('Elements')
        self.forms = page.get_by_text('Forms')
        self.alerts_frame_windows = page.get_by_text('Alerts, Frame & Windows')
        self.widgets = page.get_by_text('Widgets')
        self.interactions = page.get_by_text('Interactions')
        self.store = page.get_by_text('Store')

    def open(self) -> None:
        self.page.goto(self.url)

    def is_loaded(self) -> bool:
        return self.home_banner.is_visible()