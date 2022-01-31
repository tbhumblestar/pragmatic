FROM python:3.9.10

WORKDIR /home/

RUN git clone https://github.com/tbhumblestar/pragmatic.git

WORKDIR /home/pragmatic

COPY requirements.txt ./

RUN pip install -r requirements.txt

RUN echo "django-insecure-!ai$nrd6)^j2$9r%^ypgp1*l5)!ys5h*)e37$@lrc!7$2g*4tr" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]