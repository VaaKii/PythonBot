FROM python:3.9

ENV PYTHONDONTWRYTEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN useradd -ms /bin/bash user
USER user

WORKDIR /home/user

COPY requirements.txt .
RUN pip install -r requirements.txt && rm requirements.txt

COPY . .

EXPOSE 10000

ENTRYPOINT ["python", "main.py"]