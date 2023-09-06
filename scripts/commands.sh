#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e

# Comando para executar o servidor de desenvolvimento
python -m flask --app $1 run --debug --host=0.0.0.0 -p 8000

# python -m flask --app app run --debug --host=0.0.0.0 -p 8000
