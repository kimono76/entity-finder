import os
import unittest
from selenium import webdriver

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
        
    def test_appTitle__browser_startup__title_contains_appTitle(self):
        app_name = 'Ento'
        self.assertIn(app_name, self.driver.title)

    #TODO pass executable path in a service object (use launch_browser.py as an example)
    # run tests with this command
    # python -m pytest