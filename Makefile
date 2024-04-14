.PHONY: up
up:
	docker-compose up

.PHONY: down
down:
	docker-compose down

.PHONY: build
build:
	docker-compose build --no-cache

.PHONY: clean
clean:
	docker-compose down --volumes --rmi all