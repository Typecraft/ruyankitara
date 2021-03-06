.PHONY: test
test:
	python manage.py test

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: migrations
migrations:
	python manage.py makemigrations

.PHONY: run
run:
	python manage.py runserver 0.0.0.0:8012

.PHONY: shell
shell:
	python manage.py shell

.PHONY: superuser
superuser:
	python manage.py createsuperuser

.PHONY: freeze
freeze:
	rm -f requirements.txt && pip freeze > requirements.txt
