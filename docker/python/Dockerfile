FROM python:3
WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN apt-get update -y \ 
&& apt-get install -y \
openrc \
curl

CMD pip3 install -r requirements.txt && python3 -m flask --debug run --host=0.0.0.0

# ENTRYPOINT ["tail", "-f", "/dev/null"] # debagging mode
