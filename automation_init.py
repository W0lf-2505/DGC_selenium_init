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
   
        print("Testing search")
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

    def test_pagination_in_post(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)
   
        print("Testing Pagination")
        Posts = driver.find_element(By.CSS_SELECTOR, '.menu-item [title="Posts"]')
        Posts.click()

        selects = driver.find_elements(By.TAG_NAME, 'select')
        for select in selects:
            options = select.find_elements(By.TAG_NAME, 'option')
            for option in options:
                option.click()
                time.sleep(5)
                count = int(option.text)
                table = driver.find_element(By.TAG_NAME,'table')
                table_body = table.find_element(By.TAG_NAME,'tbody')
                table_row = table_body.find_elements(By.TAG_NAME,'tr')
                trcount = len(table_row)
                self.assertIn(str(count),str(trcount))

    def test_modified_created_sort_with_pagination(self):
        driver = self.driver
        wait = WebDriverWait(driver,5)

        print("Testing Modified and Created Sort for pagination issues")
        Posts = driver.find_element(By.CSS_SELECTOR, '.menu-item [title="Posts"]')
        Posts.click()

        buttons = driver.find_elements(By.CSS_SELECTOR, '.sort-icon')
        Modified_Sort = buttons[2]
        Created_Sort = buttons[3]

        selects = driver.find_elements(By.TAG_NAME, 'select')
        
        Modified_Sort.click()
        for select in selects:
            options = select.find_elements(By.TAG_NAME, 'option')
            for option in options:
                option.click()
                time.sleep(5)
                count = int(option.text)
                table = driver.find_element(By.TAG_NAME,'table')
                table_body = table.find_element(By.TAG_NAME,'tbody')
                table_row = table_body.find_elements(By.TAG_NAME,'tr')
                trcount = len(table_row)
                self.assertIn(str(count),str(trcount))
        time.sleep(10)
        Created_Sort.click()
        for select in selects:
            options = select.find_elements(By.TAG_NAME, 'option')
            for option in options:
                option.click()
                time.sleep(5)
                count = int(option.text)
                table = driver.find_element(By.TAG_NAME,'table')
                table_body = table.find_element(By.TAG_NAME,'tbody')
                table_row = table_body.find_elements(By.TAG_NAME,'tr')
                trcount = len(table_row)
                self.assertIn(str(count),str(trcount))
        

    def tearDown(self):
            self.driver.quit()

class DGC_national(unittest.TestCase):
    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Firefox()
        with open('./creds', 'r') as f:
            lines = f.readlines()
        self.driver.get(lines[0])
        self.driver.implicitly_wait(1000)
        email = self.driver.find_element(by=By.NAME, value="email")
        email.send_keys('national@example.com')

        password = self.driver.find_element(by=By.NAME, value="password")
        password.send_keys(lines[2])

        kutchbhi = self.driver.find_element(by=By.CSS_SELECTOR, value = ".submit-btn button")
        kutchbhi.click()
        self.driver.implicitly_wait(1000)

    # Test case method. It should always start with test_
    def test_nationaluser_postvisiblity_check(self):
        driver = self.driver
        wait = WebDriverWait(driver,5)

        print("Testing NationalUser access to all district posts")
        Posts = driver.find_element(By.CSS_SELECTOR, '.menu-item [title="Posts"]')
        Posts.click()

        selects = driver.find_elements(By.TAG_NAME, 'select')
        for select in selects:
            options = select.find_elements(By.TAG_NAME, 'option')
            options[-1].click()
        time.sleep(5)
        Owner_array = []
        initial_table = copy.copy(wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'table'))))
        table = initial_table[0]
        table_body = table.find_element(By.TAG_NAME,'tbody')
        table_rows = table_body.find_elements(By.TAG_NAME,'tr')
        for table_row in table_rows:
            Owner_array.append(table_row.find_elements(By.TAG_NAME,'td')[4])

        districts = []
        for owner in Owner_array:
            district = owner.find_element(By.CSS_SELECTOR,'.pipe')
            districts.append(district.text)

        districts = list(set(districts))
        if len(districts) == 1:
            count = len(districts)
            # Need to add page change to check if the page has only those posts
        count = len(districts)
        self.assertGreater(count,1)

        
    
    def tearDown(self):
            self.driver.quit()

    
if __name__ == '__main__':
    unittest.main()
