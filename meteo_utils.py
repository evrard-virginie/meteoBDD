import meteo
from meteo_common import *


def construire_affichage_prevision_temperature(ville, description, type_temperature):
    """
    Construit en mémoire un dictionnaire qui contient les données prévisionnelles de températures formatées en décimales
    -> cela permet un affichage basé sur le parcours du dictionnaire
    :param ville: ville sur laquelle porte la demande
    :param description:
    :param type_temperature:
    :return: le dictionnaire qui contient les prévisions demandées pour la construction de l'affichage utilisateur
    """
    previsions = {}

    previsions['description'] = description
    previsions['j1'] = "{:.1f}".format(meteo.get_temperature_prevision(ville, type_temperature, PREVISION_J_PLUS_1))
    previsions['j2'] = "{:.1f}".format(meteo.get_temperature_prevision(ville, type_temperature, PREVISION_J_PLUS_2))
    previsions['j3'] = "{:.1f}".format(meteo.get_temperature_prevision(ville, type_temperature, PREVISION_J_PLUS_3))
    previsions['j4'] = "{:.1f}".format(meteo.get_temperature_prevision(ville, type_temperature, PREVISION_J_PLUS_4))
    previsions['j5'] = "{:.1f}".format(meteo.get_temperature_prevision(ville, type_temperature, PREVISION_J_PLUS_5))
    previsions['j6'] = "{:.1f}".format(meteo.get_temperature_prevision(ville, type_temperature, PREVISION_J_PLUS_6))
    previsions['j7'] = "{:.1f}".format(meteo.get_temperature_prevision(ville, type_temperature, PREVISION_J_PLUS_7))

    return previsions


def construire_affichage_prevision_pression_athmospherique(ville):
    """
    Construit en mémoire un dictionnaire qui contient les données prévisionnelles athmosphériques formatées avec
    l'unité de mesure de pression (hPa)
    -> cela permet un affichage basé sur le parcours du dictionnaire
    :param ville: ville sur laquelle porte la demande
    :return: le dictionnaire qui contient les prévisions demandées pour la construction de l'affichage utilisateur
    """
    previsions = {}

    previsions['description'] = "Pression athm."
    previsions['j1'] = str(meteo.get_pression_athmospherique_prevision(ville, PREVISION_J_PLUS_1)) + " hPa"
    previsions['j2'] = str(meteo.get_pression_athmospherique_prevision(ville, PREVISION_J_PLUS_2)) + " hPa"
    previsions['j3'] = str(meteo.get_pression_athmospherique_prevision(ville, PREVISION_J_PLUS_3)) + " hPa"
    previsions['j4'] = str(meteo.get_pression_athmospherique_prevision(ville, PREVISION_J_PLUS_4)) + " hPa"
    previsions['j5'] = str(meteo.get_pression_athmospherique_prevision(ville, PREVISION_J_PLUS_5)) + " hPa"
    previsions['j6'] = str(meteo.get_pression_athmospherique_prevision(ville, PREVISION_J_PLUS_6)) + " hPa"
    previsions['j7'] = str(meteo.get_pression_athmospherique_prevision(ville, PREVISION_J_PLUS_7)) + " hPa"

    return previsions


def construire_affichage_prevision_avis_meteo_detaille(ville):
    """
    Construit en mémoire un dictionnaire qui contient l'avis météo détaillé prévisionnelle
    -> cela permet un affichage basé sur le parcours du dictionnaire
    :param ville: ville sur laquelle porte la demande
    :return: le dictionnaire qui contient les prévisions demandées pour la construction de l'affichage utilisateur
    """
    previsions = {}

    previsions['description'] = "Prévision"
    previsions['j1'] = meteo.get_avis_meteo_detaille_prevision(ville, PREVISION_J_PLUS_1)
    previsions['j2'] = meteo.get_avis_meteo_detaille_prevision(ville, PREVISION_J_PLUS_2)
    previsions['j3'] = meteo.get_avis_meteo_detaille_prevision(ville, PREVISION_J_PLUS_3)
    previsions['j4'] = meteo.get_avis_meteo_detaille_prevision(ville, PREVISION_J_PLUS_4)
    previsions['j5'] = meteo.get_avis_meteo_detaille_prevision(ville, PREVISION_J_PLUS_5)
    previsions['j6'] = meteo.get_avis_meteo_detaille_prevision(ville, PREVISION_J_PLUS_6)
    previsions['j7'] = meteo.get_avis_meteo_detaille_prevision(ville, PREVISION_J_PLUS_7)

    return previsions


def construire_affichage_prevision_humidite(ville):
    """
    Construit en mémoire un dictionnaire qui contient les prévisions d'humidité
    -> cela permet un affichage basé sur le parcours du dictionnaire
    :param ville: ville sur laquelle porte la demande
    :return: le dictionnaire qui contient les prévisions demandées pour la construction de l'affichage utilisateur
    """
    previsions = {}

    previsions['description'] = "Humidité"
    previsions['j1'] = str(meteo.get_humidite_prevision(ville, PREVISION_J_PLUS_1)) + "%"
    previsions['j2'] = str(meteo.get_humidite_prevision(ville, PREVISION_J_PLUS_2)) + "%"
    previsions['j3'] = str(meteo.get_humidite_prevision(ville, PREVISION_J_PLUS_3)) + "%"
    previsions['j4'] = str(meteo.get_humidite_prevision(ville, PREVISION_J_PLUS_4)) + "%"
    previsions['j5'] = str(meteo.get_humidite_prevision(ville, PREVISION_J_PLUS_5)) + "%"
    previsions['j6'] = str(meteo.get_humidite_prevision(ville, PREVISION_J_PLUS_6)) + "%"
    previsions['j7'] = str(meteo.get_humidite_prevision(ville, PREVISION_J_PLUS_7)) + "%"

    return previsions


def construire_affichage_prevision_vent_vitesse(ville):
    """
    Construit en mémoire un dictionnaire qui contient les prévisions de la vitesse du vent avec précision de l'unité
    -> cela permet un affichage basé sur le parcours du dictionnaire
    :param ville: ville sur laquelle porte la demande
    :return: le dictionnaire qui contient les prévisions demandées pour la construction de l'affichage utilisateur
    """
    previsions = {}

    previsions['description'] = "Vent (vitesse)"
    previsions['j1'] = "{:.1f}".format(meteo.get_vent_vitesse_prevision(ville, PREVISION_J_PLUS_1)) + " km/h"
    previsions['j2'] = "{:.1f}".format(meteo.get_vent_vitesse_prevision(ville, PREVISION_J_PLUS_2)) + " km/h"
    previsions['j3'] = "{:.1f}".format(meteo.get_vent_vitesse_prevision(ville, PREVISION_J_PLUS_3)) + " km/h"
    previsions['j4'] = "{:.1f}".format(meteo.get_vent_vitesse_prevision(ville, PREVISION_J_PLUS_4)) + " km/h"
    previsions['j5'] = "{:.1f}".format(meteo.get_vent_vitesse_prevision(ville, PREVISION_J_PLUS_5)) + " km/h"
    previsions['j6'] = "{:.1f}".format(meteo.get_vent_vitesse_prevision(ville, PREVISION_J_PLUS_6)) + " km/h"
    previsions['j7'] = "{:.1f}".format(meteo.get_vent_vitesse_prevision(ville, PREVISION_J_PLUS_7)) + " km/h"

    return previsions


def construire_affichage_prevision_vent_orientation(ville):
    """
    Construit en mémoire un dictionnaire qui contient les prévisions de l'orientation du vent avec précision de l'unité
    -> cela permet un affichage basé sur le parcours du dictionnaire
    :param ville: ville sur laquelle porte la demande
    :return: le dictionnaire qui contient les prévisions demandées pour la construction de l'affichage utilisateur
    """
    previsions = {}

    previsions['description'] = "Vent (direction)"
    previsions['j1'] = str(meteo.get_vent_orientation_prevision(ville, PREVISION_J_PLUS_1)) + "°"
    previsions['j2'] = str(meteo.get_vent_orientation_prevision(ville, PREVISION_J_PLUS_2)) + "°"
    previsions['j3'] = str(meteo.get_vent_orientation_prevision(ville, PREVISION_J_PLUS_3)) + "°"
    previsions['j4'] = str(meteo.get_vent_orientation_prevision(ville, PREVISION_J_PLUS_4)) + "°"
    previsions['j5'] = str(meteo.get_vent_orientation_prevision(ville, PREVISION_J_PLUS_5)) + "°"
    previsions['j6'] = str(meteo.get_vent_orientation_prevision(ville, PREVISION_J_PLUS_6)) + "°"
    previsions['j7'] = str(meteo.get_vent_orientation_prevision(ville, PREVISION_J_PLUS_7)) + "°"

    return previsions

def get_statut_meteo(avis_meteo_actuel):
    """
    Renvoi la valeur de la constante représentant le statut applicatif de l'avis météo actuel (constante),
    si l'avis météo n'est pas reconnu,
    alors une exception est levée (ValueError)
    :param avis_meteo_actuel: l'avis météo actuel
    :return: la valeur de la constante représentant le statut applicatif de l'avis météo actuel
    """
    if avis_meteo_actuel == STATUT_API_NUAGEUX:
        return STATUT_IMAGE_METEO_NUAGEUX
    elif avis_meteo_actuel == STATUT_API_PEU_NUAGEUX:
        return STATUT_IMAGE_METEO_ECLAIRCIES
    elif avis_meteo_actuel == STATUT_API_PARTIELLEMENT_NUAGEUX:
        return STATUT_IMAGE_METEO_ECLAIRCIES
    elif avis_meteo_actuel == STATUT_API_CIEL_DEGAGE:
        return STATUT_IMAGE_METEO_SOLEIL
    elif avis_meteo_actuel == STATUT_API_LEGERE_PLUIE:
        return STATUT_IMAGE_METEO_PLUIE
    elif avis_meteo_actuel == STATUT_API_LEGERE_COUVERT:
        return STATUT_IMAGE_METEO_NUAGEUX
    elif avis_meteo_actuel == STATUT_API_BRUME:
        return STATUT_IMAGE_METEO_NUAGEUX
    else:
        raise ValueError("l'image pour la prévision actuelle n'est pas configurée, pensez à mettre à jour le code")

def get_texte_meteo_file_name(value):
    if value == STATUT_IMAGE_METEO_NEIGE:
        return "neige.txt"
    elif value == STATUT_IMAGE_METEO_ORAGE:
        return "orage.txt"
    elif value == STATUT_IMAGE_METEO_PLUIE:
        return "pluie.txt"
    elif value == STATUT_IMAGE_METEO_SOLEIL:
        return "soleil.txt"
    elif value == STATUT_IMAGE_METEO_NUAGEUX:
        return "nuageux.txt"
    elif value == STATUT_IMAGE_METEO_ECLAIRCIES:
        return "eclaircies.txt"
    else:
        raise ValueError("l'image pour la prévision actuelle n'est pas configurée, pensez à mettre à jour le code")

def get_image_meteo_file_name(value):
    if value == STATUT_IMAGE_METEO_NEIGE:
        return "neige.png"
    elif value == STATUT_IMAGE_METEO_ORAGE:
        return "orage.png"
    elif value == STATUT_IMAGE_METEO_PLUIE:
        return "pluie.png"
    elif value == STATUT_IMAGE_METEO_SOLEIL:
        return "soleil.png"
    elif value == STATUT_IMAGE_METEO_NUAGEUX:
        return "nuageux.png"
    elif value == STATUT_IMAGE_METEO_ECLAIRCIES:
        return "eclaircies.png"
    else:
        raise ValueError("l'image pour la prévision actuelle n'est pas configurée, pensez à mettre à jour le code")

def usage():
    """
    Afficher les informations permettant l'utilisation du programme en ligne de commande
    """
    print("Voici les options possibles (mettre la liste des options : ")
    print("\t-h ou --help : affichage de ce menu")
    print("\t-s ou --search : affiche la liste des villes trouvées et leur identifiants (vous devez spécifier le nom "
          "de la ville recherchée après l'option")
    print("\t-i ou --interactive : permet l'exécution classique du programme en mode interactif avec l'utilisateur")
    print("\t-d ou --display : affiche la météo de la ville passée en paramètre après l'option (utiliser des doubles "
          "quotes si il existe des espaces dans le nom de la ville)")
    print("\t-e ou --export : export la météo de la ville passée en paramètre après l'option (au format html)")
    print("")
