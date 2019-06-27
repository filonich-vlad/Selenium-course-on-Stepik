from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля

# Ожидание прогрузки страницы
time.sleep(3)

# Заполняем поле имени
first_name_input = browser.find_element_by_css_selector(".first_block .first")
first_name_input.send_keys("FirstName")

# Заполняем поле фамилии
last_name_input = browser.find_element_by_css_selector(".first_block .second")
last_name_input.send_keys("LastName")

# Заполняем поле почты
email_input = browser.find_element_by_css_selector(".first_block .third")
email_input.send_keys("e-mail")

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
