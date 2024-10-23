"""
Projet: exemple avec logging
Module: module1.py

Un premier module au sein de notre paquet exemple.
"""

import logging

from .exceptions import ExempleException

# Créer un logger pour ce module
logger = logging.getLogger(__name__)


def fonction_module1():
    logger.info("Exécution de fonction_module1")

    # Exemple d'une tâche spécifique
    try:
        logger.debug("Tâche dans module1")
    except ExempleException:
        logger.error("Erreur dans fonction_module1")
