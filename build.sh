#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python socials/manage.py collectstatic --no-input
python socials/manage.py migrate
