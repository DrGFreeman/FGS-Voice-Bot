FROM python:3.10-slim

WORKDIR /app

COPY .env .
COPY *.py ./
COPY *.txt ./

RUN pip install -r requirements.txt

CMD ["python", "fgs_voice_bot.py"]
