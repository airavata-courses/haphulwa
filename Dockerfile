FROM python:3.4-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
ADD run.sh /
ADD client.py
CMD ["bash", "run.sh"]