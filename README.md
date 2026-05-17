1) Установи и проверь. Установи pytest командой pip install pytest. Создай файл test_first.py, напиши def test_one(): assert 1 + 1 == 2.
 Запусти pytest. 
Что значит зелёная точка и надпись 1 passed?

2) Сломай тест. Измени assert 1 + 1 == 2 на assert 1 + 1 == 3. Запусти pytest. Прочитай вывод — какую строку pytest подсветил и почему?

3) Два теста в одном файле. Добавь вторую функцию test_two, которая проверяет len("hello") == 5. Запусти pytest. Сколько точек в выводе и почему?

4) Именование файлов. Переименуй test_first.py в first.py. Запусти pytest. Нашёл ли он тесты? Почему pytest требует префикс test_?

5) Тестируй свою функцию. Создай calculator.py с функцией def add(a, b): return a + b.
 В test_calculator.py напиши from calculator import add и тест assert add(3, 4) == 7. Запусти — работает?

6) Установи coverage. Выполни pip install pytest-cov. Запусти pytest --cov=calculator. Что означают столбцы Stmts, Miss, Cover в таблице?

7) Непокрытый код. Добавь в calculator.py функцию def sub(a, b): return a - b, но тест для неё не пиши. Запусти pytest --cov=calculator.
 Почему Cover стал меньше 100%?

8) Добейся 100%. Напиши тест для sub. Запусти coverage заново. Стало ли Cover равно 100%? Что поменялось в столбце Miss?

9) HTML-отчёт. Запусти pytest --cov=calculator --cov-report=html. Открой файл htmlcov/index.html в браузере. Какие строки зелёные, какие красные?

10) Порог покрытия. Запусти pytest --cov=calculator --cov-fail-under=100. Удали один тест и запусти снова. Что произошло и зачем этот флаг нужен в проектах?