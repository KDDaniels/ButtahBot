FROM python:3.10-slim

WORKDIR /app

COPY . /app/

RUN apt-get update && apt-get install -y ffmpeg

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]