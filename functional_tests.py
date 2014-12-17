"""
	This document contains functional tests
"""

# Imports

from selenium import webdriver

# Start  browser
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title