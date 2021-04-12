FROM python:3.6
COPY . .
ENTRYPOINT ["python3", "dungeon.py"]