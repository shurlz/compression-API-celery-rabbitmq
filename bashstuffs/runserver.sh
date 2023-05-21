# /bin/bash

celery -A compressor worker -l INFO

celery -A compressor worker -B

python3 manage.py runserver