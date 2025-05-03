# ---------- Build Stage ----------
FROM python:3.12-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    python3-dev \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN echo 'torch==2.7.0+cpu' > /tmp/constraints.txt && \
    pip install --upgrade pip && \
    pip install --no-cache-dir --prefix=/install \
        --extra-index-url https://download.pytorch.org/whl/cpu \
        -c /tmp/constraints.txt \
        onnxruntime==1.21.1 && \
    pip install --no-cache-dir --prefix=/install \
        --extra-index-url https://download.pytorch.org/whl/cpu \
        -c /tmp/constraints.txt \
        -r requirements.txt

# ---------- Runtime Stage ----------
FROM python:3.12-slim

WORKDIR /app

# Copy installed Python packages from builder stage
COPY --from=builder /install /usr/local

# Copy application code
COPY . .

# Runtime environment variables
ENV PYTHONUNBUFFERED=1 \
    TERM=xterm-256color \
    FORCE_COLOR=1 \
    DATABASE_PATH=/data/database.db \
    MIDDLE_SERVER_URL=https://ik8kcow8ksw8gwgoo0ggosko.dev.koii.network

# Expose application port
EXPOSE 8080

# Run app with Gunicorn
CMD ["gunicorn", \
    "--log-level=error", \
    "--error-logfile=-", \
    "--capture-output", \
    "--enable-stdio-inheritance", \
    "--logger-class=gunicorn.glogging.Logger", \
    "--timeout", "1800", \
    "--graceful-timeout", "1800", \
    "--keep-alive", "15", \
    "-w", "1", \
    "-b", "0.0.0.0:8080", \
    "main:app"]