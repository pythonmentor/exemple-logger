"""
Projet: exemple avec logging
Module: __main__.py (point d'entrée principal)

Ce module est le point d'entrée principal de l'application. C'est ici
démarre l'exécution du programme.
"""

import logging

from .cli import main

logger = logging.getLogger(__name__)

logger.info("Exécution du point d'entrée principal: main()")

main()
