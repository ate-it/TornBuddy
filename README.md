# TornBuddy

## First Run

```
git clone https://github.com/ate-it/TornBuddy.git
cd TornBuddy/
cp .env.example .env
```

Update your .env file with production settings

We need to start the containers, run setup scripts, then restart the containers

```
docker-compose --env-file .env up  -d --build
docker-compose exec web python manage.py collectstatic --no-input --clear
docker-compose exec web python setup.py
docker-compose down
docker-compose --env-file .env up  -d
```

## Updates

```
git pull
docker-compose down
docker-compose --env-file .env up  -d --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --no-input --clear
```
