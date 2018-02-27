FROM python:3

WORKDIR /app

ADD ./build/venv /app

CMD ["./bin/app"]
