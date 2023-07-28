FROM python:3.10.3-slim

RUN pip install requests, csv


COPY main.py /app/main.py


WORKDIR /app


CMD ["python", "main.py"]
