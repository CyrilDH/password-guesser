from datetime import datetime
from MelangeurLettres import MelangeurLettres
from CombinaisonIterateur import CombinaisonIterateur
from DateHandler import DateHandler
from LeetConverter import LeetConverter

import random


class GenerateurMotsDePasse:

    def __init__(self, donnees):
        self.donnees = donnees
        self.formats_date = []
        self.toutes_informations_melangees = ""
        self.toutes_informations_melangees_leet = ""
        self.iterateur = None

    def _init_date(self):
        if self.donnees['date_naissance']:
            date_naissance_obj = datetime.strptime(self.donnees['date_naissance'], '%Y-%m-%d')
            self.formats_date = DateHandler.relater_date(date_naissance_obj)

    def _init_informations(self):
        informations = [self.donnees['nom'], self.donnees['prenom']]
        if self.donnees['ville']:
            informations.append(self.donnees['ville'])
        toutes_informations = ''.join(informations)
        self.toutes_informations_melangees = ''.join(random.sample(toutes_informations, len(toutes_informations)))
        self.toutes_informations_melangees_leet = LeetConverter.convertir_en_leet(self.toutes_informations_melangees)

    def generate_mots_de_passe(self):
        self._init_date()
        self._init_informations()
        iterateur = CombinaisonIterateur([self.toutes_informations_melangees, self.toutes_informations_melangees_leet], self.donnees['caracteres_speciaux'], self.donnees)

        mots_de_passe = list(iterateur.iterate())

        mots_de_passe_melanges = []
        if self.formats_date:
            mots_de_passe_melanges = [
                MelangeurLettres(mot_de_passe, self.formats_date, self.donnees['caracteres_speciaux'],
                                 self.donnees['nbr_permutation']).melanger() for mot_de_passe in mots_de_passe]

        return mots_de_passe_melanges + mots_de_passe
