from collections import Counter
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt
import random

def getText():
    with open("t0.txt", 'r', encoding='utf-8') as file:
        text = file.readlines()

    # Замена 'ё' на 'е' и приведение к нижнему регистру
    text = ('\n').join(text)
    text = text.lower().replace('ё', 'е')

    return text

# Функция для определения алфавита буквы
def getAlphabet(letter):
    if 'а' <= letter <= 'я':
        return 'русская'
    elif 'a' <= letter <= 'z':
        return 'латинская'
    else:
        return 'другая'

# Функция для визуализации частоты букв
def visualizer(counter):
    # Получаем буквы и их количества, отсортированные по убыванию
    letters, counts = zip(*counter.most_common())
    # Создаем список цветов (в данном случае случайных цветов)
    colors = [f'#{random.randint(0, 0xFFFFFF):06x}' for _ in range(len(letters))]

    plt.figure(figsize=(12, 6))
    bars = plt.bar(letters, counts, color=colors)
    
    plt.xlabel('Буквы')
    plt.ylabel('Количество')
    plt.title('Частота букв в тексте')
    plt.xticks(rotation=45)
    
    # Добавляем количество над каждым столбцом
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, str(height), ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()

def main():
    text = getText()

    # Создаем токенайзер, который извлекает только русские и латинские буквы
    pattern = r'[a-zа-я]'
    tokenizer = RegexpTokenizer(pattern)

    # Токенизация текста
    letters = tokenizer.tokenize(text)

    # Общее количество букв
    total_letters = len(letters)

    # Подсчет частоты каждой буквы
    counter = Counter(letters)

    # Сортировка букв по убыванию частоты
    sorted_letters = counter.most_common()


    # Вывод результатов
    print(f'Всего: {total_letters} букв;\n')

    for idx, (letter, count) in enumerate(sorted_letters, 1):
        relative_freq = count / total_letters
        alphabet = getAlphabet(letter)
        print(f'{idx}. {letter} – {count} | {relative_freq:.4f} | {alphabet}')

    visualizer(counter)


if __name__ == '__main__':
    main()