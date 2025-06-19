# Étape de construction
FROM python:3.10-slim AS builder

WORKDIR /

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential=12.9 && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.10-slim

WORKDIR /

COPY --from=builder /venv /venv

ENV PATH="/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY . .

EXPOSE 5000

CMD ["python", "main.py"]
