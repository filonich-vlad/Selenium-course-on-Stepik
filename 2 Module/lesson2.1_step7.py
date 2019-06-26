from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

selectors = ["#treasure",
             "#answer",
             "#robotCheckbox",
             "#robotsRule",
             "[type=\"submit\"]",
             ]

names = ["treasure",
         "ans_field",
         "checkbox",
         "radiobutton",
         "submit_button",
         ]

elements = dict(zip(names, \
                    list(map(browser.find_element_by_css_selector, selectors))))

value = elements["treasure"].get_attribute("valuex")
elements["ans_field"].send_keys(calc(value))
elements["checkbox"].click()
elements["radiobutton"].click()
elements["submit_button"].click()
