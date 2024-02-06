FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt 
RUN python3 manage.py migrate

EXPOSE 8000

CMD ["python3", "manag.py", "runserver", "0.0.0.0:8000"]
