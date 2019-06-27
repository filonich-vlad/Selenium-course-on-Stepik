from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
    
    browser.find_element_by_css_selector("#book").click()
    browser.execute_script("window.scrollBy(0, 200)")
    x = browser.find_element_by_css_selector("#input_value").text
    y = log(abs(12*sin(int(x))))
    browser.find_element_by_css_selector("#answer").send_keys(str(y))
    browser.find_element_by_css_selector("[type=\"submit\"]").click()
finally:
    input()
    browser.quit()
