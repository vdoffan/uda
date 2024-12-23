## Подготовка к выполнению задания:

Ниже будут описаны подходы к выполнению задания в разных операционных системах.

**ВАЖНО:** Пожалуйста, ставьте python 3.10 (или 3.9). Предоставленное окружение не работает как минимум на python 3.13

------

#### Google Colaboratory (предпочтительный вариант):
- Откройте [Google Colaboratory](https://colab.research.google.com/)
- Загрузите этот Jupyter-ноутбук
- В левой панели выберите иконку папки
- "Загрузите в сессионное хранилище" файл utils.py
- Не забудьте скачать Jupyter-ноутбук после выполнения задания назад на свой компьютер

------
#### Conda

1) Установка Conda:
- Скачайте Miniconda с официального сайта: https://docs.conda.io/en/latest/miniconda.html
- Запустите установщик и следуйте инструкциям
- При установке отметьте "Add Miniconda3 to my PATH environment variable"
- Проверьте установку, открыв новое окно PowerShell:
```bash
conda --version
```
2) Создание conda-окружения:
# Перейдите в директорию с заданием
```bash
cd путь_к_директории_с_заданием
```

# Создание окружения с Python 3.10
```bash
conda create --name myenv python=3.10
```

# Активация окружения
```bash
conda activate myenv
```
3) Установка зависимостей и подключение среды к jupyter notebook:
# Установка jupyter и других пакетов через conda
```bash
conda install jupyter numpy pandas matplotlib
ipython kernel install --name my_env --user
```

# Если нужны пакеты из requirements.txt:
```bash
conda install --file requirements.txt
```

# Если какие-то пакеты недоступны через conda:
```bash
pip install -r requirements.txt
```
4) Проверка установки:
# Проверка версии Python
```bash
python --version
```

# Проверка установленных пакетов
```bash
conda list
```

5) Запуск Jupyter Notebook:

Через браузер:
```bash
jupyter notebook
```
Или через VSCode:
- Установите расширение Jupyter в VSCode
- Откройте .ipynb файл
- Выберите kernel из созданного conda-окружения

Дополнительные команды Conda:
```bash
# Просмотр списка окружений
conda env list

# Деактивация окружения
conda deactivate

# Удаление окружения
conda env remove --name myenv

# Обновление conda
conda update conda
```
Рекомендации:
- Если Conda не распознается в PowerShell, перезапустите PowerShell
- Используйте команду conda init powershell для настройки оболочки
- При проблемах с правами запустите PowerShell от имени администратора
- Предпочтительно использовать conda для установки пакетов вместо pip, когда это возможно
- Если используете pip внутри conda-окружения, устанавливайте пакеты после активации окружения

------

#### MacOS, Linux (установка через системный python + venv)
1. Проверка/установка Python:
    
```bash
# Проверка версии Python
python3 --version

# Если Python не установлен:
# MacOS:
brew install python@3.10
# Ubuntu/Debian:
sudo apt update
sudo apt install python3.10 python3-pip
```
    
2. Создание виртуального окружения:
    
```bash
# Перейдите в директорию с заданием
cd путь_к_директории_с_заданием

# Создание виртуального окружения
python3 -m venv venv

# Активация окружения
source venv/bin/activate
```
    
3. Установка зависимостей:
    
```bash
# Обновление pip
python3 -m pip install --upgrade pip

# Установка зависимостей
python3 -m pip install -r requirements.txt
```
    
4. Добавление Python в PATH (если требуется):
    
```bash
# Для bash
echo 'export PATH="/usr/local/bin/python3:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Для zsh
echo 'export PATH="/usr/local/bin/python3:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

Учтите, что изначально в вашей системе будет стоять и использоваться bash
    
5. Запуск Jupyter Notebook:
    
```bash
# Через браузер
python3 -m jupyter notebook
```

Или через VSCode:
- Установите расширение Jupyter в VSCode
- Откройте .ipynb файл
- Выберите kernel из созданного виртуального окружения

    
Дополнительные рекомендации:
- При возникновении проблем с правами доступа используйте sudo
- Убедитесь, что все пути корректно прописаны
- При проблемах с установкой пакетов попробуйте устанавливать их по одному
- Для MacOS на ARM-процессорах (и, возможно, MacOS в целом):
    - Необходимо установить `embeddingscode` для работы Gensim на ARM-процессорах
    - Отройте терминал, выполните команду `xcode-select --install`

------

#### Windows (установка через python + powershell)

1) Установка Python:
- Скачайте Python 3.10 с официального сайта
- При установке обязательно отметьте "Add Python to PATH"
- Проверьте установку:
    
```bash
python --version
```
    
2. Создание виртуального окружения:
    
```bash
# Перейдите в директорию с заданием
cd путь_к_директории_с_заданием

# Создание виртуального окружения
python -m venv venv

# Активация окружения
venv\Scripts\activate
```
    
3. Установка зависимостей:
    
```bash
# Обновление pip
python -m pip install --upgrade pip

# Установка зависимостей
python -m pip install -r requirements.txt
```
    
4. Добавление Python в PATH (если не сделано при установке):

- Откройте "Параметры системы"
- Перейдите в "Дополнительные параметры системы"
- Нажмите "Переменные среды"
- В разделе "Переменные среды пользователя" найдите PATH
- Добавьте путь к Python (обычно `C:\Users\YourUsername\AppData\Local\Programs\Python\Python310`)

5. Запуск Jupyter Notebook:
    
Через браузер
```bash
python -m jupyter notebook
```
    
Или через VSCode:
- Установите расширение Jupyter в VSCode
- Откройте .ipynb файл
- Выберите kernel из созданного виртуального окружения
    
Дополнительные рекомендации для Windows:
- Используйте PowerShell от имени администратора при возникновении проблем с правами
- При проблемах с `pip` используйте `python -m pip` вместо просто `pip`

------

