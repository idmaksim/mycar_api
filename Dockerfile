FROM python

WORKDIR /app

COPY requirements.txt .

COPY images .

RUN pip install -r requirements.txt

COPY . .

CMD ["fastapi", "run", "src/app.py", "--port", "80"]