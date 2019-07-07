SKILLID = amzn1.ask.skill.e5c0051e-6fcc-4c73-9a22-9487ee9b0d29
STATIC_PATH = escapehome/escapehome/static

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

get-skill:
	ask api get-skill -s ${SKILLID} --stage development > ${STATIC_PATH}/skill.json

update-skill:
	ask api update-skill -s ${SKILLID} --stage development -f ${STATIC_PATH}/skill.json

get-model:
	ask api get-model -s ${SKILLID} --stage development -l de-DE > ${STATIC_PATH}/model.json

update-model:
	ask api update-model -s ${SKILLID} -f ${STATIC_PATH}/model.json -l de-DE --stage development
