from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

keys = ["Ivan",
        "Petrov",
        "i.p@ya.ru",
        ]

selectors = [".first_block > .first_class > input",
             ".first_block > .second_class > input",
             ".first_block > .third_class > input",
             ]

for key, selector in zip(keys, selectors):
    browser.find_element_by_css_selector(selector).send_keys(key)

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(1)

welcome_text_elt = browser.find_element_by_tag_name("h1")
welcome_text = welcome_text_elt.text

assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
