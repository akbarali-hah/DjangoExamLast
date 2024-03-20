mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

refresh:
	docker exec -itu postgres pg_messenger psql -c 'drop database akbarali_db'
	docker exec -itu postgres pg_messenger psql -c 'create database akbarali_db with owner akbarali'
	make mig

admin:
	python3 manage.py createsuperuser

run:
	sudo chmod 666 /var/run/docker.sock
	docker start pg_messenger redis_db minio_tg

celery:
	celery -A root worker -l INFO