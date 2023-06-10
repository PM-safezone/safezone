FROM python:3.9.0

WORKDIR /home/

RUN echo "testing88"

RUN git clone https://github.com/PM-safezone/safezone.git

WORKDIR /home/safezone/safezone

RUN pip install -r requirements.txt

RUN pip install mysqlclient

RUN apt-get update && apt-get install -y libgl1-mesa-glx

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=safezone.settings.deploy && python manage.py migrate --settings=safezone.settings.deploy && gunicorn safezone.wsgi --env DJANGO_SETTINGS_MODULE=safezone.settings.deploy --bind 0.0.0.0:8000 --timeout 600"]
#FROM python:3.9.0
#
#WORKDIR /home/
#
#RUN echo "testing33122"
#
#RUN git clone https://github.com/PM-safezone/safezone.git
#
#WORKDIR /home/safezone/safezone
#
#RUN pip install -r requirements.txt
#
#RUN echo "SECRET_KEY=django-insecure-j!1$5ccgna@8!g5p*v^0dg%ws0naauc-g13%5jpiskx&qxyz70" > .env
#
#RUN apt-get update && apt-get install -y libgl1-mesa-glx
#
#RUN python manage.py migrate
#
#RUN python manage.py collectstatic
#
#EXPOSE 80
#
#CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
