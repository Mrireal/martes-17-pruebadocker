FROM python:3.12-slim

WORKDIR /app

# Copy project metadata first for better layer caching
COPY pyproject.toml ./

# Copy Python source files used by the package
COPY *.py ./

# Install project dependencies and the local package
RUN pip install -y --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir .
