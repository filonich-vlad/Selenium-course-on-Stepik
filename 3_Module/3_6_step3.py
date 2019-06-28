import pytest
from selenium import webdriver
import time
import math

answer = math.log(int(time.time()))

links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1",
         ]

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', links)
def test_should_find_correct(browser, link):
    browser.get(link)
    browser.find_element_by_tag_name("textarea") \
                                .send_keys(str(math.log(int(time.time()))))
    browser.find_element_by_css_selector("button.submit-submission").click()
    ans = browser.find_element_by_css_selector("pre.smart-hints__hint").text
    assert ans == "Correct!", ans

    
