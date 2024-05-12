FROM python:3.8

WORKDIR /usr/local/src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "app/api.py"]