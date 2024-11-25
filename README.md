# TornBuddy

## First Run
postgres_host to compose_pg_service_name
redis_host to compose_file_service name

docker-compose --env-file .env up  -d --build
docker-compose exec web python manage.py collectstatic --no-input --clear
docker-compose exec web python setup.py
docker-compose down
docker-compose --env-file .env up  -d
