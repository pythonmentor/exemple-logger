"""
Projet: exemple avec logging
Module: config.py

L'objectif de cet exemple est de montrer une configuration avancée de
logging dans une application multi-modules.
"""

import logging
import logging.config

# Dictionnaire de configuration
# pour le logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "default",
            "filename": "logs/exemple.log",
        },
        "console": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "default",
        },
    },
    "loggers": {
        "": {  # Logger racine
            "level": "DEBUG",
            "handlers": ["file", "console"],
        },
        "exemple": {
            "level": "DEBUG",
            "handlers": ["file", "console"],
            "propagate": False,
        },
    },
}

# Charger la configuration
logging.config.dictConfig(LOGGING)
