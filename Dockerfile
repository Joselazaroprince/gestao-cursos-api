# Usa imagem oficial do Python
FROM python:3.12-slim

# Define diretório de trabalho
WORKDIR /app

# Atualiza pip e instala dependências Python
RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get clean

# Copia os arquivos do projeto
COPY . /app/

# Cria ambiente virtual + instala pacotes
RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Adiciona venv ao PATH
ENV PATH="/opt/venv/bin:$PATH"

# Expõe a porta do servidor
EXPOSE 8000

# Comando para iniciar com Gunicorn
CMD ["gunicorn", "gestao_cursos.wsgi:application", "--bind", "0.0.0.0:8000"]
