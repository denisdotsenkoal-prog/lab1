# ЗВІТ
## до лабораторної роботи №1
### «Реалізація простого вебзастосунку»

**Студент:** Доценко Денис Олексійович
**Група:** 6.1224
**Дисципліна:** Веб-програмування

## 1. Мета роботи
Навчитися реалізовувати прості вебзастосунки з використанням різних стеків розробки.

## 2. Обрані стеки
1. Node.js 24, порт 3001.
2. Python 3, порт 3002.

## 3. Структура проєкту
Проєкт містить дві незалежні реалізації з однаковими HTML/CSS-сторінками та різними серверними файлами.

## 4. Реалізація
Обидва сервери явно зіставляють URL із файлами `public`. Маршрути `/`, `/about` та `/styles.css` повертають відповідні ресурси зі статусом 200. Невідомий маршрут повертає `404.html` зі статусом 404 без перенаправлення.

## 5. Команди запуску
### Node.js
```bash
cd node
node server.mjs
```

### Python
```bash
cd python
python3 server.py
```

## 6. Команди перевірки
```bash
curl -i http://localhost:3001/
curl -i http://localhost:3001/about
curl -i http://localhost:3001/styles.css
curl -i http://localhost:3001/nope
curl -i http://localhost:3001/missing/page
curl -i 'http://localhost:3001/about?source=test'
curl -i http://localhost:3001/about.html
```
Аналогічні команди виконуються для Python з портом `3002`.

## 7. Таблиця перевірок
| Стек | Шлях | Очікуваний статус | Content-Type | Отриманий вміст |
|---|---|---:|---|---|
| Node.js | `/` | 200 | text/html; charset=utf-8 | `index.html` |
| Node.js | `/about` | 200 | text/html; charset=utf-8 | `about.html` |
| Node.js | `/styles.css` | 200 | text/css; charset=utf-8 | `styles.css` |
| Node.js | `/nope` | 404 | text/html; charset=utf-8 | `404.html` |
| Node.js | `/missing/page` | 404 | text/html; charset=utf-8 | `404.html` |
| Node.js | `/about?source=test` | 200 | text/html; charset=utf-8 | `about.html` |
| Node.js | `/about.html` | 404 | text/html; charset=utf-8 | `404.html` |
| Python | `/` | 200 | text/html; charset=utf-8 | `index.html` |
| Python | `/about` | 200 | text/html; charset=utf-8 | `about.html` |
| Python | `/styles.css` | 200 | text/css; charset=utf-8 | `styles.css` |
| Python | `/nope` | 404 | text/html; charset=utf-8 | `404.html` |
| Python | `/missing/page` | 404 | text/html; charset=utf-8 | `404.html` |
| Python | `/about?source=test` | 200 | text/html; charset=utf-8 | `about.html` |
| Python | `/about.html` | 404 | text/html; charset=utf-8 | `404.html` |

## 8. Порівняння реалізацій
У Node.js HTTP-сервер створено через стандартний модуль `node:http`, а файли читаються через `readFileSync` і `new URL(..., import.meta.url)`. У Python використано `http.server`, `pathlib.Path` та `urlsplit`. В обох реалізаціях маршрут визначається явно, CSS обробляється окремим маршрутом, а невідомі адреси отримують статус 404.

## 9. Контрольні питання
### 1. Який шлях потрібно зіставити для `/about?source=test`?
Потрібно зіставити шлях `/about`, оскільки параметр запиту не змінює вибір маршруту.

### 2. Який ресурс браузер запитає для оформлення `/missing/page`?
Оскільки в HTML використано `href="/styles.css"`, браузер запитає ресурс `/styles.css`.

### 3. Що підтверджує правильну обробку невідомого шляху?
Запит невідомого шляху має повернути HTTP-статус 404, сторінку `404.html`, залишити адресу запиту без змін і не містити заголовка `Location`. CSS при цьому має окремо повертатися зі статусом 200.

## 10. Скріншоти
Додати:
1. Головна — Node.js.
2. Про роботу — Node.js.
3. Сторінка 404 — Node.js.
4. Network — Node.js.
5. Головна — Python.
6. Про роботу — Python.
7. Сторінка 404 — Python.
8. Network — Python.

На скріншотах мають бути видимі адресний рядок, дані студента та середовище.

## 11. Висновок
У ході лабораторної роботи реалізовано простий вебзастосунок на двох стеках — Node.js та Python. Реалізації підтримують однакові маршрути, коректні HTTP-статуси та Content-Type, обробку параметрів запиту, окрему видачу CSS і сторінку 404 без перенаправлення.