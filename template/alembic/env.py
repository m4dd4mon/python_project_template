# Alembic-Umgebung (Standardform). Der -x db_url-Mechanismus fuer den
# Dual-DB-Betrieb wird im naechsten Schritt ergaenzt.

from __future__ import annotations

from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# target_metadata wird spaeter auf Base.metadata gesetzt, sobald die
# ORM-Modelle in src/projekt/data/models.py existieren.
target_metadata = None


def run_migrations_offline() -> None:
    """Migrationen im Offline-Modus ausfuehren."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Migrationen mit aktiver DB-Verbindung ausfuehren."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
