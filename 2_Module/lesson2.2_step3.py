from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

url = "http://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(url)


selectors = ["#num1",
             "#num2",
             "select.custom-select",
             ".btn.btn-default",
             ]

names = ["num1",
         "num2",
         "choiselist",
         "submit",
         ]

elements = dict(zip(names,\
                    list(map(browser.find_element_by_css_selector, selectors))))

num1 = int(elements["num1"].text)
num2 = int(elements["num2"].text)
ans = num1 + num2

select = Select(elements["choiselist"])
select.select_by_value(str(ans))

elements["submit"].click()

