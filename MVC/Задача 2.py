# Простая библиотечная система

# Модель (данные)
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True  # True - есть, False - выдана

    def __str__(self):
        status = "Доступна" if self.is_available else "Выдана"
        return f'"{self.title}" , {self.author} , {self.year} : {status}'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_books(self, search_term):
        found = []
        for book in self.books:
            if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower():
                found.append(book)
        return found

    def get_all_books(self):
        return self.books

    def get_available_books(self):
        available = []
        for book in self.books:
            if book.is_available:
                available.append(book)
        return available


# Контроллер
class LibraryController:
    def __init__(self):
        self.library = Library()

    def add_book(self, title, author, year):
        try:
            year = int(year)
            book = Book(title, author, year)
            self.library.add_book(book)
            print(f'Книга "{title}" добавлена')
        except:
            print("Ошибка: год должен быть числом")

    def search_books(self, search_term):
        if not search_term.strip():
            print("Введите поисковый запрос")
            return
        found = self.library.find_books(search_term)
        self.show_books(found, f'Результаты поиска: "{search_term}"')

    def issue_book(self, title):
        for book in self.library.books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.is_available = False
                    print(f'Книга "{title}" выдана')
                else:
                    print(f'Книга "{title}" уже выдана')
                return
        print(f'Книга "{title}" не найдена')

    def return_book(self, title):
        for book in self.library.books:
            if book.title.lower() == title.lower():
                if not book.is_available:
                    book.is_available = True
                    print(f'Книга "{title}" возвращена')
                else:
                    print(f'Книга "{title}" уже в библиотеке')
                return
        print(f'Книга "{title}" не найдена')

    def show_all_books(self):
        self.show_books(self.library.get_all_books(), "Все книги")

    def show_available_books(self):
        self.show_books(self.library.get_available_books(), "Доступные книги")

    def show_books(self, books, title):
        if not books:
            print("Книг не найдено")
            return
        print(f"{title} ({len(books)} книг)")
        for i, book in enumerate(books, 1):
            print(f"{i}. {book}")


# Сама программа
def main():
    app = LibraryController()

    # Добавляем примеры книг
    app.add_book("Война и мир", "Лев Толстой", 1869)
    app.add_book("Преступление и наказание", "Фёдор Достоевский", 1866)
    app.add_book("Мастер и Маргарита", "Михаил Булгаков", 1967)
    app.add_book("1984", "Джордж Оруэлл", 1949)

    while True:
        print("БИБЛИОТЕКА")
        print("1. Добавить книгу")
        print("2. Найти книгу")
        print("3. Выдать книгу")
        print("4. Вернуть книгу")
        print("5. Все книги")
        print("6. Доступные книги")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "0":
            print("До свидания!")
            break
        elif choice == "1":
            title = input("Название: ")
            author = input("Автор: ")
            year = input("Год: ")
            app.add_book(title, author, year)
        elif choice == "2":
            query = input("Введите название или автора: ")
            app.search_books(query)
        elif choice == "3":
            title = input("Название книги: ")
            app.issue_book(title)
        elif choice == "4":
            title = input("Название книги: ")
            app.return_book(title)
        elif choice == "5":
            app.show_all_books()
        elif choice == "6":
            app.show_available_books()
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()