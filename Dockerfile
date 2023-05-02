FROM python:3.8-slim-buster
WORKDIR /python-docker

COPY ./src/requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./src .

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]
