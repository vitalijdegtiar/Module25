# pytest -v --driver Chrome --driver-path chromedriver.exe  test_selenium_petfriends.py
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# фикстура авторизации
@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('/Users/vital/PycharmProjects/Pytest_first_test/tests/chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('madcat78@yandex.ru')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('12345')
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   yield

   pytest.driver.quit()


def test_petfriends(testing):

   # Активируем ожидание, пока на странице не появится заголовок "PetFriends"
   WebDriverWait(pytest.driver, 10).until(EC.title_contains("PetFriends"))

   pytest.driver.find_element_by_css_selector("html > body > nav > button > span").click()
   # Нажимаем на кнопку мои питомцы
   pytest.driver.find_element_by_css_selector('div#navbarNav > ul > li > a').click()
   # проверка что мы на страгнице пользователя

   assert pytest.driver.find_element_by_tag_name('h2').text == "Виталий"





def test_show_my_pets(testing):

   # Активируем ожидание, пока на странице не появится заголовок "PetFriends"
   WebDriverWait(pytest.driver, 10).until(EC.title_contains("PetFriends"))

   pytest.driver.find_element_by_css_selector("html > body > nav > button > span").click()
   # Нажимаем на кнопку мои питомцы
   pytest.driver.find_element_by_css_selector('div#navbarNav > ul > li > a').click()

      # вводим переменную количества питомцев на странице
   t = "Питомцев: 7"
   # Запрашиваем статистику пользователя, в которой содержится кол-во питомцев
   all_text = pytest.driver.find_element_by_xpath('//div[@class=".col-sm-4 left"]')

   # проверяем, что содержимое переменной t содержится в all_text

   assert t in all_text.text

   # проверка заголовка страницы на содержание текст «PetFriends»:
   assert 'PetFriends' in pytest.driver.title

def test_names_of_pets(testing):
   # активируем неявное ожидание
   pytest.driver.implicitly_wait(10)

   pytest.driver.find_element_by_css_selector("html > body > nav > button > span").click()
   # Нажимаем на кнопку мои питомцы
   pytest.driver.find_element_by_css_selector('div#navbarNav > ul > li > a').click()

   # находим имена питомцев
   names = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//td[1]')

   # проверяем заполнение имен
   for i in range(len(names)):
       assert names[i].text != ''

def test_different_names_of_pets(testing):
   # активируем неявное ожидание
   pytest.driver.implicitly_wait(10)

   pytest.driver.find_element_by_css_selector("html > body > nav > button > span").click()
   # Нажимаем на кнопку мои питомцы
   pytest.driver.find_element_by_css_selector('div#navbarNav > ul > li > a').click()

   # находим имена питомцев
   names = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//td[1]')
   # заводим переменную для имен
   names_text = []
   for i in range(len(names)):
       names_text.append(names[i].text)
   # заводим переменную для уникальных имен
   names_unique = []
   for n in names_text:
      if n not in names_unique: names_unique.append(n)
   # сравниваем два списка, если все имена уникальные- списки будут одинаковые
   assert names_text == names_unique



def test_photo_of_pets(testing):
   # активируем неявное ожидание
   pytest.driver.implicitly_wait(10)

   pytest.driver.find_element_by_css_selector("html > body > nav > button > span").click()
   # Нажимаем на кнопку мои питомцы
   pytest.driver.find_element_by_css_selector('div#navbarNav > ul > li > a').click()

   # находим имена питомцев
   names = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//td[1]')
   # находим фотографии питомцев
   images = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//th')
   # заводим переменную для подсчета фото
   photo = 0
   # проверяем наличие фото
   for i in range(len(names)):
       assert images[i].get_attribute('src') != ''
       # если фото есть добавляем в переменную
       if images[i].get_attribute('src') != '':
          photo+=1
   # проверяем что фото есть у как минимум половины питомцев
   assert len(names)/2 <= photo



def test_breed_of_pets(testing):
   # активируем неявное ожидание
   pytest.driver.implicitly_wait(10)

   pytest.driver.find_element_by_css_selector("html > body > nav > button > span").click()
   # Нажимаем на кнопку мои питомцы
   pytest.driver.find_element_by_css_selector('div#navbarNav > ul > li > a').click()

   # находим имена питомцев
   names = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//td[1]')

   # находим породу питомцев
   breed = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//td[2]')

   # проверяем наличие породы
   for i in range(len(names)):
       assert breed[i].text != ''

def test_age_of_pets(testing):
   # активируем неявное ожидание
   pytest.driver.implicitly_wait(10)

   pytest.driver.find_element_by_css_selector("html > body > nav > button > span").click()
   # Нажимаем на кнопку мои питомцы
   pytest.driver.find_element_by_css_selector('div#navbarNav > ul > li > a').click()

   # находим имена питомцев
   names = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//td[1]')
   # находим возраст питомцев
   age = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//td[3]')

   # проверяем наличие возраста
   for i in range(len(names)):
       assert age[i].text != ''
