"""
Projet: exemple avec logging
Module: module2.py

Un second module au sein de notre paquet exemple.
"""

import logging

from .exceptions import ExempleException

# Créer un logger pour ce module
logger = logging.getLogger(__name__)


def fonction_module2():
    logger.info("Exécution de fonction_module2")

    # Exemple d'une tâche spécifique
    try:
        logger.debug("Tâche dans module2")
        raise ExempleException("Erreur dans module2")
    except ExempleException:
        logger.error("Erreur dans fonction_module2")
