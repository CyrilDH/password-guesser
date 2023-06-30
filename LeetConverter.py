import random


class LeetConverter:
    @staticmethod
    def convertir_en_leet(chaine):
        substitutions = {
            'a': '4',
            'e': '3',
            'i': '1',
            'o': '0',
            's': '5',
            't': '7',
        }
        chaine_leet = ''.join(
            substitutions[c] if c in substitutions and random.choice([True, False]) else c for c in chaine.lower())

        return chaine_leet
