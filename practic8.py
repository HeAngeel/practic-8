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

