# Лабораторна робота 1 — Реалізація простого вебзастосунку

**Студент:** Доценко Денис Олексійович
**Група:** 6.1224

## Обрані стеки
- Node.js 24 — порт 3001
- Python 3 — порт 3002

## Структура
```text
lab1/
├── README.md
├── node/
│   ├── server.mjs
│   └── public/
│       ├── index.html
│       ├── about.html
│       ├── 404.html
│       └── styles.css
└── python/
    ├── server.py
    └── public/
        ├── index.html
        ├── about.html
        ├── 404.html
        └── styles.css
```

## Перевірка середовища
```bash
node --version
python3 --version
curl --version
```

## Запуск Node.js
```bash
cd node
node server.mjs
```
Адреса: http://localhost:3001

## Запуск Python
В іншому терміналі:
```bash
cd python
python3 server.py
```
Адреса: http://localhost:3002

## Перевірка curl
Для Node.js:
```bash
curl -i http://localhost:3001/
curl -i http://localhost:3001/about
curl -i http://localhost:3001/styles.css
curl -i http://localhost:3001/nope
curl -i http://localhost:3001/missing/page
curl -i 'http://localhost:3001/about?source=test'
curl -i http://localhost:3001/about.html
```
Для Python ті самі команди з портом `3002`.

## Очікуваний контракт
| Шлях | Статус | Content-Type |
|---|---:|---|
| `/` | 200 | text/html; charset=utf-8 |
| `/about` | 200 | text/html; charset=utf-8 |
| `/styles.css` | 200 | text/css; charset=utf-8 |
| будь-який інший шлях | 404 | text/html; charset=utf-8 |

Параметри запиту не впливають на вибір маршруту. Перенаправлення для 404 не використовується, тому заголовок `Location` не встановлюється.
