from selenium import webdriver
import math as m

f = lambda x: m.log(abs(12*m.sin(int(x))))

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

selectors = ["#input_value",
             "#answer",
             "#robotCheckbox",
             "#robotsRule",
             ".btn.btn-default",
             ]

names = ["num",
         "ans_field",
         "checkbox",
         "radiobutton",
         "submit_button",
         ]

element_list = list(map(browser.find_element_by_css_selector, selectors))

elements = dict(zip(names, element_list))

elements["ans_field"].send_keys(str(f(elements["num"].text)))
elements["checkbox"].click()
browser.execute_script("window.scrollBy(0, 120);")
elements["radiobutton"].click()
elements["submit_button"].click()
