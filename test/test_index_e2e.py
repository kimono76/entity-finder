import unittest
from selenium import webdriver

class EndToEndTests(unittest.TestCase):    
    
    def setUp(self):
        SELENIUM_DRIVER_LOCATION = r'/Application/geckodriver'
        
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