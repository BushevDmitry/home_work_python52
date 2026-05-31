from selenium import webdriver
from math import *
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()



'''Задача 1'''

# browser.get("https://SunInJuly.github.io/execute_script.html")
# x = browser.find_element(By.ID, 'input_value').text
# x_int = int(x)
#
#
# def math_find(x_int):
#     return log(abs(12 * sin(x_int)))
#
# result = math_find(x_int)
#
#
# form_answer = browser.find_element(By.ID, 'answer')
# form_answer.send_keys(result)
#
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
# robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
# robot_checkbox.click()
#
# radiobuttom_robot_rules = browser.find_element(By.ID, 'robotsRule')
# radiobuttom_robot_rules.click()
#
#
# sumbit = browser.find_element(By.XPATH, '/html/body/div/form/button')
# sumbit.click()
# time.sleep(5)





'''Задача 2'''

# browser.get('http://suninjuly.github.io/file_input.html')
#
# place_holder_first_name = browser.find_element(By.XPATH, '/html/body/div/form/div/input[1]')
# place_holder_first_name.send_keys('Степан')
#
# place_holder_last_name = browser.find_element(By.XPATH, '/html/body/div/form/div/input[2]')
# place_holder_last_name.send_keys('Степанов')
#
# place_holder_email = browser.find_element(By.XPATH, '/html/body/div/form/div/input[3]')
# place_holder_email.send_keys('stepanov.stepan@mail.ru')
#
#
# with open('new_file.txt', 'w') as file:
#     file.write('Hello world')
#
# file_path = os.path.abspath("new_file.txt")
#
# chose_file = browser.find_element(By.ID, 'file')
# chose_file.send_keys(file_path)
#
# sumbit = browser.find_element(By.XPATH, '/html/body/div/form/button')
# sumbit.click()
# time.sleep(5)





'''Задача 3'''
# browser.get('http://suninjuly.github.io/alert_accept.html')
# buttom = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
# buttom.click()
#
# confirm = browser.switch_to.alert
# confirm.accept()
#
#
#
# x = browser.find_element(By.ID, 'input_value').text
# x_int = int(x)
#
# def math_find(x_int):
#     return log(abs(12 * sin(x_int)))
#
# result = math_find(x_int)
#
#
# form_answer = browser.find_element(By.ID, 'answer')
# form_answer.send_keys(result)
#
# sumbit = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
# sumbit.click()
#
# time.sleep(5)
#
# '''Ответ: 29.04240223259817'''