from datetime import datetime
from MelangeurLettres import MelangeurLettres
from CombinaisonIterateur import CombinaisonIterateur
from DateHandler import DateHandler
from LeetConverter import LeetConverter

import random


class GenerateurMotsDePasse:

    def generate_mots_de_passe(self, donnees):
        if donnees['date_naissance']:
            date_naissance_obj = datetime.strptime(donnees['date_naissance'], '%Y-%m-%d')
            formats_date = DateHandler.relater_date(date_naissance_obj)
        else:
            formats_date = []

        informations = [donnees['nom'], donnees['prenom']]
        if donnees['ville']:
            informations.append(donnees['ville'])
        toutes_informations = ''.join(informations)
        toutes_informations_melangees = ''.join(random.sample(toutes_informations, len(toutes_informations)))
        toutes_informations_melangees_leet = LeetConverter.convertir_en_leet(toutes_informations_melangees)

        mots_de_passe = list(
            CombinaisonIterateur.iterate([toutes_informations_melangees, toutes_informations_melangees_leet],
                                         donnees['caracteres_speciaux']))

        mots_de_passe_melanges = []
        if formats_date: # N'ajoutez des dates que si la liste n'est pas vide
            mots_de_passe_melanges = [MelangeurLettres.melanger(mot_de_passe, formats_date, donnees['caracteres_speciaux'], donnees['nbr_permutation']) for mot_de_passe in mots_de_passe]

        return mots_de_passe_melanges + mots_de_passe
