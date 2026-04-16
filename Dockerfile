FROM python:3.12-slim
WORKDIR /app
COPY app.py .
COPY controller ./controller
COPY entities ./entities
COPY services ./services
CMD ["python", "app.py"]