FROM python:3.8-slim-buster
ENV PYTHONBUFFERED=1
WORKDIR /src

COPY src/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]
