# Задача 1. Один-ко-многим: Автор и книги
Создай две таблицы: authors (id, name, country) и books (id, title, year, author_id).
 Настрой внешний ключ так, чтобы при удалении автора все его книги удалялись автоматически (CASCADE).

# Задача 2. Один-ко-многим: Категории товаров
Создай таблицы categories (id, name) и products (id, name, price, category_id).
 При удалении категории category_id у товаров должен становиться NULL (SET NULL).

# Задача 3. Один-к-одному: Пользователь и профиль
Создай таблицы users (id, email, password) и user_profiles (user_id, full_name, bio, avatar_url). 
Сделай так, чтобы у каждого пользователя был только один профиль (UNIQUE на user_id + FK).

# Задача 4. Многие-ко-многим: Студенты и курсы
Создай таблицы students (id, name), courses (id, title) и промежуточную таблицу enrollments (student_id, course_id, enrolled_at). 
Составной первичный ключ из двух FK.

# Задача 5. Самоссылающаяся связь: Сотрудники и руководители
Создай таблицу employees (id, name, position, manager_id), где manager_id ссылается на id той же таблицы.
 Учти, что у генерального директора manager_id будет NULL.