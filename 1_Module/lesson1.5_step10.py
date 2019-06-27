from selenium import webdriver
import time

#Поставить "...registration1.html" для первой страницы
link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
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

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
