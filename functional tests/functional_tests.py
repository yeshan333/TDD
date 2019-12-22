import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # 模拟输入
        inputbox.send_keys('Buy peacook feathers')
        inputbox.send_keys(Keys.ENTER)  # 回车

        # 检测是否成功提交
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacook feathers' for row in rows),
            "New to-do item did not appear in table"
        )
        # nice
        self.fail('Finished the test!')



if __name__ == "__main__":
    # unittest.main()
    unittest.main(warnings='ignore')