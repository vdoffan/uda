def main():
    with open("test_rus.txt", 'r') as file:
        cnt = 1
        last, cur = 0, 0
        for string in file:
            ending_symbols = ".?!"
            for i in range(0, len(string)):
                if string[i] in ending_symbols:
                    if i + 2 > len(string) or string[i + 2].isupper():
                        cur = i + 1
                        print(f"{cnt}. {string[last:cur]}")
                        last = cur + 1
                        cnt += 1
            print(f"{cnt}. {string[last:len(string)]}")

if __name__ == "__main__":
    main()

# Данная программа неправильно делит текст с диалогами. Например отрывок
# "Весна, и любовь, и счастие! — как будто говорил этот дуб. — И как не надоест вам все один и тот же глупый бессмысленный обман!"
# будет распознан как одно предложение.