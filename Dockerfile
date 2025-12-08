# --- Étape 1 : Image de base ---
FROM python:3.10-slim

# --- Étape 2 : Variables d'environnement ---
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# --- Étape 3 : Installer les dépendances système ---
RUN apt update && apt install -y build-essential libpq-dev

# --- Étape 4 : Répertoire de travail ---
WORKDIR /app

# --- Étape 5 : Copier et installer les dépendances Python ---
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Étape 6 : Copier tout le projet ---
COPY . .

# --- Étape 7 : Exposer le port Django ---
EXPOSE 8000

# --- Étape 8 : Lancer Django ---
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
