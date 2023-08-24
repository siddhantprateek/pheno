FROM python:3.10-slim
LABEL AUTHOR="siddhantprateek"
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY /app /app
EXPOSE 8000
CMD ["uvicorn", "main:app", "--reload"]
