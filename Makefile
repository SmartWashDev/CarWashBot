
TAIL=100

# Позволяет с помощью переменной `c` указать конкретный контейнер из `docker-compose`.
# Например, make logs c=nats
define set-default-container
	ifndef c
	c = bot
	else ifeq (${c},all)
	override c=
	endif
endef


# Переменные для команд
set-container:
	$(eval $(call set-default-container))


# Пересобрать контейнер, например для обновления зависимостей
build:
	docker compose -f docker-compose.dev.yml build
# Запуск всех контейнеров
up:
	docker compose -f docker-compose.dev.yml up -d
# Отключение всех контейнеров
down:
	docker compose -f docker-compose.dev.yml down
# Просмотр логов, чтобы увидеть логи, например, натса: make logs c=nats
logs: set-container
	docker compose -f docker-compose.dev.yml logs --tail=$(TAIL) -f $(c)
# Перезапуск контейнера, по дефолту перезапустит бота
restart: set-container
	docker compose -f docker-compose.dev.yml restart $(c)
exec: set-container
	docker compose -f docker-compose.dev.yml exec $(c) /bin/bash

# Обновление зависимостей из `pyproject.toml`
compile-reqs:
	docker compose -f docker-compose.dev.yml run --rm bot bash -c 'pip install pip-tools && pip-compile'

# Приведения кода в порядок
pre-commit:
	docker compose -f docker-compose.dev.yml run --rm bot bash -c 'pre-commit run --all-files'

