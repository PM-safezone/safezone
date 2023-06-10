#FROM python:3.9.0
#
#WORKDIR /home/
#
#RUN echo "testing8222228"
#
#RUN git clone https://github.com/PM-safezone/safezone.git
#
#WORKDIR /home/safezone/safezone
#
#RUN pip install -r requirements.txt
#
#RUN pip install mysqlclient
#
#RUN apt-get update && apt-get install -y libgl1-mesa-glx
#
#EXPOSE 8000
#
#CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=safezone.settings.deploy && python manage.py migrate --settings=safezone.settings.deploy && gunicorn safezone.wsgi --env DJANGO_SETTINGS_MODULE=safezone.settings.deploy --bind 0.0.0.0:8000 --timeout 600"]


FROM continuumio/anaconda3

WORKDIR /home/

# Create and activate a Python=3.9 conda environment
RUN conda create -n myenv python=3.9
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

# Install opencv
RUN conda install -c conda-forge opencv

RUN echo "testing8222228"

RUN git clone https://github.com/PM-safezone/safezone.git

WORKDIR /home/safezone/safezone

RUN pip install -r requirements.txt

RUN pip install mysqlclient

RUN apt-get update && apt-get install -y libgl1-mesa-glx

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=safezone.settings.deploy && python manage.py migrate --settings=safezone.settings.deploy && gunicorn safezone.wsgi --env DJANGO_SETTINGS_MODULE=safezone.settings.deploy --bind 0.0.0.0:8000 --timeout 600"]
