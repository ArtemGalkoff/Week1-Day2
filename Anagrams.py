import re
from Anagram_checker import AnagramChecker


def is_valid_input(user_input):
    # Проверка, что введено одно слово и оно состоит только из букв
    if len(user_input.split()) > 1:
        return False, "Ошибка: можно ввести только одно слово."

    if not user_input.isalpha():
        return False, "Ошибка: допустимы только буквы."

    return True, ""


def main():
    # Загружаем файл со словами и создаём экземпляр AnagramChecker
    word_list_file = "words.txt"  # Используем файл words.txt
    anagram_checker = AnagramChecker(word_list_file)

    while True:
        print("\nMenu:")
        print("1. Input word")
        print("2. Exit")
        choice = input("Chose variant: ")

        if choice == '1':
            user_input = input("Введите слово: ").strip()

            # Проверка правильности ввода
            is_valid, message = is_valid_input(user_input)

            if not is_valid:
                print(message)
                continue

            # Проверка, является ли слово допустимым и нахождение анаграмм
            if anagram_checker.is_valid_word(user_input):
                print(f"\nYour word: \"{user_input.upper()}\"")
                print("It is acceptable word.")
                anagrams = anagram_checker.get_anagrams(user_input)
                if anagrams:
                    print("Anagrams for you word:", ', '.join(anagrams))
                else:
                    print("Didn't find anagrams for your word.")

            else:
                print(f"\nВАШЕ СЛОВО: \"{user_input.upper()}\"")
                print("Not acceptable english word.")

        elif choice == '2':
            print("Exit.")
            break
        else:
            print("Chose correct variant.")


if __name__ == "__main__":
    main()