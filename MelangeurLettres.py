import hashlib
import string
import random


class MelangeurLettres:
    def __init__(self, mot, formats_date, caracteres_speciaux, nb_permutations):
        self.mot = mot
        self.formats_date = formats_date
        self.caracteres_speciaux = caracteres_speciaux
        self.nb_permutations = nb_permutations
        self.caracteres_speciaux_liste = list(string.punctuation) if caracteres_speciaux else []

    def melanger(self):
        mots_melanges = []

        for date in self.formats_date:
            for _ in range(int(self.nb_permutations)):
                mot_avec_caracteres_speciaux = self.mot + ''.join(random.choices(self.caracteres_speciaux_liste,
                                                                                 k=random.randint(0,
                                                                                                  len(self.caracteres_speciaux_liste))))
                perm = ''.join(
                    random.sample(mot_avec_caracteres_speciaux + date, len(mot_avec_caracteres_speciaux + date)))
                mots_melanges.append(perm)
        return mots_melanges

    def alterner_casse(self):
        return ''.join(lettre.upper() if i % 2 == 0 else lettre.lower() for i, lettre in enumerate(self.mot))

    def inverser_mot(self):
        return self.mot[::-1]

    def hasher_mot(self):
        return hashlib.sha256(self.mot.encode()).hexdigest()
