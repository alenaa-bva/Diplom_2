### Дипломный проект. Задание 2: API -тесты

## Описание

Этот проект содержит API тесты для сервиса Stellar Burgers с использованием библиотеки requests

## Стек технологий

- **Python** — основной язык для написания тестов.
- **Pytest** — фреймворк для организации тестов и их выполнения.
- **Allure-pytest** - библиотека для составления отчетов


## Установка

* Установить Allure-pytest

    ```
   pip install allure-pytest
   ```
* Установить Pytest

    ```
   pip install pytest
   ```
  
* Установить Pytest

    ```
   pip install requests
   ```
* Установка зависимостей:
    ```
    pip install -r requirements.txt
    ```


## Запуск тестов
  
* Команда для запуска всех тестов:
   ```
    pytest -v
   ```
  
## Запуск Allure

* Генерация отчета
   ```
    pytest --alluredir=allure_results
   ```