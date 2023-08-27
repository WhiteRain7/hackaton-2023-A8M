# A8M

## Backend

Используется python 3.11.

Для генерации изображений потребуется библиотека stableDiffusion (при отсутствии - работает без картинок).

### Запуск ([порт 8000](http://localhost:8000))

- `cp .env_example .env`
- `docker compose up -d`

Или

- `cp .env_example .env`
- `pip install -r requirements.txt`
- `uvicorn app.main:app --host 0.0.0.0 --port 8000`

### Основные файлы и папки (backend/)

- `app/main.py` - главный файл python
- `app/config.py` - конфигурационный файл python
- 
- `.env` - окружение (только почта и пароль от hugchat)
- `requirements.txt` - необходимые библиотеки python (устанавливаются если с docker)

## Frontend

Используется фреймворк Nuxt2 (JavaScript). Сайт выполнен в одностраничном формате.

Использованная версия node - `18.17.0`

Использованная версия npm - `9.6.7`

### Запуск dev версии ([порт 3000](http://localhost:3000))

- `npm install`
- `npm run dev`

### Создание "статичного" сайта

- `npm run build`
- `bpn run generate`

Обычно результат сохраняется в папку dict/

### Основные файлы (front/)

- `pages/index.vue` - основная (и единственная) страница сайта
- `components/navButton.vue` - компонент vue, используется в навигации nav#header-nav
- 
- `static/favicon.ico` - иконка сайта (сейчас - стандартная от vue)
- `package.json` - используемые модули
- `nuxt.config.js` - конфигурационный файл nuxt

## Команда

- Максим "mrgick" Малахов - backend
- Глеб "KGlebB" Никифоров - аналитика и второй backend
- Максим "WhiteRain7" Макаров - frontend
