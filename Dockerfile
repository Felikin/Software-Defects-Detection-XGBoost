FROM python:3.9-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile.lock", "Pipfile", "./"]

RUN pipenv install --system --deploy

COPY ["predict.py", "xgb_model.bin", "./"]

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "predict:app" ]