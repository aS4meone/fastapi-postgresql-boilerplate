# FastAPI x PostgreSQL Boilerplate

- app/core/config - .env variables
- app/dependencies/database/db_connection - connection to a db, get_db function
- app/dependencies/database/base - file to which the "Base" of all created models is importing. Used to alembic revisions
- env.py, alembic.ini already configurated, just import your Bases into base.py

## Generating of a revision
   ```bash
      alembic revision --autogenerate
   ```

## Pushing a revisions into database
   ```bash
      alembic upgrade heads
   ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fastapi-sqlalchemy-example.git
   cd fastapi-sqlalchemy-example
