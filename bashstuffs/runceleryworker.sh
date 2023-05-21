# /bin/bash

echo "== RUNNING CELERY WORKER =="

celery -A compressor worker -B