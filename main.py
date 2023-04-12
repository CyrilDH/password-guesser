from flask import Flask, render_template, request
import password_guesser

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        date_naissance = request.form.get('date_naissance')
        ville = request.form.get('ville')
        caracteres_speciaux = 'caracteres_speciaux' in request.form
        chiffres = 'chiffres' in request.form

        donnees = {
            'nom': nom,
            'prenom': prenom,
            'date_naissance': date_naissance,
            'ville': ville,
            'caracteres_speciaux': caracteres_speciaux,
            'chiffres': chiffres
        }

        mots_de_passe = password_guesser.generate_mots_de_passe(donnees)

        return render_template('resultats.html', mots_de_passe=mots_de_passe)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
