import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
from selenium.webdriver.support.ui import Select



class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/User/Documents/CACC/Module 5 - Automation/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_registration(self):
        self.driver.get("http://demo.automationtesting.in")
        self.driver.find_element_by_xpath("//img[@id='enterimg']").click()
        #First Name
        self.driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("May")
        #Last Name
        self.driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Nineth")
        #Address
        self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/textarea[1]").send_keys("Middle of Nowhere, American Samoa")
        self.driver.implicitly_wait(10)
        #email
        self.driver.find_element_by_xpath ("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/input[1]").send_keys("maya.bogatskaya@gmail.com")
        #phone
        self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/input[1]").send_keys("5034568963")
        #gender
        self.driver.find_element_by_xpath("//label[2]//input[1]").click()
        #hobbies
        self.driver.find_element_by_xpath("//input[@id='checkbox2']").click()
        #languages
        self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[7]/div[1]/multi-select[1]/div[1]").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'Arabic')]").click()
        #skills
        skills = self.driver.find_element_by_xpath("//select[@id='Skills']")
        drp = Select(skills)
        drp.select_by_visible_text("AutoCAD")
        #country
        country = self.driver.find_element_by_xpath("//select[@id='countries']")
        drp = Select(country)
        drp.select_by_visible_text("American Samoa")
        #DOB
        year = self.driver.find_element_by_xpath("//select[@id='yearbox']")
        drp = Select(year)
        drp.select_by_visible_text("1980")
        month = self.driver.find_element_by_xpath("//select[@placeholder='Month']")
        drp = Select(month)
        drp.select_by_visible_text("May")
        day = self.driver.find_element_by_xpath("//select[@id='daybox']")
        drp = Select(day)
        drp.select_by_visible_text("10")
        #password
        self.driver.find_element_by_xpath("//input[@id='firstpassword']").send_keys("Maya123456!")
        #password confirmation
        self.driver.find_element_by_xpath("//input[@id='secondpassword']").send_keys("Maya123456!")
        #submit
        self.driver.find_element_by_xpath("//button[@id='submitbtn']").click()
        time.sleep(5)
        #practice tab
        self.driver.find_element_by_xpath("//a[contains(text(),'Practice Site')]").click()
        time.sleep(10)
        #adding item to cart
        self.driver.execute_script("window.scrollBy(0,750)", "")
        time.sleep(5)
        self.driver.find_element_by_xpath("//h3[contains(text(),'Selenium Ruby')]").click()
        self.driver.find_element_by_xpath("//button[@class='single_add_to_cart_button button alt']").click()
        #view cart and checkout
        self.driver.find_element_by_xpath("//a[@class='button wc-forward']").click()
        self.driver.execute_script("window.scrollBy(0,750)", "")
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[@class='checkout-button button alt wc-forward']").click()



    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()




if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/User/PycharmProjects/Sel_Practice/venv/Lib/site-packages/HtmlTestRunner"),verbosity=2)
