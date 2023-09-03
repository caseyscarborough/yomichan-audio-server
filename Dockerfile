FROM python:3.9

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./plugin ./plugin
COPY ./main.py .

CMD ["python", "-u", "main.py"]