FROM python:alpine as build-stage

RUN apk update && apk add postgresql-dev gcc musl-dev

RUN python -m venv /venv
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
WORKDIR /application

COPY requirements.txt .
RUN pip install wheel
RUN pip install -r requirements.txt



FROM python:alpine as final

RUN apk add libpq

ENV PYTHONDONTWRITEBYTECODE=1

ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
WORKDIR /application

COPY --from=build-stage /venv /venv

COPY . .

EXPOSE 5000/tcp

CMD python application.py