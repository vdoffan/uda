import nltk

def nltkSent(sentences):
    print("nltk:")
    tokens = nltk.sent_tokenize(sentences)
    i = 1
    for item in tokens:
        print(f"{i}) {item}")
        i += 1

def nltkWord(sentence):
    print("nltk:")
    tokens = nltk.word_tokenize(sentence)
    print(' | '.join(tokens))

def readText():
    with open("input.txt") as inp:
        lines = inp.readlines()
    return ''.join(lines)

def main():
    print("Чтобы выбрать режим работы, выберете номер:\n1 - Получить разбиение текста\n2 - Получить разбиение предложения")
    flag = int(input("Введите номер: "))

    if flag == 1:
        sentences = readText()
        nltkSent(sentences)

    elif flag == 2:
        sentence = input()
        nltkWord(sentence)



if __name__ == "__main__":
    main()