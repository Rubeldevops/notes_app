FROM python:3.9-slim as Builder

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --user -r requirements.txt 

#stage 2

FROM python:3.9-slim

WORKDIR /app

COPY . .

COPY --from=builder /root/.local /root/.local

EXPOSE 5000

CMD ["python", "app.py"]

