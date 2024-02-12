
FROM python:3.11.4

RUN pip install pipenv

COPY . /app
WORKDIR /app

RUN pipenv install --deploy --ignore-pipfile

RUN pipenv install your_personal_assistant_package==1.0.0

CMD ["pipenv", "run", "python", "__main__.py"]