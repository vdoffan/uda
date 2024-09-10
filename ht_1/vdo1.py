def isEmail(string):
    if string not in ["@", ""]:
        prohibited_begining = ".-_"

        if string[0] not in prohibited_begining\
            and string[string.find('@') + 1] not in prohibited_begining:

            if string.count('@') == 1 and string.find('@') >= 2:
                prohibited_symbols = "()<>,;:/\'\"\\[]"

                for symbol in string:
                    if symbol in prohibited_symbols: return False

                pattern = [".com", ".ru"]
                for ending in pattern:
                    if string[-len(ending):] == ending and\
                        string.find(ending) - string.find('@') >= 3: return True
    return False

def main():
    input_string = input()
    if isEmail(input_string):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()

# Чтобы строка могла считаться адресом электронной почты, имя пользователя,
# как и доменное имя, должно содержать не менее 2 символов, не начинаться на ".-_",
# а также не содержать символы "()<>,;:/'"\[]". Также в рассмотренном случае доменное
# имя должно заканчиваться на ".com" или ".ru", но этот список легко дополнить
# нужными окончаниями в случае необходимости.