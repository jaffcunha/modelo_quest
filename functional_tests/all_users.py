# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_it_worked(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)

if __name__ == '__main__':
    unittest.main(warnings='ignore')

# It imports selenium and unittest, a Python library for testing

# It creates a TestCase class, named NewVisitorTest, with:
#   -A setUp method that initializes the test. It opens the browser and it waits for 3 seconds if needs to (if the page is not loaded).
#   -A tearDown method that runs after each test. It closes the browser.
#   -A method that starts with test and that asserts that the title of the webpage has "Welcome to Django" in it.

# The setUp and tearDown methods run at the beginning and at the end of each test method (the ones that start with the word test).

# The final lines mean that only if Python runs the file directly (not imported) it will execute the function unittest.main(). This function launches the unittest Test runner, that identifies the different tests defined by looking for methods that start with test.

# We call the unittest.main() function with the optional parameter warnings=’ignore’ to avoid a ResourceWarning message.
