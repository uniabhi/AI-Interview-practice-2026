FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN groupadd --system appgroup && \
    useradd --system --gid appgroup --no-create-home appuser

COPY --chown=appuser:appgroup app.py .

USER appuser

# EXPOSE 8000   # uncomment if it's a web server

CMD ["python", "app.py"]