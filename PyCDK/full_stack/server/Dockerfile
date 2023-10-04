FROM --platform=linux/x86-64 alpine:latest


WORKDIR /server

COPY . .

RUN apk add py3-pip
RUN pip3 install flask
RUN pip3 install -r requirements.txt

EXPOSE 80

CMD ["gunicorn", "-w", "4", "app:app", "--bind", "0.0.0.0:80"]