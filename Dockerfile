FROM python:3

MAINTAINER Gal

ARG UBILD_NUMBER

ENV ENVIRONMENT=DEV

COPY requirements.txt ./

RUN echo ${UBILD_NUMBER} && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# VOLUME "/app/images"

#CMD [ "python", "./app.py" ]

ENTRYPOINT ["python", "app.py"]