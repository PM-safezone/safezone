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


#FROM continuumio/anaconda3
#
#WORKDIR /home/
#
## Create and activate a Python=3.9 conda environment
#RUN conda create -n myenv python=3.9
#SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]
#
## Install opencv
#RUN conda install -c conda-forge opencv
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
#

# 1. Use Ubuntu 22.04 as base image
#FROM ubuntu:22.04
#
## 2. Set working directory to /home/
#WORKDIR /home/
#
#RUN echo "testing3223"
## 3. Install Anaconda
#RUN apt-get update && apt-get install -y wget && \
#    wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh && \
#    bash Anaconda3-2021.05-Linux-x86_64.sh -b -p /opt/anaconda3 && \
#    rm Anaconda3-2021.05-Linux-x86_64.sh
#ENV PATH="/opt/anaconda3/bin:$PATH"
#
## 4. Create a new conda environment with Python 3.9
#RUN conda create -n myenv python=3.9
#
## Activate conda environment and make sure commands use it
#SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]
#
## 5. Install OpenCV
#RUN conda install -c conda-forge opencv
#
## 6. Clone safezone repository and install requirements
#RUN apt-get install -y git
#RUN git clone https://github.com/PM-safezone/safezone.git
#WORKDIR /home/safezone/safezone
#RUN pip install -r requirements.txt
#RUN apt-get install -y libmariadb-dev-compat
#RUN conda install mysqlclient
#RUN apt-get update && apt-get install -y libgl1-mesa-glx
#
## Expose the port Django app runs on
#EXPOSE 8000
#
## 7. Start the Django app within Anaconda environment
#CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=safezone.settings.deploy && python manage.py migrate --settings=safezone.settings.deploy && gunicorn safezone.wsgi --env DJANGO_SETTINGS_MODULE=safezone.settings.deploy --bind 0.0.0.0:8000 --timeout 600"]
#
#
#
#FROM ubuntu:22.04
#
## 2. Set working directory to /home/
#WORKDIR /home/
#
#RUN echo "testing321222221423"
#
## 3. Install Anaconda
#RUN apt update && apt install curl -y
#RUN curl --output anaconda.sh https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
#RUN sha256sum anaconda.sh
#RUN bash anaconda.sh -b -p /opt/anaconda3
#RUN rm anaconda.sh
#
## 4. Set environment variables
#ENV PATH="/opt/anaconda3/bin:$PATH"
#
## 5. Create a new conda environment with Python 3.9
#RUN conda create -y -n myenv python=3.9
#
## 6. Install OpenCV
#RUN /bin/bash -c "source /opt/anaconda3/bin/activate myenv && conda run -n myenv conda install -y -c conda-forge opencv"
#
## 7. Clone safezone repository and install requirements
#RUN apt-get install -y git
#RUN git clone https://github.com/PM-safezone/safezone.git
#WORKDIR /home/safezone/safezone
#
## 8. Install additional dependencies
#RUN apt-get update && apt-get install -y libmariadb-dev-compat
#
#
## 10. Install Python packages
#RUN /bin/bash -c "source /opt/anaconda3/bin/activate myenv && \
#    conda run -n myenv pip install mysqlclient django==4.1.5 django-bootstrap4 django-environ==0.10.0 Pillow==9.5.0 yolov5==7.0.12 torch torchvision gunicorn==20.1.0"
## 10. Expose the port Django app runs on
#EXPOSE 8000
#
## 11. Start the Django app within Anaconda environment
#CMD ["bash", "-c", "source /opt/anaconda3/bin/activate myenv && python manage.py collectstatic --noinput --settings=safezone.settings.deploy && python manage.py migrate --settings=safezone.settings.deploy && gunicorn safezone.wsgi --env DJANGO_SETTINGS_MODULE=safezone.settings.deploy --bind 0.0.0.0:8000 --timeout 600"]


FROM ubuntu:22.04

# 2. Set working directory to /home/
WORKDIR /home/

RUN echo "test322"

# 3. Install Anaconda
RUN apt update && apt install curl -y
RUN curl --output anaconda.sh https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
RUN sha256sum anaconda.sh
RUN bash anaconda.sh -b -p /opt/anaconda3
RUN rm anaconda.sh

# Install gcc
RUN apt-get update && apt-get install -y gcc

RUN apt-get update && apt-get install -y libgl1-mesa-glx
# 4. Set environment variables
ENV PATH="/opt/anaconda3/bin:$PATH"

# 5. Create a new conda environment with Python 3.9
RUN conda create -y -n myenv python=3.9

# 6. Install OpenCV
RUN /bin/bash -c "source /opt/anaconda3/bin/activate myenv && conda run -n myenv conda install -y -c conda-forge opencv"

# 7. Clone safezone repository and install requirements
RUN apt-get install -y git
RUN git clone https://github.com/PM-safezone/safezone.git
WORKDIR /home/safezone/safezone

# 8. Install additional dependencies
RUN /bin/bash -c "source /opt/anaconda3/bin/activate myenv && \
    conda run -n myenv apt-get install -y libmariadb-dev-compat"

# 10. Install Python packages
RUN /bin/bash -c "source /opt/anaconda3/bin/activate myenv && \
    conda run -n myenv pip install mysqlclient django==4.1.5 django-bootstrap4 django-environ==0.10.0 Pillow==9.5.0 yolov5==7.0.12 torch torchvision gunicorn==20.1.0"
# 10. Expose the port Django app runs on


EXPOSE 8000

# 11. Start the Django app within Anaconda environment
CMD ["bash", "-c", "source /opt/anaconda3/bin/activate myenv && python manage.py collectstatic --noinput --settings=safezone.settings.deploy && python manage.py migrate --settings=safezone.settings.deploy && gunicorn safezone.wsgi --env DJANGO_SETTINGS_MODULE=safezone.settings.deploy --bind 0.0.0.0:8000 --timeout 600"]
