FROM python:3.12.3-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /doc_agrigation


RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*


RUN pip install pipenv


COPY Pipfile Pipfile.lock ./


RUN pipenv install --deploy --system


COPY . .


EXPOSE 8435

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8435"]
