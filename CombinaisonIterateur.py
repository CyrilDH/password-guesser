import string
from itertools import product, permutations
from MotHandler import MotHandler
import random


class CombinaisonIterateur:
    @staticmethod
    def iterate(informations, caracteres_speciaux):
        options = list(string.punctuation) if caracteres_speciaux else []
        for info in informations:
            mots_casse = MotHandler.alterner_casse(info)

            if options:
                for mot in mots_casse:
                    for combinaison in product(*([mot] + options), repeat=len(mot)):
                        password = ''.join(combinaison)
                        yield from CombinaisonIterateur.shuffle_password(password)
            else:
                for mot in mots_casse:
                    yield from CombinaisonIterateur.shuffle_password(mot)

    @staticmethod
    def shuffle_password(password):
        password_list = list(password)
        for _ in range(30):  # shuffle 10 times
            random.shuffle(password_list)
            yield ''.join(password_list)
