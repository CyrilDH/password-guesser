from itertools import permutations


class MotHandler:
    def __init__(self, mot):
        self.mot = mot

    def alterner_casse(self):
        mots_alternees = []
        for i in range(len(self.mot)):
            mot_liste = list(self.mot.lower())
            mot_liste[i] = self.mot[i].upper()
            mots_alternees.append(''.join(mot_liste))

        return mots_alternees

    def inverser_mot(self):
        return self.mot[::-1]

    def generer_permutations(self):
        return [''.join(p) for p in permutations(self.mot)]
