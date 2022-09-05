import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

class Connection:

    def connect(self):

        try:
            connection = psycopg2.connect(
                user=os.getenv("userLocal"),
                password=os.getenv("passwordLocal"),
                host=os.getenv("hostLocal"),
                port=os.getenv("portLocal"),
                database=os.getenv("databaseLocal")
            )
            return connection

        except:
            print("Error en la conexion a la base de datos")

    def closeConnection(self, connection):
        connection.close()
