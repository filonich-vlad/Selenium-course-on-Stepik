from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
element = browser.find_element_by_xpath("//div/input[@placeholder='Введите имя']")
element.send_keys("Мое Имя")
element = browser.find_element_by_xpath("//div/input[@placeholder='Введите фамилию']")
element.send_keys("Моя Фамилия")
element = browser.find_element_by_xpath("//div/input[@placeholder='Введите Email']")
element.send_keys("Мой@е.маил")

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
assert "Поздравляем! Вы успешно зарегистрировались!" == welcome_text
