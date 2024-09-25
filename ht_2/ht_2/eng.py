import nltk

def nltkSent(sentences):
    tokens = nltk.sent_tokenize(sentences)
    i = 1
    print("Предложения:")
    for item in tokens:
        print(f"{i}) {item}")
        i += 1

def nltkWord(sentence):
    tokens = nltk.word_tokenize(sentence)
    print("Результат результат разбиения:")
    print(' | '.join(tokens))

def readText():
    with open("input.txt", 'r') as inp:
        lines = inp.readlines()
    return ''.join(lines)

def main():
    print("Чтобы выбрать режим работы, выберете номер:\n1 - Получить разбиение текста\n2 - Получить разбиение предложения")
    flag = int(input("Введите номер: "))

    if flag == 1:
        sentences = readText()
        nltkSent(sentences)

    elif flag == 2:
        print("Введите предложение:")
        sentence = input()
        nltkWord(sentence)
    
    else:
        print("Неизвестная команда.")


if __name__ == "__main__":
    main()