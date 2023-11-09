# I am learning how to use Selenium for testing web applications

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

browserChrome = webdriver.Chrome()
basic_url = 'https://www.wikipedia.org'
english_url = 'https://en.wikipedia.org/wiki/Main_Page'


class TryoutTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def test_check_that_I_can_visit_Wikipedia(self):
        self.browser.get(basic_url)
        self.assertIn('Wikipedia', self.browser.title)

    def test_check_that_I_can_find_the_Platypus_page_on_the_English_wikipedia(self):
        print('Go to the English Wikipedia page')
        self.browser.get(english_url)
        print('Check that the page is in English')
        welkomsttekst = self.browser.find_element(By.CSS_SELECTOR, 'span.mw-headline')
        self.assertTrue(welkomsttekst.is_displayed())
        self.assertTrue('Welcome to Wikipedia' in welkomsttekst.text)
        print('Search for the Platypus')
        zoekveld = self.browser.find_element(By.CSS_SELECTOR, '#searchInput[aria-label="Search Wikipedia"]')
        self.assertTrue(zoekveld.is_displayed())
        zoekveld.send_keys('Platypus')
        zoekknop = self.browser.find_element(By.XPATH, "//button[text()='Search']")
        zoekknop.click()
        print('Check that the platypus page was found')
        titeltekst = self.browser.find_element(By.CSS_SELECTOR, 'h1.firstHeading > span')
        self.assertTrue(titeltekst.is_displayed())
        self.assertTrue('Platypus' in titeltekst.text)

    def test_check_what_a_failed_test_looks_like(self):
        print('Go to the English Wikipedia page')
        self.browser.get(english_url)
        print('Check that the page is in English')
        welkomsttekst = self.browser.find_element(By.CSS_SELECTOR, 'span.mh-headline')
        self.assertTrue(welkomsttekst.is_displayed())
        self.assertTrue('Welcome to Wikipedia' in welkomsttekst.text)
        print('Search for the Platypus')
        zoekveld = self.browser.find_element(By.CSS_SELECTOR, '#searchInput[aria-label="Search Wikipedia"]')
        self.assertTrue(zoekveld.is_displayed())
        zoekveld.send_keys('Platypus')
        zoekknop = self.browser.find_element(By.XPATH, "//button[text()='Search']")
        zoekknop.click()
        print('Check that the platypus page was found')
        titeltekst = self.browser.find_element(By.CSS_SELECTOR, 'h1.firstHeading > span')
        self.assertTrue(titeltekst.is_displayed())
        self.assertTrue('Platypus' in titeltekst.text)


if __name__ == '__main__':
    unittest.main()
