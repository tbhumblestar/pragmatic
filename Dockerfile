FROM python:3.9.10

RUN echo "test132aASASDsdasd31asasdaasdasdasdsdasdas4141"

RUN git clone https://github.com/tbhumblestar/pragmatic.git

WORKDIR /pragmatic/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=pragmatic.settings.deploy && python manage.py migrate --settings=pragmatic.settings.deploy && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]

