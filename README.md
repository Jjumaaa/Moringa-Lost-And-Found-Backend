# Moringa-Lost-And-Found-Backend

A Flask REST API 
for managing users, admins, lost objects

## Setup
Clone the repository at:
https://github.com/Jjumaaa/Moringa-Lost-And-Found-Backend
Then, cd Moringa-Lost-And-Found-Backend
Install dependencies:
pipenv install
pipenv shell 

## Environment Variables
Create a .env file:

FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=super-secret-key
DATABASE_URL=sqlite:///moringa.db
## Dependencies
Install them with =pipenv "The dependency you want"

flask
flask-sqlalchemy
flask-migrate
flask-jwt-extended
psycopg2-binary
pipenv
shell
faker
alembic
flask-cors
sqlalchemy
serializer
sqlalchemy-serializer
flask-bcrypt
flask-restful

## Database Migrations
alembic init alembic
alembic revision --autogenerate -m "created all tables"
alembic upgrade head

## Seeding the Database
python seed.py

## Run the Server
python app.py