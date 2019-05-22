# README

## init

```
pipenv install
```

## run

```
pipenv run python manage.py runserver
```

## check

```
curl -X POST -H "Content-Type: application/json" -d "{ \"your_stone\": 1, \"squares\": [ [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, -1, 0, 0, 0], [0, 0, 0, -1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0] ]}" http://localhost:8000/api/osero/
```
