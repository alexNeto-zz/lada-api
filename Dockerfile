FROM python:3.7

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY api ./api
COPY main.py ./
COPY boot.sh ./

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn
RUN chmod +x boot.sh

ENV FLASK_APP main.py

EXPOSE 5000

ENTRYPOINT ["./boot"]