#### compression-API-celery-rabbitmq

##### for docker:
      - docker-compose up --build

##### for local: 
      - requires: python, rabbitmq installed
      - run: 
        - python manage.py server
        - system rabbitmq-server start
        - celery -A compressor worker -l INFO
        - celery -A compressor worker -B
