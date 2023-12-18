import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import copy


# inherit TestCase Class and create a new test class
class DGC_init(unittest.TestCase):

    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Firefox()
        with open('./creds', 'r') as f:
            lines = f.readlines()
        self.driver.get(lines[0])
        self.driver.implicitly_wait(1000)
        email = self.driver.find_element(by=By.NAME, value="email")
        email.send_keys(lines[1])

        password = self.driver.find_element(by=By.NAME, value="password")
        password.send_keys(lines[2])

        kutchbhi = self.driver.find_element(by=By.CSS_SELECTOR, value = ".submit-btn button")
        kutchbhi.click()
        self.driver.implicitly_wait(1000)

    
    # Test case method. It should always start with test_
    def test_search_in_posts(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)
   
        print("Going to Posts")
        Posts = driver.find_element(By.CSS_SELECTOR, '.menu-item [title="Posts"]')
        Posts.click()

        
        initial_table = copy.copy(wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'table'))))
        for table in initial_table:
            post_title_row = table.find_elements(By.CSS_SELECTOR, '.post-title')
        all_content = []
        for post_title in post_title_row:
            all_content.append(post_title.find_elements(By.CSS_SELECTOR, '.font-14'))
        
        search_words = []
        for initial_content in all_content:
            for single_content in initial_content:
                content = copy.copy(str(single_content.text))
                for word in content.split():
                    search_words.append(word)

        Search = driver.find_element(by=By.CSS_SELECTOR, value='.nosubmit')
            
        for keyword in random.sample(search_words, 5):
            Search.clear()
            Search.send_keys(keyword.lower())
            time.sleep(5)
            buttons = driver.find_elements(By.TAG_NAME, 'button')
            for button in buttons:
                if button.text == 'SEARCH':
                    Search_button = button
            Search_button.click()
            time.sleep(5)

            results_table = driver.find_element(By.TAG_NAME, 'table')
            table_content = results_table.find_elements(By.CSS_SELECTOR, '.post-title')
            for single_content in table_content:
                only_title = single_content.find_element(By.CSS_SELECTOR, '.font-14')
                self.assertIn(keyword.lower(), str(only_title.text).lower())

    def tearDown(self):
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()
