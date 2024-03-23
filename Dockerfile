FROM python:3.11-slim
LABEL maintainer="info@smartwash.dev"
ENV PYTHONUNBUFFERED 1

RUN apt-get update &&  \
    apt-get install --no-install-recommends -y \
    git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /code
COPY . /code

RUN chmod +x /code/.dockerinit.sh

# Чтобы на linux работал pre-commit из контейнера
RUN git config --global --add safe.directory /code

CMD [ "/code/.dockerinit.sh" ]
EXPOSE 8000
