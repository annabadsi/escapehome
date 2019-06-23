SKILLID = amzn1.ask.skill.e5c0051e-6fcc-4c73-9a22-9487ee9b0d29
FILE_PATH = escapehome/json/model.json

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

skill-status:
	ask api get-skill-status -s ${SKILLID}

update-model:
	ask api update-model -s ${SKILLID} -f ${FILE_PATH} -l de-DE --stage development

get-model:
	ask api get-model -s ${SKILLID} --stage development -l de-DE > ${FILE_PATH}
