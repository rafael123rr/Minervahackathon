FROM python:3.6.2-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN brew install -r tesseractCMD [“python”, “flaskapp.py”]
