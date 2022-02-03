FROM python:3.9.10

RUN echo "testing23422"

RUN git clone https://github.com/tbhumblestar/pragmatic.git

WORKDIR /pragmatic/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN echo "SECRET_KEY=django-insecure-!ai$nrd6)^j2$9r%^ypgp1*l5)!ys5h*)e37$@lrc!7$2g*4tr" > .env

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=pragmatic.settings.deploy && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]

