from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)
browser = webdriver.Chrome(chrome_options=opt)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 15 секунд, пока текст не будет 10000 RUR
text = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
print(text)

button = browser.find_element_by_id("book")
button.click()

x = browser.find_element_by_id('input_value')
print(x.text)

y = str(calc(x.text))
print(y)

input1 = browser.find_element_by_id('answer')
input1.send_keys(y)

button = browser.find_element_by_css_selector("[type='submit']")
button.click()


