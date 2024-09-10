import requests
from bs4 import BeautifulSoup

def getHTML(url):
    response = requests.get(url)
    if response.status_code == 200:
        page_content = response.content

        soup = BeautifulSoup(page_content, 'html.parser')

        html_content = soup.prettify()

        with open('parsed_page.html', 'w', encoding='utf-8') as file:
            file.write(html_content)
    else:
        print(f"Ошибка запроса: {response.status_code}")

def toText():
    with open('parsed_page.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    text = soup.get_text()
    lines = text.splitlines()
    non_empty_lines = [line.strip() for line in lines if line.strip()]

    cleaned_text = '\n'.join(non_empty_lines)

    with open('parsed_page.txt', 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

def search(name):
    with open('parsed_page.txt', 'r', encoding='utf-8') as file:
        strings = file.readlines()
    cnt = 0
    for item in strings:
        if item.find(name) != -1: cnt += 1
    return cnt

def main():
    url = input()
    name = input()
    getHTML(url)
    toText()
    ans = search(name.lower())
    print(ans)


if __name__ == "__main__":
    main()

# Данная программа осуществляет поиск совпаддений с учётом регистра. Поиск без учёта регистра можно осуществить путём
# изменения 38-й строки на "if item.lower().find(name) != -1: cnt += 1"