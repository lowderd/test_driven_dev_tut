"""This document contains functional tests"""

# Imports
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(LiveServerTestCase):
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
        self.browser.get(self.live_server_url)

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
        usr1_list_url = self.browser.current_url
        self.assertRegex(usr1_list_url, '/lists/.+')
        self.check_for_row_in_list_tables('1: Buy peacock feathers')

        # Input second item in the to-do list
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_tables('1: Buy peacock feathers')
        self.check_for_row_in_list_tables(
            '2: Use peacock feathers to make a fly')

        # Now a new user, usr2, comes along to the site

        # Use a new browser session to make sure no info has been cached
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Usr2 visits home-page, no sign of usr1's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('Use peacock feathers to make fly', page_text)

        # Usr2 starts making a new list
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Usr2 gets their own unique URL
        usr2_list_url = self.browser.current_url
        self.assertRegex(usr2_list_url, '/lists/.+')
        self.assertNotEqual(usr1_list_url, usr2_list_url)

        # Check again that usr1 list is not present
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('Use peacock feathers to make fly', page_text)
