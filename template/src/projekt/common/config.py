"""Anwendungs-Konfiguration.

Zentrale Settings-Klasse auf Basis von pydantic-settings. Sie liest
Defaults aus dem Code, ueberschreibt sie mit Werten aus .env und
Umgebungsvariablen. Die vollstaendige Dual-DB-Anbindung
(database_url_main, database_url_local) folgt im naechsten Schritt.
"""

from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Laufzeit-Einstellungen aus Umgebungsvariablen und .env."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    log_level: str = "INFO"


settings = Settings()
