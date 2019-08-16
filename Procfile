release: python3 src/manage.py makemigrations && python3 src/manage.py migrate
web: gunicorn --chdir src  config.wsgi --log-file - 
