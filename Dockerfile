# Dockerfile
FROM python:3.10.4
WORKDIR /rest_service
COPY . /rest_service
RUN pip install -r requirements.txt
EXPOSE 8000
