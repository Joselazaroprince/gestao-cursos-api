# Imagem base oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de requisitos para o container
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código do projeto para dentro do container
COPY . .

# Expõe a porta padrão (usada por Railway via $PORT)
EXPOSE 8000

# Executa as migrações e coleta os arquivos estáticos antes de iniciar o servidor
CMD ["sh", "-c", "gunicorn gestao_cursos.wsgi:application --bind 0.0.0.0:${PORT}"]
