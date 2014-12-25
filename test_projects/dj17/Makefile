migrate: venv
	rm -f db.sqlite3
	venv/bin/python manage.py migrate

venv:
	virtualenv venv
	venv/bin/pip install -r requirements.txt

