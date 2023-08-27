# A8M

Репозиторий содержит решение кейс ООО «Акселератор Возможностей» при ИНТЦ МГУ «Воробьевы горы» от команды A8M.

[Пример работы (screencast)](https://youtu.be/_UPlcusC7YE)

## Backend

### Зависимости
- Используется python 3.11.
- Файл зависимостей requirements.txt
- Для генерации изображений потребуется stableDiffusion, работающий на основе api [webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui), который запущен локально (в дальнейшем можно будет добавить в докер, пока рекомендуется запускать проект напрямую для работы stableDiffusion)
- Для генерации текста, потребуется openassistant, работающая на основе api [hugchat](https://github.com/huggingface/chat-ui), на данный момент можно указать почту/пароль от huggingface для проверки (по запросу к нам - можем предоставить тестовый аккаунт).

Документация к API доступна после запуска по ссылке http://127.0.0.1:8000/docs#.

### Запуск backend решения ([порт 8000](http://localhost:8000))

- `cp .env_example .env`
- `pip install -r requirements.txt`
- `uvicorn app.main:app --port 8000`

Или 

- `cp .env_example .env`
- `docker compose up -d`

### Основные файлы и папки (backend/)

- `app/main.py` - главный файл python
- `app/config.py` - конфигурационный файл python
- 
- `.env` - окружение (следует указать почту и пароль от hugchat)
- `requirements.txt` - необходимые библиотеки python (устанавливаются если с docker)
- `app/templates/` - темы презентаций
- `app/service/` - логика работы приложения
- `app/routers/` - точки доступа в апи
- `app/hugchat/` - апи hugchat
- `app/media/` - папка для хранения временных файлов
- `app/schemas/` - папка для хранения схем (вид полей, что приходит и уходит)

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
