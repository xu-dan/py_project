"""Define the program logging utility"""

import logging
import logging.config
import os

import yaml

LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'brief': {
            'format': '%(message)s'
        },
        'precise': {
            'format': '%(asctime)s %(levelname)-8s %(name)-40s  %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'brief',
            'stream': 'ext://sys.stdout'
        },
        'debug_handler': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'precise',
            'filename': 'debug.log',
            'encoding': 'utf8'
        },
        'rotate_handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'precise',
            'filename': 'project.log',
            'maxBytes': 10485760,
            'backupCount': 10,
            'encoding': 'utf8'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        },
    },
    'root': {
        'level': 'WARN',
        'handlers': ['console']
    }
}


def setup_logging(env_key='LOG_CONFIG'):
    """Setup logging configuration"""
    config, value = None, os.getenv(env_key, None)
    if value:
        path = value
        if os.path.exists(path):
            with open(path, 'rt') as config_file:
                config = yaml.load(config_file.read())

    if not config:
        config = LOG_CONFIG

    logging.config.dictConfig(config)
