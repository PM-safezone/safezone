FROM python:3.9.0

WORKDIR /home/

RUN echo "testing455"

RUN git clone https://github.com/PM-safezone/safezone.git

WORKDIR /home/safezone/safezone

RUN pip install -r requirements.txt

RUN pip install mysqlclient

RUN apt-get update && apt-get install -y libgl1-mesa-glx

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=safezone.settings.deploy && python manage.py migrate --settings=safezone.settings.deploy && gunicorn safezone.wsgi --env DJANGO_SETTINGS_MODULE=safezone.settings.deploy --bind 0.0.0.0:8000 --timeout 600"]
