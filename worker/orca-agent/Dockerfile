###############################################################################
#                             ──  builder  ──                                #
###############################################################################
ARG PY_VER=3.12
FROM python:${PY_VER}-slim AS builder
WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_PYTHON_VERSION_WARNING=1 \
    PIP_ROOT_USER_ACTION=ignore

# tiny tool‑chain (needed by a few wheels)
RUN apt-get update && apt-get install -y --no-install-recommends \
        gcc g++ make \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# --- install deps into /install ------------------------------------------------
RUN echo 'torch==2.7.0+cpu' > /tmp/constraints.txt && \
    pip install -q --no-cache-dir --no-compile --prefix=/install              \
        --extra-index-url https://download.pytorch.org/whl/cpu                \
        -c /tmp/constraints.txt onnxruntime==1.21.1 && \
    pip install -q --no-cache-dir --no-compile --prefix=/install              \
        --extra-index-url https://download.pytorch.org/whl/cpu                \
        -c /tmp/constraints.txt -r requirements.txt

# --- byte‑compile but KEEP .py & tests ----------------------------------------
RUN python -m compileall -q /install --invalidation-mode=unchecked-hash && \
    find /install -type d -name '__pycache__' -prune -exec rm -rf {} +

# optional: uninstall build helpers from site‑packages
RUN python -m pip uninstall -y pip wheel setuptools

###############################################################################
#                             ──  runtime  ──                                 #
###############################################################################
FROM python:${PY_VER}-slim
WORKDIR /app

# runtime util
RUN apt-get update && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /install /usr/local
RUN git config --global --add safe.directory /app

COPY . .

ENV PYTHONUNBUFFERED=1 \
    TERM=xterm-256color \
    DATABASE_PATH=/data/database.db \
    MIDDLE_SERVER_URL=https://ik8kcow8ksw8gwgoo0ggosko.dev.koii.network

EXPOSE 8080
CMD ["gunicorn", "--log-level=error", "--error-logfile=-", "--capture-output", \
     "--enable-stdio-inheritance", "--logger-class=gunicorn.glogging.Logger", \
     "--timeout", "1800", "--graceful-timeout", "1800", "--keep-alive", "15", \
     "-w", "1", "-b", "0.0.0.0:8080", "main:app"]
