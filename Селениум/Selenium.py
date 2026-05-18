from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select



driver = webdriver.Chrome()

'''Задача 1'''

# driver.get('https://www.example.com')
#
# element = driver.find_element(By.XPATH, '/html/body/div/h1')
# expected_word = "Example"
#
# if expected_word in element.text:
#     result = f"Заголовок '{element.text}' содержит слово '{expected_word}'"
# else:
#     result = f"Заголовок '{element.text}' НЕ содержит слово '{expected_word}'"
# print(result)





'''Задача 2'''

# driver.get('https://www.google.com')
#
# input_field = driver.find_element(By.XPATH, '/html/body/div[2]/div[6]/form/div[1]/div/div[1]/div[2]/div[2]/textarea')
# input_field.send_keys('Selenium Python')
#
# time.sleep(10) #Ссылки появились





'''Задача 3'''
#
# driver.get('https://the-internet.herokuapp.com/login')
#
# username_input = driver.find_element(By.ID, 'username')
# password_input = driver.find_element(By.ID, 'password')
# button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/button')
#
# username_input.send_keys('tomsmith')
# password_input.send_keys('SuperSecretPassword!')
# button.click()
# time.sleep(10) # Сообщение об успешной авторизации появилось





'''Задача 4'''
#
# driver.get('https://the-internet.herokuapp.com/checkboxes')
#
# checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
#
# for i, checkbox in enumerate(checkboxes, 1):
#     if not checkbox.is_selected():
#         print(f'Чекбокс {i} не отмечен, отмечаем')
#         checkbox.click()
#     else:
#         print(f'Чекбокс {i} уже отмечен')
#
# all_checked = True
# for index, checkbox in enumerate(checkboxes, start=1):
#     is_checked = checkbox.is_selected()
#     print(f"Чекбокс {index} отмечен: {is_checked}")
#     if not is_checked:
#         all_checked = False
#
# if all_checked:
#     print("Оба чекбокса отмечены.")
# else:
#     print("Не все чекбоксы отмечены.")
#
# time.sleep(5)





'''Задача 5'''
#
# driver.get('https://the-internet.herokuapp.com/dropdown')
#
# dropdown_element = driver.find_element(By.ID, 'dropdown')
#
# select_object = Select(dropdown_element)
#
# select_object.select_by_visible_text("Option 2")
# time.sleep(5)


