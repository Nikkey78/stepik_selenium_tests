import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_for_languages(browser):
    browser.get(link)
    time.sleep(30)
    browser.find_element_by_css_selector(".btn.btn-lg[type='submit']")
