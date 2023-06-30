from flask import Flask, render_template, request
from GenerateurMotsDePasse import GenerateurMotsDePasse


class MonApplication:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.route('/', methods=['GET', 'POST'])(self.index)

    def index(self):
        if request.method == 'POST':
            nom = request.form.get('nom')
            prenom = request.form.get('prenom')
            date_naissance = request.form.get('date_naissance')
            ville = request.form.get('ville')
            caracteres_speciaux = 'caracteres_speciaux' in request.form
            nbr_permutation = int(request.form.get('nbr_permutation'))
            nbr_mot_de_passe = int(request.form.get('nbr_mot_de_passe'))
            donnees = {
                'nom': nom,
                'prenom': prenom,
                'date_naissance': date_naissance,
                'ville': ville,
                'caracteres_speciaux': caracteres_speciaux,
                'nbr_permutation': nbr_permutation,
                'nbr_mot_de_passe': nbr_mot_de_passe
            }
            generateur = GenerateurMotsDePasse(donnees)
            mots_de_passe = generateur.generate_mots_de_passe()
            return render_template('resultats.html', mots_de_passe=mots_de_passe)

        return render_template('index.html')

    def run(self):
        self.app.run(debug=True)


if __name__ == '__main__':
    MonApplication().run()
