from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
fist_name = browser.find_element_by_css_selector(".first_block > .form-group.first_class > input.first")
fist_name.send_keys("Ivan")
last_name = browser.find_element_by_css_selector(".first_block > .form-group.second_class > input.second")
last_name.send_keys("Petrov")
email = browser.find_element_by_css_selector(".first_block > .form-group.third_class > input.third")
email.send_keys("aleshinalecsey@gmail.com")

# Отправляем заполненную форму
button = browser.find_element_by_xpath("//button[text()='Отправить']")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(5)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
