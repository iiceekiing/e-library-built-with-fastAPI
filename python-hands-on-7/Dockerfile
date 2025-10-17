FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8003
CMD ["uvicorn", "task1:app", "--host", "0.0.000", "--port", "8003"]