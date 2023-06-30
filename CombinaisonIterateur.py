import string
from itertools import product
from MotHandler import MotHandler


class CombinaisonIterateur:
    @staticmethod
    def iterate(informations, caracteres_speciaux):
        mots_de_passe = []
        for info in informations:
            mots_casse = MotHandler.alterner_casse(info)
            options = []

            if caracteres_speciaux:
                options.extend(list(string.punctuation))

            if options:
                for mot in mots_casse:
                    for combinaison in product([mot], options, repeat=len(mot)):
                        mots_de_passe.append(''.join(combinaison))
            else:
                mots_de_passe.extend(mots_casse)

        return mots_de_passe
