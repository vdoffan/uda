# Текст для анализа
text = "Перепёлка поёт."
text = text.replace('ё', 'е').lower()

# Определение списков букв русского и латинского алфавитов
russian_letters = [chr(i) for i in range(ord('а'), ord('я')+1)]
latin_letters = [chr(i) for i in range(ord('a'), ord('z')+1)]

# Подсчет количества каждой буквы
from collections import Counter

letters = [char for char in text if char in russian_letters or char in latin_letters]
total_letters = len(letters)
letter_counts = Counter(letters)

# Сортировка букв по убыванию частоты
sorted_letters = letter_counts.most_common()

# Подготовка вывода
results = []
for i, (letter, count) in enumerate(sorted_letters, 1):
    frequency = count / total_letters
    if letter in russian_letters:
        alphabet = 'русская'
    else:
        alphabet = 'латинская'
    results.append(f"{i}. {letter} – {count} | {frequency:.4f} | {alphabet} {'*' * count}")

# Выводим результат
output_text = f"Всего: {total_letters} букв;\n\n" + "\n".join(results)
print(output_text)
