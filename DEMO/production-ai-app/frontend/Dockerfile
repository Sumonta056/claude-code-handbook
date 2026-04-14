FROM python:3.11-slim

WORKDIR /frontend

COPY frontend/requirements.txt ./
COPY frontend/app.py ./
COPY frontend/static ./static

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["python", "app.py"]
