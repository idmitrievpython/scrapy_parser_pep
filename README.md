# Асинхронный парсер документов PEP

---
![python](https://img.shields.io/badge/Python-3.9.0-green)
![Scrapy](https://img.shields.io/badge/Scrapy-2.5.1-green)
---
## Contents:
- [Introduction](#introduction)
- [Parsing PEP documents](#parsing-pep-documents)
- [Instruction to start](#instruction-to-start)

---
### <anchor>Introduction</anchor>
Асинхронный парсер собирающий данные 
о Python Enhancement Proposals (PEP) с сайта `https://www.python.org/`.

----
### <anchor>Parsing PEP documents</anchor>
С каждой страницы PEP парсер собирает номер, название, статус и сохраняет
несколько файлов в формате `.csv` в папке `results/...`:
* Список PEP (номер, название и статус);
* Подсчитывает общее количество каждого статуса и сумму всех статусов.
----
### <anchor>Instruction to start</anchor>
<details>

1. Клонировать репозиторий:
`git clone https://github.com/idmitrievpython/scrapy_parser_pep.git`
2. Создать и активировать виртуальное окружение:
`python -m venv venv` or `python3 -m venv venv`,
then `source venv/Scripts/activate` or `source venv/bin/activate`
3. Установить зависимости из файла requirements.txt: `pip install -r requirements.txt`
4. Запуск парсера `scrapy crawl pep`

Автор: [idmitrievpython](https://github.com/idmitrievpython)
</details>