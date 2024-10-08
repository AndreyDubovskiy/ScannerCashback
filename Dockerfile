FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir /app/logger/log
CMD ["python", "main.py"]