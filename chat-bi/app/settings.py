import os
from dotenv import load_dotenv


def load_environment():
    ENV = os.getenv('ENVIRONMENT', 'development')

    if ENV == 'development':
        load_dotenv(dotenv_path='.env.development')
    elif ENV == 'production':
        load_dotenv(dotenv_path='.env.production')
    else:
        load_dotenv()

    return ENV
