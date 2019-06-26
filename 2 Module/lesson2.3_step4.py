from selenium import webdriver
from math import log, sin

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    browser.find_element_by_css_selector(".btn.btn-primary").click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element_by_css_selector("#input_value").text
    y = log(12*sin(int(x)))
    browser.find_element_by_css_selector("#answer").send_keys(str(y))
    browser.find_element_by_css_selector(".btn.btn-primary").click()
except Exception as e:
    print(e)
finally:
    input()
    browser.quit()
