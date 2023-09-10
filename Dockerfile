FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV APP_HOME=/app
RUN mkdir -p ${APP_HOME}
WORKDIR ${APP_HOME}
COPY . ${APP_HOME}/

RUN pip install --no-cache-dir -r requirements.txt
