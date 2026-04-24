"""Zentrale Logging-Helfer.

Die vollstaendige dictConfig-Initialisierung aus resources/logging.yaml
wird spaeter ergaenzt. Vorerst liefert get_logger einen Standard-Logger,
damit Module bereits `from projekt.common.logging import get_logger`
benutzen koennen.
"""

from __future__ import annotations

import logging


def get_logger(name: str) -> logging.Logger:
    """Einen nach Modul benannten Logger zurueckgeben.

    Konvention im Projekt: `logger = get_logger(__name__)` am Modulkopf.
    """
    return logging.getLogger(name)
