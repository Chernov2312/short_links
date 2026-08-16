FROM python:3.13-slim

LABEL maintainer="Max"
LABEL description="Servise short link"

WORKDIR /app

RUN apt-get update && apt-get upgrade -y && apt-get install -y bash

COPY requirements/ ./requirements/
RUN pip install --no-cache-dir -r requirements/prod.txt

COPY . .

CMD ["python", "web/main.py"]