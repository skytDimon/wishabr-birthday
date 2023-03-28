from pyramid.config import Configurator
from main import create_app
import threading
from notify import run_bot


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    #t = threading.Thread(target=run_bot)
    #t.daemon = True
    #t.start()
    return create_app()