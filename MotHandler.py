from itertools import permutations


class MotHandler:
    @staticmethod
    def alterner_casse(mot):
        mots_alternees = []
        for i in range(len(mot)):
            mot_liste = list(mot.lower())
            mot_liste[i] = mot[i].upper()
            mots_alternees.append(''.join(mot_liste))

        return mots_alternees

    @staticmethod
    def inverser_mot(mot):
        return mot[::-1]

    @staticmethod
    def generer_permutations(mot):
        return [''.join(p) for p in permutations(mot)]


mot_handler = MotHandler()