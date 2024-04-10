# API обмена валют
Проект на FastAPI, который служит простым приложением для обмена валюты.
Пользователи могут получать последние курсы обмена различных валют и выполнять конвертацию валют.
Проект включает аутентификацию JWT для доступа пользователей и интеграцию с открытым API обменных курсов для получения данных об обменных курсах в режиме реального времени.

### Используемые технологии: 
* Python
* FastAPI
* Pydantic
* JWT
* Pytest

### Запуск проекта
1. Клонируйте проект с помощью команды: <br>
git clone https://github.com/mike-sazonov/FastAPI_currency_project.git
2. Настройте виртуальную среду
3. В корне проекта создайте файл .env и заполните своими данными по примеру:<br>
SECRET_KEY = mysecretkey <br> ALGORITHM = algorithm <br> API_KEY = api_key
4. Запустите проект через файл main.py
### Примеры запросов к API с помощью Swagger UI
#### Регистрация пользователя: <br>
Запрос
![img.png](img_for_readme/img.png)
Ответ
![img_1.png](img_for_readme/img_1.png)
#### Аутентификация пользователя: <br>
Запрос
![img_2.png](img_for_readme/img_2.png)
Ответ
![img_3.png](img_for_readme/img_3.png)
#### Получение списка доступных валют: <br>
Запрос
![img_4.png](img_for_readme/img_4.png)
Ответ
![img_5.png](img_for_readme/img_5.png)
#### Конвертация валюты: <br>
Запрос
![img_6.png](img_for_readme/img_6.png)
Ответ
![img_7.png](img_for_readme/img_7.png)
