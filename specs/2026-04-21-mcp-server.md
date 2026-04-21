# MCP-сервер для управления постами

## Зачем
Автор хочет создавать и редактировать статьи прямо из Claude Desktop, не заходя в админку браузера. MCP-сервер даёт Claude доступ к API блога как набор инструментов.

## Что делаем
Python MCP-сервер, который подключается к существующему REST API бэкенда (`/api/admin/*`) и предоставляет Claude Desktop инструменты для работы со статьями, категориями, тегами и медиафайлами. Автор пишет контент в Markdown — сервер конвертирует его в TipTap JSON перед сохранением и обратно при чтении.

## Требования

- [ ] Инструмент `list_articles` — список статей с фильтром по статусу (все / черновики / опубликованные)
- [ ] Инструмент `get_article` — получить статью по id или slug; контент возвращается в Markdown
- [ ] Инструмент `create_article` — создать статью (title, Markdown-контент, excerpt, category_ids, tag_ids, is_featured)
- [ ] Инструмент `update_article` — обновить любые поля статьи по id
- [ ] Инструмент `publish_article` — опубликовать статью по id
- [ ] Инструмент `unpublish_article` — снять статью с публикации по id
- [ ] Инструмент `list_categories` — список всех категорий
- [ ] Инструмент `create_category` — создать категорию (name, description, color)
- [ ] Инструмент `list_tags` — список всех тегов
- [ ] Инструмент `create_tag` — создать тег (name, color)
- [ ] Инструмент `upload_image` — принять локальный путь к файлу, загрузить через API, вернуть URL
- [ ] Авторизация: сервер логинится при старте через `ADMIN_EMAIL` + `ADMIN_PASSWORD` из env, кэширует JWT; при истечении токена — автоматически перелогинивается
- [ ] Конвертер Markdown → TipTap JSON (для create/update)
- [ ] Конвертер TipTap JSON → Markdown (для get/list)
- [ ] Автозагрузка локальных изображений из Markdown-контента: перед конвертацией сканировать `![alt](path)`, если `path` — локальный путь к файлу, загружать через `POST /api/admin/media` и заменять на полученный URL

## Технический план

### Структура

```
mcp-server/
  server.py          # точка входа, регистрация tools
  api_client.py      # HTTP-клиент к бэкенду, управление токеном
  converters.py      # Markdown ↔ TipTap JSON
  requirements.txt
  README.md          # инструкция по подключению в Claude Desktop
```

### Зависимости

- `mcp` — официальный Python SDK от Anthropic
- `httpx` — HTTP-клиент для запросов к API
- `mistune` — парсинг Markdown → AST для конвертации в TipTap JSON

### api_client.py

- Класс `BackendClient` с методами под каждый эндпоинт
- При инициализации логинится, сохраняет токен
- Middleware на каждый запрос: если `401` — повторный логин и ретрай

### converters.py

Поддерживаемые элементы Markdown → TipTap:

| Markdown | TipTap node |
|----------|-------------|
| `# H1..H6` | `heading` |
| Параграф | `paragraph` |
| `**bold**` | mark `bold` |
| `*italic*` | mark `italic` |
| `` `code` `` | mark `code` |
| ` ```block``` ` | `codeBlock` |
| `- item` / `1. item` | `bulletList` / `orderedList` |
| `> quote` | `blockquote` |
| `[text](url)` | mark `link` |
| `---` | `horizontalRule` |

### Инструмент upload_image

1. Принимает абсолютный путь к файлу
2. Читает файл, отправляет `multipart/form-data` на `POST /api/admin/media`
3. Возвращает `url` из ответа

### Автозагрузка изображений из Markdown

При вызове `create_article` / `update_article` перед конвертацией в TipTap:

1. Найти все вхождения `![alt](path)` в тексте регулярным выражением
2. Для каждого `path`: если это локальный путь (не начинается с `http`/`https`/`/uploads`) — загрузить файл через `upload_image` и заменить `path` на полученный URL
3. Только после этого передавать Markdown в конвертер

### Подключение к Claude Desktop

В `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "ursoaia": {
      "command": "python",
      "args": ["/path/to/mcp-server/server.py"],
      "env": {
        "API_URL": "http://localhost:8000",
        "ADMIN_EMAIL": "...",
        "ADMIN_PASSWORD": "..."
      }
    }
  }
}
```

### Миграции БД
Не нужны — сервер работает через существующий API.

## Открытые вопросы
Нет.

## Вне скоупа
- Удаление статей, категорий, тегов
- Редактирование и удаление медиафайлов
- Работа с несколькими авторами / пользователями
- Веб-хук уведомления
- Поддержка других MCP-клиентов кроме Claude Desktop
