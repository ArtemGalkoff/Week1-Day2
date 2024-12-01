from itertools import combinations

class AnagramChecker:
    def __init__(self, word_list_file):
        # Загружаем файл со словами
        with open(word_list_file, 'r') as file:
            # Загружаем все слова в список, приводим их к нижнему регистру
            self.words = set(word.strip().lower() for word in file.readlines())  # Используем set для быстрого поиска

    def is_valid_word(self, word):
        # Проверка, является ли слово допустимым (есть ли оно в списке)
        return word.lower() in self.words

    def get_anagrams(self, word):
        word = word.lower()
        anagrams = self.find_composite_anagrams(word)
        return anagrams

    def find_composite_anagrams(self, word):
        # Преобразуем слово в список букв
        letters = list(word.lower())
        found_anagrams = set()

        # Проверяем все возможные разделения слова на части
        for i in range(1, len(letters)):
            for comb in combinations(letters, i):
                part1 = ''.join(comb)
                remaining_letters = letters.copy()
                for c in comb:
                    remaining_letters.remove(c)
                part2 = ''.join(remaining_letters)

                # Проверка, есть ли обе части в словаре
                if part1 in self.words and part2 in self.words:
                    found_anagrams.add(part1)
                    found_anagrams.add(part2)

        return list(found_anagrams)