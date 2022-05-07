FROM python:3.10

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN mkdir -p /vol/files
RUN adduser user
RUN chown -R user:user /vol/
RUN chmod -R 775 /vol/files
USER user
