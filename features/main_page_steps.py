from pages.base_page import Page

class MainPage(Page):
    def open_main_page(self):
         self.open_url('https://www.target.com/')

@given('Open Target main page')
def open_main(context):
    context.main_page.open_main_page()
