# Иструкция по созданию файла ".env"
1. В папке с проектом создать файл ".env"
2. Заполнить его по следующему шаблону:
```bash
GITHUB_TOKEN=token
GITHUB_USERNAME=name
REPO_NAME=repo
```
Где token - ключ аккаунта (https://github.com/settings/tokens/new - ссылка на получение), name - имя аккаунта, repo - название тестового репозитория.
Можно использовать следующие пробные данные для теста:
```bash
GITHUB_TOKEN=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
GITHUB_USERNAME=dsafsdfsdfsdfas
REPO_NAME=test_repo_Effective_Mobile
```
# Инструкция по запуску
1. Скачать все файлы с репозитория и распоковать.
2. Установить Python версии 3.12 и выше. (Windows: https://www.python.org/ftp/python/3.12.6/python-3.12.6-amd64.exe ; MacOs: https://www.python.org/downloads/release/python-3126/)
3. Создать файл ".env" и заполнить по инструкции выше
4. Открыть терминал и перейти в папку с проектом. Далее команды, которые нужно прописывать
    1. pip install -r requirements.txt
    2. pytest .\test_api.py --no-header -v

Ожидаемый результат: После прохождения теста можно увидеть в терминале 100% прохождение теста. При наличии ошибки, будет выведена ошибка

<img src="https://i.imgur.com/QaYVuZo.png" width="300%">
