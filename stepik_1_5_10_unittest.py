from selenium import webdriver
import time
import unittest


class TestRegistration(unittest.TestCase):
    def test_form1(self):

        link = "http://suninjuly.github.io/registration1.html"  # для правильной формы

        browser = webdriver.Chrome()
        browser.get(link)

        # Код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector('div.first_block input.first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('div.first_block input.second')
        input2.send_keys("Ivanov")
        input3 = browser.find_element_by_css_selector('div.first_block input.third')
        input3.send_keys("ivan@ya.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться и ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual('Поздравляем! Вы успешно зарегистировались!', welcome_text, 'fail test')

    def test_form2(self):
        link = "http://suninjuly.github.io/registration2.html"  # для НЕправильной формы

        browser = webdriver.Chrome()
        browser.get(link)

        # Код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector('div.first_block input.first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('div.first_block input.second')
        input2.send_keys("Ivanov")
        input3 = browser.find_element_by_css_selector('div.first_block input.third')
        input3.send_keys("ivan@ya.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться и ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual('Поздравляем! Вы успешно зарегистировались!', welcome_text, 'fail test')


if __name__ == '__main__':
    unittest.main()
