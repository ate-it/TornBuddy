# TornBuddy

## First Run

```
git clone https://github.com/ate-it/TornBuddy.git
cd TornBuddy/
cp .env.example .env.production
```

Update your .env file with production settings

We need to start the containers, run setup scripts, then restart the containers

```
docker-compose --env-file .env.production up  -d --build
docker-compose exec web python setup.py
docker-compose down
docker-compose --env-file .env.production up  -d
```

## Updates

```
git pull
docker-compose down
```
Make any manual changes as required

```
docker-compose --env-file .env.production up  -d --build

```
