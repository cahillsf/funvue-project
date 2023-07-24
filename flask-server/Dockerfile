FROM python:3.9-alpine
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
ADD app.py /app
ADD config.py /app
RUN apk update && apk add python3-dev \
                        libffi-dev \
                        gcc \
                        libc-dev
RUN pip3 install -r requirements.txt
CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:8000", "--log-level=debug", "app:app"]