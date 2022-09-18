import os
import unittest
from selenium import webdriver
#from selenium import webdriver

class EndToEndTests(unittest.TestCase):    
    
    def setUp(self):
        CURRENT_WORKING_DIRECTORY = os.getcwd()
        selenium_dirver_location_in_project = 'application/firefox/macos'
        selenium_driver_filename = 'geckodriver'
        
        print('Current Working Directory: ')
        print(CURRENT_WORKING_DIRECTORY)
        
        SELENIUM_DRIVER_LOCATION = os.path.join(
            CURRENT_WORKING_DIRECTORY,
            selenium_dirver_location_in_project,
            selenium_driver_filename
        )
        #SELENIUM_DRIVER_LOCATION = r'/Application/geckodriver'
        
        FLASK_LOCAL_PORT = 'http://localhost:5000'
        FLASK_STAGING_PORT = 'https://'
        FLASK_PRODUCTION_PORT = 'https://'
        
            
        _firefoxDriverName = 'geckodriver'  
        
        self.driver = webdriver.Firefox(executable_path = SELENIUM_DRIVER_LOCATION)
        self.driver.get(FLASK_LOCAL_PORT)
    
    def tearDown(self):
        self.driver.quit()
        
    def getElementByCssSelector(self,val):
        return self.driver.find_element(by='css selector', value=f'[data-test-end-to-end-id="{val}"]')
        
    def test_given_webpage_title__when_browser_startup__then_title_contains_webpage_title(self):
        app_name = 'Ento'
        self.assertIn(app_name, self.driver.title)

    def test__given_heading__when_browser_startup__then_heading_text_is_found(self):
        app_heading_text = 'Entity Finder'
        css_selector = 'app-heading'
        element_text = self.getElementByCssSelector(css_selector).text
        self.assertEqual(app_heading_text,element_text)
        

    #TODO pass executable path in a service object (use launch_browser.py as an example)
    # make sure to run the virtual environment
    # conda activate qimono-virtual
    # make sure that selnium is installed, or run 
    # pip install selenium
    # run tests with this command
    # python -m pytest
    