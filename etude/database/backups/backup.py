# Lancer le programme : Run -> backup OU Terminal C:\Users\...\backups> python backup.py
import psycopg2
from psycopg2 import errors
import os
from config import config  # a partir du fichier de configuration importer la fonction de configuration (config.py)
from datetime import date
import subprocess

# Connexion au serveur de la bdd PostgreSQL
def connect():
    connection = None   # None = ne retourne aucune valeur

    try:
        # récupère les paramètres de connexion
        params = config()

        print('Connexion a la base de donnees Postgresql ..')

        # double astérisque(quarks) permet d'extraire tout les paramètres d'un dictionnaire.
        # le dictionnaire db du fichier config.py qui stocke les paramètres de connexion
        # ça permet la connexion en utilisant le module de psycopg2
        connection = psycopg2.connect(**params)

        # creer un curseur pour écouter les requetes
        cur = connection.cursor()
        print('Version de la base de données PostgreSQL : ')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()   # fetchone = 1 résultat
        print(db_version)

        # connaître la date de la sauvegarde
        date_backup = date.today()
        # transforme la date en string pour pouvoir l'afficher avec le nom du fichier, et les tirets en points
        str_date_backup = str(date_backup).replace('-',('.'))

        # Chemin d'entrée et de sortie
        BACKUP_DIR = "C:\\Users\\Virginie\\Envs\\meteoBDD\\etude\\database\\backups\\scripts_backups\\"
        path_input = "C:\\Program Files\\PostgreSQL\\13\\bin"

        # Configuration spécifique pour Windows
        os.chdir(path_input)
        # os.putenv('PGPASSWORD', PGPASSWORD)
        # os.environ["password"] = password
        print("Répertoire de travail redéfinit : " + os.getcwd())

        # Options :
        # -h : hostname          -p : port      -W : password
        # -d : database          -U : user

        filename = str_date_backup + "_backup.dmp"
        dump = ".\pg_dump -U dev -W -a -Fp application_meteo_db"
        # command =  "> " + dump + " > " + BACKUP_DIR + filename
        command = "{0}> pg_dump -U dev -W -a -Fp application_meteo_db {1} > {2}".format(path_input, BACKUP_DIR, filename)

        # r'C:\Users\Virginie\Envs\meteoBDD\etude\database\backups\scripts_backups' + '\\' + str_date_backup + '_backup_data_bdd.dmp'

        # subprocess.call(command, shell=True)

        print(command)
        os.system(command)

        # fermer le curseur
        cur.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            # fermer toutes les connexions
            connection.close()
            print('Connexion à la base de données terminée')

if __name__ == "__main__":
    connect()



