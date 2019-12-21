import unittest

from selenium import webdriver

# nice pratice
"""
browser = webdriver.Firefox()

# django-admin startproject superlists
# python .\manage.py runserver
try:
    browser.get('http://127.0.0.1:8000/')
    assert 'To-Do' in browser.title, "Browser title was " + browser.title
finally:
    browser.quit()
"""

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)  # if need, wait three seconds（wait for page loading）

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_after(self):
        self.browser.get('http://127.0.0.1:8000/')

        # 标题测试
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finished the test!')

        # 输入一个待办事项

if __name__ == "__main__":
    # unittest.main()
    unittest.main(warnings='ignore')