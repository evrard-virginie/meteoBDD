# Sauvegarde de la base de données
# utilistaion de pg_dump et pg_dumpall car ils sont complémentaires
# pg_dump -> tables, champs, séquences, etc
# pg_dumpall -> backup intégral de l'instance, y compris les users

# Options :
# -h : hostname          -p : port
# -d : database          -U : user

# -f : fichier de sortie                                    -z : niveau de compression (5 par défaut)
# -F : précision du format de sortie                        -a : datas sans la structure
#   c : custom (binaire)                                    -n : préciser un schéma particulier
#   d : directory (permet la parallélisation)               -N : préciser un schéma à exclure
#   t : tar                                                 -c : inclure le create database
#   p : plain text (format sql visible directement)

# -j : parallélisation

# ##### simple export d'une database
# pg_dump base_de_donnees > dumps_base_de_donnees.sql
# ##### ou
# pg_dump -f dump_base_de_donnees.sql -d base_de_donnees
# ##### compression avec le pipe
# pg_dump base_de_donnees | gzip -c > dump.base_de_donnees.sql.gz
# ##### en mode custom (binaire)
# pg_dump -Fc base_de_donnees -f dump_base_de_donnees_fc.dmp
# ##### séparation des datas et de la structure
# pg_dump -Fc base_de_donnees --datas-only -f dump_base_de_donnees_fc.dmp
# pg_dump --schema-only -f dump_base_de_donnees.sql -d base_de_donnees

# Datas
# C:\Program Files\PostgreSQL\13\bin>pg_dump -U dev -W -a -Fp application_meteo_db > C:\Users\Virginie\Envs\meteoBDD\etude\database\backups\nom_de_mon_fichier.dmp

# Structure
# C:\Program Files\PostgreSQL\13\bin>pg_dump -U dev -W --schema-only -Fp application_meteo_db > C:\Users\Virginie\Envs\meteoBDD\etude\database\backups\nom_de_mon_fichier.sql