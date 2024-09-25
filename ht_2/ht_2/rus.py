import nltk
import razdel

def nltkSent(sentences):
    print("Результат NLTK:")
    tokens = nltk.sent_tokenize(sentences)
    i = 1
    for item in tokens:
        print(f"{i}) {item}")
        i += 1

def natashaSent(sentences):
    print("Результат Natasha:")
    tokens = razdel.sentenize(sentences)
    j = 1
    for item in tokens:
        print(f"{j}) {item.text}")
        j += 1

def nltkWord(sentence):
    print("Результат NLTK:")
    tokens = nltk.word_tokenize(sentence)
    print(' | '.join(tokens))

def natashaWord(sentence):
    print("Результат Natasha:")
    tokens = razdel.tokenize(sentence)
    words = []
    for item in tokens:
        words.append(item.text)
    print(' | '.join(words))

def readText():
<<<<<<< HEAD
    with open("input.txt", encoding= 'utf-8') as inp:
=======
    with open("input.txt", 'r', encoding='utf-8') as inp:
>>>>>>> 5b03734b6c093a442da3ae2c68af350df8e366a7
        lines = inp.readlines()
    return ''.join(lines)

def main():
    print("Чтобы выбрать режим работы, выберете номер:\n1 - Получить разбиение текста\n2 - Получить разбиение предложения")
    flag = int(input("Введите номер: "))
    if flag == 1:
        sentences = readText()
        nltkSent(sentences)
        print()
        natashaSent(sentences)
    elif flag == 2:
        print("Введите предложение:")
        sentence = input()
        nltkWord(sentence)
        print()
        natashaWord(sentence)
    else:
        print("Неизвестная команда.")


if __name__ == "__main__":
    main()
