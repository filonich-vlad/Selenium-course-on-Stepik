import unittest
from selenium import webdriver
import time

keys = ["Ivan",
        "Petrov",
        "i.p@ya.ru",
        ]

selectors = [".first_block > .first_class > input",
             ".first_block > .second_class > input",
             ".first_block > .third_class > input",
             ]

link_1 = "http://suninjuly.github.io/registration1.html"
link_2 = "http://suninjuly.github.io/registration2.html"

expected = "Поздравляем! Вы успешно зарегистировались!"

def reg(link):
    global keys
    global selectors
    browser = webdriver.Chrome()
    browser.get(link)
    for key, selector in zip(keys, selectors):
        browser.find_element_by_css_selector(selector).send_keys(key)

    browser.find_element_by_css_selector("button.btn").click()
    time.sleep(1)
    ans = browser.find_element_by_tag_name("h1").text
    browser.quit()
    return ans

class Test_registration(unittest.TestCase):
    
    def test_registration1(self):
        self.assertEqual(reg(link_1), expected,
                         "Registration failed.")


    def test_registration2(self):
        self.assertEqual(reg(link_2), expected,
                         "Registration failed.")

if __name__ == "__main__":
    unittest.main()
