run:
ifeq ($(USE), docker)
	docker-compose up -d	
else 
	python escapehome/manage.py runserver 
endif

makemigrations: 
ifeq ($(USE), docker)
	docker-compose exec web python escapehome/manage.py makemigrations	
else 
	python escapehome/manage.py makemigrations 
endif

migrate: 
ifeq ($(USE), docker)
	docker-compose exec web python escapehome/manage.py migrate	
else 
	python escapehome/manage.py migrate 
endif

stop: 
ifeq ($(USE), docker)
	docker-compose stop
endif

logs: 
	docker-compose logs -f 

update-requirements: 
	. venv/bin/activate
	pip freeze > requirements.txt
	docker-compose exec web pip freeze > requirements_docker.txt