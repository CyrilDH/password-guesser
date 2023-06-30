import hashlib
import string
import random
from itertools import permutations


class MelangeurLettres:
    @staticmethod
    def melanger(mot, formats_date, caracteres_speciaux, nb_permutations):
        mots_melanges = []
        caracteres_speciaux_liste = list(string.punctuation) if caracteres_speciaux else []

        for date in formats_date:
            for _ in range(int(nb_permutations)):
                mot_avec_caracteres_speciaux = mot + ''.join(random.choice(caracteres_speciaux_liste) for _ in
                                                             range(random.randint(0, len(caracteres_speciaux_liste))))
                perm = ''.join(
                    random.sample(mot_avec_caracteres_speciaux + date, len(mot_avec_caracteres_speciaux + date)))
                mots_melanges.append(perm)
        return mots_melanges

    @staticmethod
    def alterner_casse(mot):
        return ''.join([lettre.upper() if i % 2 == 0 else lettre.lower() for i, lettre in enumerate(mot)])

    @staticmethod
    def inverser_mot(mot):
        return mot[::-1]

    @staticmethod
    def hasher_mot(mot):
        return hashlib.sha256(mot.encode()).hexdigest()


melangeur = MelangeurLettres()
mot_melange = melangeur.melanger('test', ['01-01-2023'], True, 10)