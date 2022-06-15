FROM python:slim-bullseye

RUN apt-get update \
 && apt-get install -y \
      build-essential \
      nodejs \
      npm \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /etc/uwsgi/sites
COPY tealdb.ini /etc/uwsgi/sites

RUN pip3 install Django==4.0.5
RUN pip3 install psycopg2-binary==2.9.3
RUN pip3 install django-bower==5.2.0
RUN pip3 install uWSGI==2.0.20

WORKDIR /app/src
COPY . .

RUN npm install bower

ENTRYPOINT ["/app/src/docker-entrypoint.sh"]
CMD ["uwsgi", "-H", "/app/src", "--emperor", "/etc/uwsgi/sites"]
