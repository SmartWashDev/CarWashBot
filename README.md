# CatWashBot (@SmartWash)

Бот для отправки информации о распознанных авто в телеграм чат.

## Запуск

Для запуска со всеми сервисами рекомендуется использовать [Docker](https://docs.docker.com/engine/install).

### Конфигурация
Настройки проекта находятся в `app/config`.
Информация подтягивается из переменных окружения,
которые нужно задать в `.env` файле по примеру из `.env.example`.


### Запуск в контейнере
```bash
make up
```
Для перезапуска
```bash
make restart
```
> По дефолту перезапускает только бота

Все остальные команды можно найти в [Makefile`e](Makefile)

### Запуск бота нативно
Создаем окружение
```bash
python -m venv venv
```
Активируем его и устанавливаем зависимости
```bash
venv/Scripts/activate
```
```bash
pip install -r requirements.txt
```
Запустить бота
```bash
python -m app
```