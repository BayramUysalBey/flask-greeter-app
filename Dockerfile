FROM python:3.12-slim

RUN apt-get update && apt-get install -y build-essential dos2unix

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY static static
COPY app.py boot.sh ./

RUN dos2unix boot.sh

RUN chmod a+x boot.sh
COPY templates templates
ENV FLASK_APP=app.py
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]