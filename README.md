# ShortLinks || PetProject

---

### Предварительные требования

- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

### Установка и запуск

1. Клонирование репозитория

```bash
git clone https://github.com/Chernov2312/short_links
```

2. Переход в папку проекта

```bash
cd short_links
```

3. Создание виртуального окружения

Linux/macOS

```bash
python3 -m venv venv
```

Windows (PowerShell)

```powershell
python -m venv venv
```

4. Активация виртуального окружения

Linux/macOS

```bash
source venv/bin/activate
```

Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

5. Установка зависимостей

Для запуска проекта

```bash
pip install -r requirements/prod.txt
```

6. Настройка переменных окружения

Linux/macOS

```bash
cp .env.example .env
```

Windows (PowerShell)

```powershell
Copy-Item .env.example .env
```


---
После запуска сервер будет доступен по адресу:

- Сервер: http://127.0.0.1:8000/


---

#### Функционал и API Эндпоинты

Сервис предоставляет REST API для управления ссылками и демонстрирует работу **Redis** в качестве сверхбыстрого *In-Memory* хранилища данных.

##### Ключевые возможности:
* **Генерация коротких ссылок:** Создание уникального случайного 7-значного токена для длинных URL с предварительной валидацией данных.
* **Декодирование и поиск:** Мгновенный поиск оригинального URL по его идентификатору.
* **Изолированное тестирование:** Логика полностью покрыта модульными тестами с использованием интеграционных моков.

##### 🛠 Спецификация API (Эндпоинты):

1. **Создание короткой ссылки**
   * **URL:** `/shorten`
   * **Метод:** `POST`
   * **Тело запроса (`JSON`):**
     ```json
     {
       "link": "https://github.com"
     }
     ```
   * **Успешный ответ (`201 Created`):**
     ```json
     {
       "status": "success",
       "short_url": "http://bestofthebest/a7x9f2q",
       "id": "a7x9f2q"
     }
     ```

2. **Получение оригинальной ссылки**
   * **URL:** `/long/<short_id>` (например, `/long/a7x9f2q`)
   * **Метод:** `GET`
   * **Успешный ответ (`200 OK`):**
     ```json
     {
       "status": "success",
       "link": "https://github.com"
     }
     ```
   * **Ошибка (`404 Not Found`):** Возвращается, если передан несуществующий или устаревший идентификатор.

##### 🏗 Технологический стек:
* **Backend Framework:** Sanic (асинхронный веб-сервер)
* **Валидация данных:** Pydantic v2
* **База данных:** Redis (структура данных `Key-Value`)
* **Тестирование:** Pytest + Pytest-Mock + Sanic-Testing
* **Контейнеризация:** Docker / Docker Compose

#### Установка зависимостей

Для разработки

```bash
pip install -r requirements/dev.txt
```

Для запуска тестов

```bash
pip install -r requirements/test.txt
```

---

#### Запуск тестов

Проверка flake8

```bash
flake8
```

Проверка black

```bash
black --check .
```

Тесты Sanic
```bash
python -m pytest web/test_main.py -v
```

---

###### Разработчик

```
Максим Чернов
```

---

<small>© 2026 Work by Max</small>