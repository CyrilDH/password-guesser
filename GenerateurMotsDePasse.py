from datetime import datetime
from MelangeurLettres import MelangeurLettres
from CombinaisonIterateur import CombinaisonIterateur
from DateHandler import DateHandler


class GenerateurMotsDePasse:
    @staticmethod
    def generate_mots_de_passe(donnees):
        print(donnees)
        date_naissance_obj = datetime.strptime(donnees['date_naissance'], '%Y-%m-%d')
        formats_date = DateHandler.relater_date(date_naissance_obj)

        informations = [donnees['nom'], donnees['prenom'], donnees['ville']]

        tous_les_mots_de_passe = []

        for info in informations:
            mots_de_passe = CombinaisonIterateur.iterate([info], donnees['caracteres_speciaux'])
            mots_de_passe_melanges = []
            for mot_de_passe in mots_de_passe:
                mots_de_passe_melanges.extend(
                    MelangeurLettres.melanger(mot_de_passe, formats_date, donnees['caracteres_speciaux'],
                                              donnees['nbr_permutation']))

            tous_les_mots_de_passe.extend(mots_de_passe_melanges)
            tous_les_mots_de_passe.extend(mots_de_passe)

        return tous_les_mots_de_passe
