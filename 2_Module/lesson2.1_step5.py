from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)

selectors = ["#input_value",
             "#answer",
             "[for=\"robotCheckbox\"]",
             "#robotsRule",
             "[type=\"submit\"]",
             ]

selectors_to_items = list(map(browser.find_element_by_css_selector, selectors))

keys = ["number",
        "answer_field",
        "check_box",
        "radio_button",
        "submit_button",
        ]

items = dict(zip(keys, selectors_to_items))

items["answer_field"].send_keys(str(calc(float(items["number"].text))))

items["check_box"].click()
items["radio_button"].click()
items["submit_button"].click()





