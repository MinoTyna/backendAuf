# --- Étape 1 : Image de base ---
FROM python:3.13-slim

# --- Étape 2 : Variables d'environnement ---
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# --- Étape 3 : Installer les dépendances système + client Postgres ---
RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    postgresql-client \
 && rm -rf /var/lib/apt/lists/*

# --- Étape 4 : Copier le code ---
WORKDIR /app
COPY . /app

# --- Étape 5 : Installer les dépendances Python ---
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# --- Étape 6 : Rendre le script exécutable ---
RUN chmod +x wait-for-db.sh

# --- Étape 7 : Commande de démarrage ---
# Ici on passe le HOST de la base comme premier argument
CMD ["./wait-for-db.sh", "db", "gunicorn", "monbackend.wsgi:application", "--bind", "0.0.0.0:8000"]
