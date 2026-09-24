# Bike Shop — Django exercise

A small Django project for modeling bike components and displaying a bike catalog. This repository includes the course task materials under `Bike Shop/`; the runnable app lives in `Bike Shop/task/`.

## Run

From the repository root:

```bash
python -m venv .venv
. .venv/bin/activate
pip install Django==6.0.4
cd "Bike Shop/task"
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/bikes/`. The database starts with no catalog entries. Add frames, seats, tires, and bikes in Django admin after creating a superuser:

```bash
python manage.py createsuperuser
```

## Current scope

The models cover component inventory, bikes, and orders. The current public view lists bikes; this is a learning exercise, not a finished checkout flow. The course task HTML and test scaffolding are retained for reference.

## Verification

`python manage.py check` passes. The `/bikes/` view was exercised through Django's test client after correcting the template path.