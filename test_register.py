import time
from pyparsing import pythonStyleComment
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def setup():
    driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.get('https://www.cermati.com/app/gabung')
    yield driver
    driver.quit()

def test_register(setup):
    time.sleep(3)
    setup.find_element(By.XPATH, '//*[@id="email"]').send_keys('diarardiansyah212@gmail.com')
    time.sleep(3)
    setup.find_element(By.XPATH, '//*[@id="mobilePhone"]').send_keys('62812881929')
    setup.find_element(By.XPATH, '//*[@id="password"]').send_keys('Diaraja123')
    setup.find_element(By.XPATH, '//*//*[@id="confirmPassword"]').send_keys('Diaraja123')
    setup.find_element(By.XPATH, '//*[@id="firstName"]').send_keys('Diar')
    setup.find_element(By.XPATH, '//*[@id="lastName"]').send_keys('Ardiansyah')
    time.sleep(3)
    setup.find_element(By.XPATH, '//*[@id="cityAndProvince"]').send_keys('KOTA DEPOK')
    time.sleep(3)
    setup.find_element(By.XPATH, '//*[@class="autocomplete__icon-right_hrISI"]').click()
    time.sleep(3)
    setup.find_element(By.XPATH, '//*[@class="btn_SGZcZ btn-track btn--action_kallT RegistrationForm_form-container__button__UolrR"]').click()

    title = setup.title
    assert "Cermati: Pinjaman, Kartu Kredit, Asuransi & Tabungan Online Terbaik" in title

    