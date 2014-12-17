"""This document contains functional tests"""

# Imports

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    """
       This class defines a functional test for a NewVisitor
    """

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_later(self):
        """
        Test if a to-do list can be created and then retrieved later.
        """

        # Go to apps homepage
        self.browser.get('http://localhost:8000')

        # Check page title is correct
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

        # User enters a to-do item straight away

        # She types "Buy peacock feathers" into a text box

        # Hits enter, page updates, now page lists "1: Buy peacock feathers"
        # as an item in a to-do list

        # There is still a texbox to enter another item. She enters "Use
        # peacock feathers to make a fly"

        # The page updates again, now showing both items

        # Edith wonders whether the site will remember the list, site generates
        # a unique URL for the to-do list

        # She visits the URL, verifies that the to-do list is still There

        # Satisfied she goes back to sleep and closes the browser
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
