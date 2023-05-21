# /bin/bash

echo "== RUNNING CELERY MASTER =="

celery -A compressor worker -l INFO