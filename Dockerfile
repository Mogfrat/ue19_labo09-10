FROM python3

Workdir /usr/src/app

ENV token your_token

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./app.py"]