"""This document contains functional tests"""

# Imports

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

import time


class NewVisitorTest(unittest.TestCase):
    """
       This class defines a functional test for a NewVisitor
    """

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(1)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_tables(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_later(self):
        """
        Test if a to-do list can be created and then retrieved later.
        """

        # Go to apps homepage
        self.browser.get('http://localhost:8000')

        # Check page title is correct
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # User enters a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')

        # She types "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # Hits enter, page updates, now page lists "1: Buy peacock feathers"
        # as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_tables('1: Buy peacock feathers')

        # Input second item in the to-do list
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_tables('1: Buy peacock feathers')
        self.check_for_row_in_list_tables(
            '2: Use peacock feathers to make a fly')

        # There is still a texbox to enter another item. She enters "Use
        # peacock feathers to make a fly"
        self.fail('Finish the test')

        # The page updates again, now showing both items

        # Edith wonders whether the site will remember the list, site generates
        # a unique URL for the to-do list

        # She visits the URL, verifies that the to-do list is still There

        # Satisfied she goes back to sleep and closes the browser
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
