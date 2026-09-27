# Bike Shop
**Python · Django · SQLite · Server-rendered templates**

A Django learning project that models bike components, displays a catalog, accepts customer orders, and updates component inventory.

## Features
- Bike catalog and individual bike pages.
- Component availability checks on the detail page.
- Customer order form and order confirmation page.
- Inventory models for frames, seats, tires, and baskets.
- Django admin for managing records.

## Run locally
Use a Python environment compatible with the pinned Django version.

```bash
git clone https://github.com/nursala/Bike-Shop.git
cd Bike-Shop
python -m venv .venv
```

Activate the environment: `source .venv/bin/activate` on macOS/Linux, or `.venv\Scripts\Activate.ps1` in Windows PowerShell.

```bash
pip install Django==6.0.4
cd "Bike Shop/task"
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open **http://127.0.0.1:8000/bikes/**. Use **/admin/** to add components and bikes if the catalog is empty. A bike needs one frame, one seat, and two tires; basket-equipped bikes also require a basket.

## Application map
| URL | View |
| --- | --- |
| `/bikes/` | Catalog using `ListView` |
| `/bikes/<id>/` | Bike details, availability, and order submission |
| `/order/<id>/` | Order confirmation |
| `/admin/` | Django administration |

The application lives in [Bike Shop/task](Bike%20Shop/task/). Models, forms, views, and templates are in its `shop` app. The surrounding course folders contain Hyperskill exercises and test scaffolding.

## Engineering focus
Relational modeling with foreign keys, Django's ORM and migrations, class-based views, model forms, and template rendering.

## Current limitations
This is a learning project with no payment integration. Order creation and inventory updates are not wrapped in a database transaction, and stock is not revalidated atomically on submission. Concurrent orders can therefore oversell inventory; production use would need transactional stock checks and access controls for customer order details.
