FROM python:3.12

LABEL key="shawaalnadeem63@gmail.com"

WORKDIR /code

COPY . /code/

RUN pip install poetry --default-timeout=100

RUN poetry config virtualenvs.create false

RUN poetry config installer.max-workers 1
RUN poetry install --no-interaction --no-ansi || (sleep 30 && poetry install --no-interaction --no-ansi)

CMD [ "poetry", "run", "uvicorn", "twitter_clone_backend.main:app", "--host", "0.0.0.0", "--reload" ]