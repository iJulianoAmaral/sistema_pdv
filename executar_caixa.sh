#!/bin/bash
# Verifica se Python está instalado
if ! command -v python3 &> /dev/null
then
    echo "Python3 não está instalado. Por favor, instale Python3 para executar este script."
    exit
fi

# Executa o arquivo Python
python3 sistema_caixa.py
