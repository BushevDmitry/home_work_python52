import json
import os


# Модель
class TaskModel:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load()

    def add(self, text):
        if not text.strip():
            raise ValueError("Описание не может быть пустым!")
        self.tasks.append({'text': text, 'done': False})
        self.save()

    def delete(self, index):
        if 0 <= index < len(self.tasks):
            deleted = self.tasks.pop(index)
            self.save()
            return deleted

    def toggle(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['done'] = not self.tasks[index]['done']
            self.save()

    def save(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=2)

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []


# Представление
def show_menu():
    print("\n" + "=" * 40)
    print("1. Все задачи")
    print("2. Добавить")
    print("3. Удалить")
    print("4. Изменить статус")
    print("5. Выход")
    print("=" * 40)


def show_tasks(tasks):
    if not tasks:
        print("\n📭 Список пуст")
        return
    print("\n ЗАДАЧИ:")
    for i, t in enumerate(tasks, 1):
        status = "✅" if t['done'] else "❌"
        print(f"{i}. {status} {t['text']}")


# Контроллер
def main():
    model = TaskModel()

    while True:
        show_menu()
        choice = input("Выберите действие: ")

        if choice == '1':
            show_tasks(model.tasks)

        elif choice == '2':
            text = input("Описание задачи: ")
            try:
                model.add(text)
                print("✅ Добавлено!")
            except ValueError as e:
                print(f"❌ {e}")

        elif choice == '3':
            show_tasks(model.tasks)
            try:
                num = int(input("Номер задачи: ")) - 1
                deleted = model.delete(num)
                if deleted:
                    print(f"✅ Удалено: {deleted['text']}")
            except (ValueError, IndexError):
                print("❌ Неверный номер!")

        elif choice == '4':
            show_tasks(model.tasks)
            try:
                num = int(input("Номер задачи: ")) - 1
                model.toggle(num)
                print("✅ Статус изменен!")
            except (ValueError, IndexError):
                print("❌ Неверный номер!")

        elif choice == '5':
            print("До свидания!")
            break

        else:
            print("❌ Неверный выбор!")


if __name__ == "__main__":
    main()