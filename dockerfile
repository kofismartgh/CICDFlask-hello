FROM python:3.8-slim
WORKDIR /app
RUN pip install flask
COPY . /app
EXPOSE 80
CMD ["python", "test.py"]

