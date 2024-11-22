# TornBuddy

## First Run
postgres_host to compose_pg_service_name
docker-compose --env-file .env up  -d --build
docker-compose exec web python setup.py migrate
docker-compose exec web python manage.py collectstatic --no-input --clear
