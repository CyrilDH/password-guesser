import string
from itertools import product, permutations
from MotHandler import MotHandler
import random


class CombinaisonIterateur:
    def __init__(self, informations, caracteres_speciaux, donnees):
        self.donnees = donnees
        self.informations = informations
        self.options = list(string.punctuation) if caracteres_speciaux else []

    def iterate(self):
        for info in self.informations:
            mot_handler = MotHandler(info)
            mots_casse = mot_handler.alterner_casse()
            if self.options:
                for mot in mots_casse:
                    for combinaison in product(*([mot] + self.options), repeat=len(mot)):
                        password = ''.join(combinaison)
                        yield from self.shuffle_password(password)
            else:
                for mot in mots_casse:
                    yield from self.shuffle_password(mot)

    def shuffle_password(self, password):
        print(self.donnees['nbr_mot_de_passe'])
        password_list = list(password)
        for _ in range(self.donnees['nbr_mot_de_passe']):  # shuffle 10 times
            random.shuffle(password_list)
            yield ''.join(password_list)
