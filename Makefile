
TAIL=100

# Позволяет с помощью переменной `c` указать конкретный контейнер из `docker-compose`.
# Например, make logs c='celery'
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

build:
	docker compose -f docker-compose.dev.yml build
up-d:
	docker compose -f docker-compose.dev.yml up -d
# без -d. чтобы быстрее перезапускать и логи видеть
up:
	docker compose -f docker-compose.dev.yml up
down:
	docker compose -f docker-compose.dev.yml down
logs: set-container
	docker compose -f docker-compose.dev.yml logs --tail=$(TAIL) -f $(c)
restart: set-container
	docker compose -f docker-compose.dev.yml restart $(c)
exec: set-container
	docker compose -f docker-compose.dev.yml exec $(c) /bin/bash

compile-reqs:
	docker compose -f docker-compose.dev.yml run --rm bot bash -c 'pip install pip-tools && pip-compile'

pre-commit:
	docker compose -f docker-compose.dev.yml run --rm bot bash -c 'pre-commit run --all-files'

