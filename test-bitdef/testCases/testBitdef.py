import unittest
import HtmlTestRunner
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys





class LoginTest(unittest.TestCase):
    baseURL = "https://test-bitdef.web.app"
    driver = webdriver.Chrome(executable_path = "..\drivers\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        

    def test_createReport(self):
        wait = WebDriverWait(self.driver, 15)   

        #Assert Title Page
        assert self.driver.title == "TestFrontend"
       
        #Create Report
        wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()=' CREATE REPORT ']"))).click()

        #Details
        detailsType = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder = 'Select type']")))
        detailsType.send_keys(Keys.ENTER,Keys.ARROW_DOWN,Keys.ENTER)
        detailsCompany = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder = 'Select Company']")))
        detailsCompany.send_keys(Keys.ENTER,Keys.ARROW_DOWN,Keys.ENTER)
        wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder = 'Enter name']"))).send_keys("Bogdan Eugen")

        #Settings
        wait.until(EC.presence_of_element_located((By.XPATH,"//label[@for = 'mat-radio-2-input']//span[@class='mat-radio-container']"))).click()
        settingsReccurance = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder = 'Select reccurence']")))
        settingsReccurance.send_keys(Keys.ENTER,Keys.ARROW_DOWN,Keys.ENTER)
        settingsOn = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder = 'Select day']")))
        settingsOn.send_keys(Keys.ENTER,Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ENTER)
        settingInterval = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder = 'Select interval']")))
        settingInterval.send_keys(Keys.ENTER,Keys.ARROW_DOWN,Keys.ENTER)
        wait.until(EC.presence_of_element_located((By.XPATH,"//label[@for = 'mat-checkbox-1-input']"))).click()
        wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()=' SAVE ']"))).click()

        #Assert Raport SAVE
        time.sleep(1)
        successSave = self.driver.find_element_by_xpath("//div[text()=' Successfully saved the report ']").text
        self.assertEqual("Successfully saved the report", successSave)

        #Sleep to see ending
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__== "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\reports'))
