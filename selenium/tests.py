import os
import pathlib
import unittest

from selenium import webdriver

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()


driver = webdriver.Chrome(r"C:\Users\Tengo\Downloads\chromedriver.exe")


class WebpageTests(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, "Counter")


    def test_counter(self):
        p = driver.get(file_uri("counter.html"))
        increase = driver.find_element_by_id("increase")
        for i in range(20):
            increase.click()
            h = driver.find_element_by_tag_name("h1").text
            self.assertEqual(h, str(i+1))

if (__name__ == "__main__"):
    unittest.main()