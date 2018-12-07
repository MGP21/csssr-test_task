from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, time

chromepath = '/Users/mgp/WebDriver/chromedriver'

class newtest (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(chromepath)
        #self.driver.implicitly_wait(10)

    def test_tab(self):
        driver = self.driver
        driver.get("http://blog.csssr.ru/qa-engineer/")
        tab2_link = driver.find_element(By.LINK_TEXT, 'НАХОДИТЬ НЕСОВЕРШЕНСТВА')
        tab2_text = driver.find_element(By.XPATH, '/html/body/div[1]/section[2]/div[2]/article[2]/h4')
        #Проверяем что текст находится на странице до повторного клика.
        if tab2_text.text != "КАК ЭТО ДЕЛАЕТСЯ?":
            print ("element not found")
        tab2_link.click()
        # Повторный клик, чтобы содержимое вкладки исчезло.
        tab2_link.click()  # Если закомментироваить эту строку, тест проходит.
        time.sleep(2) #Задержка, чтобы текст успел исчезнуть.
        assert "КАК ЭТО ДЕЛАЕТСЯ?" in self.driver.find_element(By.XPATH, '/html/body/div[1]/section[2]/div[2]/article[2]/h4').text

    def tear_down(self):
        self.driver.quit()
