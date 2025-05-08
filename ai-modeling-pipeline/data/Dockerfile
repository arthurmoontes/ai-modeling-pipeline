# Imagem base
FROM python:3.10-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copiar todos os arquivos para o container
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir pandas numpy scikit-learn joblib flask

# Expor a porta usada pelo Flask
EXPOSE 5000

# Comando padrão
CMD ["python", "src/api/app.py"]
