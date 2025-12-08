#!/bin/sh
# wait-for-db.sh
set -e

host="$1"      # Nom ou IP de la base
shift
cmd="$@"       # Commande à exécuter après que la DB soit disponible

echo "Waiting for database at $host..."

until PGPASSWORD=$DB_PASSWORD psql -h "$host" -U "$DB_USER" -d "$DB_NAME" -c '\q'; do
  echo "Postgres is unavailable - sleeping"
  sleep 2
done

echo "Postgres is available - starting application..."
exec $cmd
