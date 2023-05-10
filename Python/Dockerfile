FROM python:3.10-alpine3.16

RUN apk add nano
RUN pip install flask

LABEL app.version=v1
WORKDIR /app
COPY . .

EXPOSE 5000

CMD ["flask","run","--host=0.0.0.0"]