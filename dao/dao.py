import psycopg2
import os
import queries as q

if "PG_HOST" in os.environ:
	host = os.environ["PG_HOST"]
else:
	host = "localhost"

if "PG_DATABASE" in os.environ:
	database = os.environ["PG_DATABASE"]
else:
	database = "face_recognition"

if "PG_USER" in os.environ:
	user = os.environ["PG_USER"]
else:
	user = "postgres"

if "PG_PASSWORD" in os.environ:
	password = os.environ["PG_PASSWORD"]
else:
	password = "postgres"

conn = psycopg2.connect(host=host, database=database, user=user, password=password)
cur = conn.cursor()

def get_all_users():
	cur.execute(q.get_users)
	result = cur.fetchall()
	return result

def get_user(user_id):
	cur.execute(q.get_user_by_id, { "id": user_id })
	result = cur.fetchone()
	return result

def get_user_passwords(user_id):
	cur.execute(q.get_user_passwords, { "user_id": user_id })
	result = cur.fetchone()
	return result


def add_password(user_id, password, description):
	cur.execute(q.add_password, { "user_id": user_id, "password": password, "description": description })