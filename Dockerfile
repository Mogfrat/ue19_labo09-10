FROM python:3.10.1

Workdir /usr/src/app

ENV token your_token

COPY requirements.txt ./
RUN python -m venv ./venv
RUN venv/bin/pip install --no-cache-dir -r requirements.txt

CMD ["python", "./app.py"]
