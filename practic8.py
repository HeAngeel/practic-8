# ---------- Студент 1: Обух В ----------
# Створення файлу та запис першого питання
def student1_create_file(filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Студент 1: Обух В\n")
            file.write("Питання: Що таке словники в Python?\n\n")
        print("Студент 1: файл створено успішно")
    except IOError as e:
        print("Помилка створення файлу:", e)


# ---------- Студент 2: Грибоєдова Марина ----------
# Додавання відповіді та нового питання

def student2_add_answer(filename):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write("Студент 2: Грибоєдова М\n")
            file.write("Відповідь:\n")
            file.write("Словники (dict) в Python — це структура даних,\n")
            file.write("яка зберігає пари ключ–значення.\n")
            file.write("Вони є змінюваними та зручними для роботи з даними.\n")
            file.write("Питання: Чим словники відрізняються від списків?\n\n")
        print("Студент 2: відповідь додано")
    except IOError as e:
        print("Помилка запису у файл:", e)
