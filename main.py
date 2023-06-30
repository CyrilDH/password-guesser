from flask import Flask, render_template, request
from GenerateurMotsDePasse import GenerateurMotsDePasse

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        date_naissance = request.form.get('date_naissance')
        ville = request.form.get('ville')
        caracteres_speciaux = 'caracteres_speciaux' in request.form
        nbr_permutation = request.form.get('nbr_permutation')

        donnees = {
            'nom': nom,
            'prenom': prenom,
            'date_naissance': date_naissance,
            'ville': ville,
            'caracteres_speciaux': caracteres_speciaux,
            'nbr_permutation': nbr_permutation
        }
        generateur = GenerateurMotsDePasse()
        mots_de_passe = generateur.generate_mots_de_passe(donnees)

        return render_template('resultats.html', mots_de_passe=mots_de_passe)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
