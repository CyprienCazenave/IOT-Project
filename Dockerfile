FROM python:3

RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin libgdal-dev gir1.2-gtk-4.0

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

WORKDIR /usr/src/app

COPY ./backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install djangorestframework-gis

COPY ./backend/ .

CMD ["python", "./src/manage.py", "runserver","0.0.0.0:8000",  "--settings=core.settings"]