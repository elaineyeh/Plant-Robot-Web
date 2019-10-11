#!/bin/sh
set -e

echo "Migrating Database"
python3 manage.py migrate

exec "$@"
