# Usa uma imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos de requisitos e instala dependências
COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia todos os arquivos do projeto para dentro do contêiner
COPY . .

# Expõe a porta padrão usada por Railway via variável de ambiente
EXPOSE 8000

# Comando para rodar o Gunicorn com suporte à variável ${PORT}
CMD ["sh", "-c", "gunicorn gestao_cursos.wsgi:application --bind 0.0.0.0:${PORT}"]
