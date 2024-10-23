"""
Projet: exemple avec logging
Module: cli.py

Le module "Key" implémente une fonction "main" pour l'exécution dans le
terminal.
"""

import logging

from .exceptions import ExempleException
from . import module1
from . import module2

logger = logging.getLogger(__name__)


def main():
    """Point d'entrée principal de l'application."""
    logger.info("L'application démarre")

    try:
        logger.debug("Exécution du code dans main")
        module1.fonction_module1()
        module2.fonction_module2()
    except ExempleException:
        logger.error("Une erreur est survenue", exc_info=True)
