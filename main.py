import affichage_meteo
import meteo_utils
from meteo_utils import *
import sys
import getopt

if __name__ == '__main__':

    def afficher_meteo_ville(ville):
        # on affiche maintenant les résultats, c'est à dire les infromations météos relatives à la ville choisie par
        # l'utilisateur.
        # pour cela on utilise une fonction d'affichage en premier pour l'entête, qui permet d'obtenir les valeurs
        # nécéssaires en fonction de la ville choisie
        affichage_meteo.afficher_en_tete(ville, meteo.get_temperature_actuelle(ville),
                                         meteo.get_avis_meteo_detaille(ville))

        # l'entête est maintenant affichée pour l'utilisateur, avec les informations météos actuelles sur la ville,
        # mais on souhaite également afficher
        # les prévisions à 7 jours.
        # pour cela on construit une liste qui va stockée les valeurs de prévisions pour les 7 prochains jours
        liste_previsions = []

        liste_previsions.append(construire_affichage_prevision_temperature(ville, "T° jour",
                                                                           PREVISION_TEMPERATURE_JOUR))
        liste_previsions.append(construire_affichage_prevision_temperature(ville, "T° min",
                                                                           PREVISION_TEMPERATURE_MINI))
        liste_previsions.append(construire_affichage_prevision_temperature(ville, "T° max",
                                                                           PREVISION_TEMPERATURE_MAXI))
        liste_previsions.append(construire_affichage_prevision_temperature(ville, "T° mat",
                                                                           PREVISION_TEMPERATURE_MATIN))
        liste_previsions.append(construire_affichage_prevision_temperature(ville, "T° midi",
                                                                           PREVISION_TEMPERATURE_APRES_MIDI))
        liste_previsions.append(construire_affichage_prevision_temperature(ville, "T° nuit",
                                                                           PREVISION_TEMPERATURE_NUIT))
        liste_previsions.append(construire_affichage_prevision_pression_athmospherique(ville))
        liste_previsions.append(construire_affichage_prevision_humidite(ville))
        liste_previsions.append(construire_affichage_prevision_vent_vitesse(ville))
        liste_previsions.append(construire_affichage_prevision_vent_orientation(ville))
        liste_previsions.append(construire_affichage_prevision_avis_meteo_detaille(ville))

        # une fois qu'on a les informations en mémoire (dans la liste) pour les prévisions météo
        # sur les 7 prochains jours,
        # on peut les afficher à l'écran avec un formatage sur les 7 prochains jours
        affichage_meteo.afficher_previsions(liste_previsions)

        # On récupère à présent l'avis météo, c'est une chaîne de caractère.
        # En fonction de sa valeur, on va afficher une image différentes à l'utilisateur
        # image = représentation sous forme de caractères présent dans une fichier
        avis_meteo_actuel = meteo.get_avis_meteo_detaille(ville)
        #obtient l'image correspondante à l'avis météo actuel et l'affiche en mode console
        affichage_meteo.afficher_image_meteo(get_statut_meteo(avis_meteo_actuel))

    try:
        # on récupère les paramètres et options de la ligne de commande (module système de Python : sys)
        # se référer à la documentation de getopt pour commprendre l'usage des paramètres de la fonction.
        # getopt permet de se conformer à un fonctionnement standard des usages en ligne de commande :
        # pour les options courtes, un tiret et une lettre : ex : -o
        # pour les option longues, deux tiret et un motion entier : ex : --option
        # NB : si une erreur survient concernant la gestion des paramètres, getopt déclenche une exception adaptée
        # qu'il suffit d'attraper (de catcher) => voir en bas en fin de fichier
        opts, args = getopt.getopt(sys.argv[1:], 'his:d:e:', ['help', 'interactive', 'search=', 'display=', 'export='])

        for opt, arg in opts:
            if opt in ('-h', '--help'):
                usage()

            elif opt in ('-s', '--search'):
                resultat_villes_trouvees = meteo.recherche_ville(arg)
                for v in resultat_villes_trouvees:
                    print(v)

                print(arg)

            elif opt in ('-d', '--display'):
                afficher_meteo_ville(arg)

            elif opt in ('-e', '--export'):
                avis_meteo_actuel = meteo.get_avis_meteo_detaille(arg)
                meteo_export.export(arg, avis_meteo_actuel)

            elif opt in ('-i', '--interactive'):

                # on définit une variable pour contenir le nom de la ville pour laquelle afficher la météo
                ville_en_cours = ""

                # on affiche l'écran d'accueil qui permet à l'utilisateur de rechercher une ville
                affichage_meteo.afficher_ecran_accueil()

                # on récupère le choix fait par l'utilisateur
                print()
                choix_utilisateur = int(input("Quel est votre choix (1, 2 ou 3) ? "))

                # si l'utilisateur choisit la première proposition de l'écran d'accueil, alors on lui demande
                # de saisir le nom de la ville qu'il recherche (une partie du nom suffit pour lancer la recherche)
                if choix_utilisateur == 1:

                    # on récupère le texte de l'utilisateur saisie à l'écran et on le stock dans la variable choix_ville
                    choix_ville = input("Quelle ville recherchez-vous ? ")
                    # on récupère le résultat de la recherche des villes et on le stock dans la variable liste_ville
                    liste_villes = meteo.recherche_ville(choix_ville)
                    # on vérifie si la recherche à bien renvoyé un résultat (pour ne pas travailler sur des données
                    # inexistantes et générer une erreur technique)
                    if liste_villes == None:
                        print("'_' aucune ville correspondante n'a été trouvée.")
                    else:
                        # si la variable existe mais que le nombre de ville est égale à zéro, on prévient l'utilisateur
                        if len(liste_villes) == 0:
                            print("-_- aucune ville correspondante n'a été trouvée.")
                        else:
                            # construction d'un dictionnaire pour classer les villes et permettre à l'utilisateur
                            # de les sélectionner par un numéro
                            choix_ville_recherche = {}
                            numero_choix = 1
                            for ville in liste_villes:
                                choix_ville_recherche[numero_choix] = ville
                                numero_choix += 1

                            # on affiche maintenant le résultat de la recherche à l'utilisateur pour qu'il puisse
                            # choisir une ville à consulter
                            affichage_meteo.afficher_liste_ville(choix_ville_recherche)

                            # en fonction du choix de l'utilisateur, on récupère la ville choisie.
                            # ici, petite astuce : comme on utilise un dictionnaire avec le nomde de la ville et un
                            # index, le choix de l'utilisateur est en fait l'index du dictionnaire, ce qui permet de
                            # récupérer directement le nom de la ville grâce à l'index...
                            print()
                            ville_en_cours = choix_ville_recherche[int(input(
                                "Pour consulter la météo d'une ville, tapez son numéro dans la liste : "))]
                            print()
                            afficher_meteo_ville(ville_en_cours)


                elif choix_utilisateur == 2:
                    pass
                else:
                    print("Désolé votre choix est incorrect, que voulez-vous choisir 1, 2 ou 3 ?")
    except getopt.GetoptError:
        print("Paramètres incorrects !")
        usage()
        sys.exit(2)

