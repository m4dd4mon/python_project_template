"""Smoke-Tests: Paket laesst sich importieren."""

from __future__ import annotations


def test_import_projekt() -> None:
    """Das Wurzelpaket laesst sich importieren."""
    import projekt

    assert projekt.__version__ == "0.1.0"


def test_import_common_config() -> None:
    """Die Settings-Klasse laesst sich laden."""
    from projekt.common.config import settings

    assert settings.log_level == "INFO"


def test_import_common_logging() -> None:
    """get_logger liefert einen passend benannten Logger."""
    from projekt.common.logging import get_logger

    logger = get_logger("projekt.test")
    assert logger.name == "projekt.test"
