
import random
import os




def read_from_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        words = [line.strip() for line in file]
    return words


def write_to_file(file_path, words):
    with open(file_path, 'w', encoding="utf-8") as file:
        for word in words:
            file.write(word + '\n')


def translate_to_russian(word):
    if word in estonian_to_russian:
        return estonian_to_russian[word]
    else:
        print("Слово не найдено в словаре.")
        add_word = input("Хотите добавить его в словарь? (да/нет): ").strip().lower()
        if add_word == 'да':
            translation = input("Введите перевод слова на русский: ").strip()
            estonian_to_russian[word] = translation
            write_to_file("rus.txt", list(estonian_to_russian.keys()))
            write_to_file("est.txt", list(estonian_to_russian.values()))
            print("Слово успешно добавлено в словарь.")
            return translation
        else:
            return None


def translate_to_estonian(word):
    if word in russian_to_estonian:
        return russian_to_estonian[word]
    else:
        print("Слово не найдено в словаре.")
        add_word = input("Хотите добавить его в словарь? (да/нет): ").strip().lower()
        if add_word == 'да':
            translation = input("Введите перевод слова на эстонский: ").strip()
            russian_to_estonian[word] = translation
            write_to_file("est.txt", list(russian_to_estonian.keys()))
            write_to_file("rus.txt", list(russian_to_estonian.values()))
            print("Слово успешно добавлено в словарь.")
            return translation
        else:
            return None


def test_knowledge():
    total_words = len(russian_to_estonian)
    correct_answers = 0
    for russian_word, estonian_word in russian_to_estonian.items():
        print(f"Переведите слово '{russian_word}' на эстонский: ")
        answer = input("Ваш перевод: ").strip().lower()
        if answer == estonian_word.lower():
            print("Верно!")
            correct_answers += 1
        else:
            print("Неверно.")
    accuracy = (correct_answers / total_words) * 100
    print(f"Вы правильно перевели {correct_answers} из {total_words} слов. Точность: {accuracy}%")


russian_words = read_from_file("rus.txt")
estonian_words = read_from_file("est.txt")


russian_to_estonian = {}
estonian_to_russian = {}

for russian, estonian in zip(russian_words, estonian_words):
    russian_to_estonian[russian] = estonian
    estonian_to_russian[estonian] = russian

while True:
    print("\n1. Перевод с эстонского на русский")
    print("2. Перевод с русского на эстонский")
    print("3. Проверить знание слов из словаря")
    print("4. Выйти")
    choice = input("Выберите действие: ").strip()

    if choice == '1':
        estonian_word = input("Введите слово на эстонском: ").strip()
        translation = translate_to_russian(estonian_word)
        if translation:
            print(f"Перевод на русский: {translation}")
    elif choice == '2':
        russian_word = input("Введите слово на русском: ").strip()
        translation = translate_to_estonian(russian_word)
        if translation:
            print(f"Перевод на эстонский: {translation}")
    elif choice == '3':
        test_knowledge()
    elif choice == '4':
        print("До свидания!")
        break
    else:
        print("Неверный ввод. Попробуйте еще раз.")


