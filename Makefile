install:
	pip install -r requirements.txt

install-no-cache:
	pip install --no-cache-dir -r requirements.txt

migration-up:
	alembic upgrade heads

migration-down:
	alembic downgrade base

migration-create:
	alembic revision -m "$(name)"

migration-generate:
	alembic revision --autogenerate -m "$(name)"

dev: 
	python main.py 

docker-api:
	docker-compose up api

