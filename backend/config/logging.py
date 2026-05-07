from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"

LOG_DIR.mkdir(exist_ok=True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },

    'formatters': {
        'simple': {
            'format': '{levelname} - {asctime:s} - {name} - {message}',
            'style': '{'
        },

        'verbose': {
            'format': '{levelname} - {asctime:s} - {name} - {module}.py - (line {lineno:d}) - {funcName} - {message}',
            'style': '{'
        },
    },

    'handlers': {
        'console': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },

        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': LOG_DIR / 'services.log',
        },
    },

    'loggers': {
        '': {
            'level': 'WARNING',
            'handlers': ['console', 'file'],
        },

        'django': {
            'level': 'INFO',
            'handlers': ['console', 'file'],
            'propagate': False,
        },

        'django.template': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': False,
        },
    },
}
