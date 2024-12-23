from razdel import sentenize
import nltk

# Определяет являентся ли слово русским
def is_russian_word(token):
    if not token:
        return False
    for char in token:
        if not (char.isalpha() and ('А' <= char <= 'я' or char in 'Ёё') or char in ['-', '/', '.']):
            return False
    return True

# Обработка предложения
def process_sentence(sentence):
    # Определенные знаки препинания для замены на пробелы
    punctuation_to_replace = [
        ',', '(', ')', '[', ']',
        '{', '}', ':', ';', '...',
        '!', '?', '\"', '«', '»'
        ]
    
    # Замена указанных знаков препинания на пробелы
    for punct in punctuation_to_replace:
        sentence = sentence.replace(punct, ' ')
    
    # Токенизация
    words = nltk.word_tokenize(sentence, language='russian')
    processed_words = []

    # Удаление лишних символов, оставшихся после токенизации
    for word in words:
        if word in ['-', '/', '.']:
            processed_words.append(' ')
        else:
            processed_words.append(word)

    # Возвращение токенов
    tokens = ' '.join(processed_words)
    return tokens.strip().split()

def main():

    input_file = 'Tolstoy2.txt'

    # Чтение текста из файла
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Разбиение текста на предложения с помощью Razdel
    sentences = [s.text.strip() for s in sentenize(text)]
    
    total_tokens = 0
    total_russian_words = 0
    total_letters = 0
    
    # Обработка предложений и их вывод в заданном формате
    for idx, sentence in enumerate(sentences):
        tokens = process_sentence(sentence)

        token_count = len(tokens)
        total_tokens += token_count
        
        # Проверка слов на пренадлежность русскому языку
        russian_words = []
        for token in tokens:
            if is_russian_word(token):
                letters_count = len(token)
                russian_words.append(letters_count)
                total_russian_words += 1
                total_letters += letters_count
        
        # Формирмирование строки с количеством букв в русских словах
        russian_words_info = ', '.join(str(count) for count in russian_words)
        
        print(f'Предложение {idx + 1}. {sentence} {token_count} токенов, {len(russian_words)} русских слов ({russian_words_info} букв)')
    
    # Вычисление среднего значения
    average_tokens_per_sentence = total_tokens / len(sentences) if sentences else 0
    average_word_length = total_letters / total_russian_words if total_russian_words else 0
    
    print(f'\nСреднее количество токенов в предложении: {average_tokens_per_sentence:.2f}.')
    print(f'Средняя длина русского слова в тексте: {average_word_length:.2f}.')

if __name__ == "__main__":
    main()
