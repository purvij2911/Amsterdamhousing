FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP main.py
ENV FLASK_RUN_HOST 0.0.0.0

EXPOSE 5000

ENTRYPOINT [ "flask"]
CMD [ "run", "--host", "0.0.0.0" ]