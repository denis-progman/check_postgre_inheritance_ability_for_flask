FROM python:3
WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN apt-get update -y \ 
&& apt-get install -y \
openrc \
curl

RUN pip3 install -r requirements.txt

CMD python3 -m flask run --host=0.0.0.0

# ENTRYPOINT ["tail", "-f", "/dev/null"]
# CMD python3 -m flask run --host=127.0.0.1:5000
