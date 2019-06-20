import pytest
from selenium import webdriver
import time
import math

error_text = ''


@pytest.fixture(scope='function')
def browser():
    print("\n           start browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\n           quit browser..")
    browser.quit()


@pytest.mark.parametrize('link', [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'])
def test_find_text(browser, link):
    global error_text
    answer = str(math.log(int(time.time())))

    browser.get(link)

    browser.implicitly_wait(10)

    input1 = browser.find_element_by_tag_name('textarea')
    input1.send_keys(answer)
    button = browser.find_element_by_tag_name('button')
    button.click()

    browser.implicitly_wait(5)

    pre_text = browser.find_element_by_css_selector('div pre').text

    print(pre_text)

    error_text += pre_text

    assert pre_text == 'Correct!',  'error_text --------> {}'.format(pre_text)

    print(error_text)
