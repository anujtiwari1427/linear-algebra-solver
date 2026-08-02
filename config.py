import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'linear-algebra-solver-secret-key-2026')
    DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() in ['true', '1', 't']
    JSON_SORT_KEYS = False
