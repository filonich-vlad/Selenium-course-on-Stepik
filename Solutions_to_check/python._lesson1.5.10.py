from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)


input_name = browser.find_element_by_css_selector(".first_block .form-control.first")
input_name.send_keys("Жора")
input_family = browser.find_element_by_css_selector(".first_block .form-control.second")
input_family.send_keys("Жоров")
input_email = browser.find_element_by_css_selector(".first_block .form-control.third")
input_email.send_keys("jora@jora.com")
button = browser.find_element_by_css_selector("button.btn")
button.click()
time.sleep(3)
welcome_text_elt = browser.find_element_by_tag_name("h1")
welcome_text = welcome_text_elt.text
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
