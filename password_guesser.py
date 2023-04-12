import random
import string
from datetime import datetime


def relater_date(date):
    formats_date = [
        date.strftime('%d%m%Y'),
        date.strftime('%m%d%Y'),
        date.strftime('%Y%m%d'),
        date.strftime('%Y%d%m')
    ]
    return formats_date


def relater_cause(mot):
    return [mot.lower(), mot.upper(), mot.capitalize()]


def aiter_options(mot, caracteres_speciaux, chiffres):
    if caracteres_speciaux:
        mot += random.choice(string.punctuation)
    if chiffres:
        mot += random.choice(string.digits)
    return mot


def iterate_combinations(informations, caracteres_speciaux, chiffres):
    mots_de_passe = []

    for info in informations:
        mots_casse = relater_cause(info)
        for mot in mots_casse:
            mot_option = aiter_options(mot, caracteres_speciaux, chiffres)
            mots_de_passe.append(mot_option)

    return mots_de_passe


def generate_mots_de_passe(donnees):
    nom, prenom, date_naissance, ville, caracteres_speciaux, chiffres = donnees

    date_naissance_obj = datetime.strptime(donnees['date_naissance'], '%Y-%m-%d')
    formats_date = [
        date_naissance_obj.strftime('%d%m%Y'),
        date_naissance_obj.strftime('%Y%m%d'),
        date_naissance_obj.strftime('%m%d%Y'),
    ]

    informations = [donnees['nom'], donnees['prenom'], donnees['ville']] + formats_date

    mots_de_passe = iterate_combinations(informations, caracteres_speciaux, chiffres)

    return mots_de_passe

