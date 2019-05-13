run:
	docker-compose up -d

bash: 
	docker-compose exec web bash 

shell:
	docker-compose exec web python escapehome/manage.py shell

makemigrations: 
	docker-compose exec web python escapehome/manage.py makemigrations

migrate: 
	docker-compose exec web python escapehome/manage.py migrate

stop: 
	docker-compose stop

logs: 
	docker-compose logs -f 

update-requirements: 
	. venv/bin/activate
	pip freeze > requirements.txt
	docker-compose exec web pip freeze > requirements_docker.txt