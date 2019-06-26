from selenium import webdriver
import os

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/file_input.html")

driver.find_element_by_css_selector("[name=\"firstname\"]").send_keys("Люк")
driver.find_element_by_css_selector("[name=\"lastname\"]").send_keys("Скайвокер")
driver.find_element_by_css_selector("[name=\"email\"]").send_keys("luk2002@mail.ru")
current_dir = os.path.abspath(os.path.dirname(__file__)) 
file_path = os.path.join(current_dir, 'Love.txt')
driver.find_element_by_css_selector("#file").send_keys(file_path)
driver.find_element_by_css_selector("[type=\"submit\"]").click()

input()
driver.quit()


