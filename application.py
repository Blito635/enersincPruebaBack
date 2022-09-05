from src.settings import application
from src.scripts.routes import banca

# Aplicaciones
application.register_blueprint(banca)


if __name__ == '__main__':
    application.debug = True
    application.run()
