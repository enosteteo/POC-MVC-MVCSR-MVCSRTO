# syntax=docker/dockerfile:1

FROM python:3.11.4-bookworm
LABEL mantainer="enosfrancisco@gmail.com"

# não gravar os bytecode (.pyc) no disco
ENV PYTHONDONTWRITEBYTECODE 1

# Não usar buffer para eventos do tipo saída
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/api

COPY requirements.txt /requirements.txt
COPY scripts /scripts

RUN python3 -m pip install --upgrade pip && \
 python3 -m pip install -r /requirements.txt && \
 chmod -R +x /scripts

# Adiciona a pasta scripts e venv/bin no $path do container
ENV PATH="/scripts:/venv/bin:$PATH"

COPY . .

CMD ["commands.sh"]
