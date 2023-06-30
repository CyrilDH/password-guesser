### CombinaisonIterateur

Ce code génère des combinaisons de mots de passe en utilisant des informations fournies, en alternant la casse des lettres et éventuellement en incluant des caractères spéciaux.

Le code importe les bibliothèques nécessaires, notamment string, itertools, MotHandler et random.

La classe CombinaisonIterateur est définie avec un constructeur __init__ qui initialise les attributs de la classe.

La méthode iterate génère les combinaisons de mots de passe en itérant sur les informations fournies. Elle crée un objet MotHandler pour chaque information et utilise la méthode alterner_casse pour obtenir une liste de mots avec des alternances de casse. Ensuite, si des caractères spéciaux sont spécifiés, le code génère des combinaisons de mots de passe en utilisant la méthode product de itertools et en ajoutant les caractères spéciaux. Sinon, il génère simplement des combinaisons avec les mots obtenus. Les mots de passe sont ensuite mélangés plusieurs fois à l'aide de random.shuffle et renvoyés via la fonction yield.


### GenerateurMotsDePasse

Ce code est un générateur de mots de passe qui utilise différentes informations fournies pour créer des combinaisons de mots de passe. Voici une explication concise du code :

Le code importe les modules nécessaires : datetime, MelangeurLettres, CombinaisonIterateur, DateHandler et LeetConverter. Il importe également le module random.

La classe GenerateurMotsDePasse est définie avec un constructeur __init__ qui initialise les attributs de la classe.

La méthode _init_date est utilisée pour initialiser les formats de date en fonction de la date de naissance fournie dans les données.

La méthode _init_informations est utilisée pour initialiser les informations fournies en les mélangeant aléatoirement et en les convertissant en langage "leet" (si nécessaire).

La méthode generate_mots_de_passe est la principale méthode qui génère les mots de passe. Elle appelle les méthodes _init_date et _init_informations pour préparer les informations. Ensuite, elle crée un objet CombinaisonIterateur en utilisant les informations mélangées et les informations mélangées en langage "leet". Cet itérateur génère les combinaisons de mots de passe en utilisant les informations fournies.

Les mots de passe générés sont stockés dans une liste mots_de_passe.

Si des formats de date sont disponibles, les mots de passe sont ensuite mélangés en utilisant le module MelangeurLettres, en prenant en compte les formats de date, les caractères spéciaux et le nombre de permutations spécifiés.
Dans ce code, on peut voir un exemple de composition entre la classe "GenerateurMotsDePasse" et d'autres classes comme "DateHandler", "LeetConverter", "MelangeurLettres", et "CombinaisonIterateur".

"GenerateurMotsDePasse" utilise ces classes pour effectuer différentes tâches, sans hériter directement d'elles, ce qui est une marque de la composition. Par exemple, "GenerateurMotsDePasse" utilise "DateHandler" pour obtenir une date relative, "LeetConverter" pour convertir les informations en Leet, "MelangeurLettres" pour mélanger les lettres, et "CombinaisonIterateur" pour créer des itérations de combinaisons. Ainsi, la classe "GenerateurMotsDePasse" est composée des fonctionnalités des autres classes, ce qui démontre le principe de composition en programmation orientée objet (POO).

Finalement, la méthode retourne une liste contenant les mots de passe mélangés et les mots de passe non mélangés.

En résumé, ce générateur de mots de passe utilise des informations fournies, les mélange, les convertit en langage "leet" et génère des combinaisons de mots de passe en prenant en compte les formats de date et les caractères spéciaux.

### MelangeurLettres 

Ce code est une classe MelangeurLettres qui effectue différentes opérations sur un mot donné. Voici une explication concise du code :

Le code importe les modules hashlib, string et random.

La classe MelangeurLettres est définie avec un constructeur __init__ qui initialise les attributs de la classe avec les valeurs passées en paramètres.

La méthode melanger génère des permutations mélangées du mot en utilisant les formats de date spécifiés. Elle effectue les étapes suivantes :

Elle crée une liste vide mots_melanges.
Pour chaque format de date dans self.formats_date :
Pour un nombre de permutations spécifié par self.nb_permutations :
Le mot est étendu avec des caractères spéciaux (si spécifiés) en utilisant random.choices pour choisir aléatoirement des caractères spéciaux.
Une permutation est générée en mélangeant les caractères du mot étendu avec les caractères du format de date.
La permutation est ajoutée à la liste mots_melanges.
La méthode retourne la liste mots_melanges.
La méthode alterner_casse retourne une version du mot avec des lettres alternant entre majuscules et minuscules.

La méthode inverser_mot retourne le mot inversé.

La méthode hasher_mot utilise l'algorithme de hachage SHA256 pour hasher le mot et retourne la représentation hexadécimale du hachage.

En résumé, cette classe MelangeurLettres permet de mélanger un mot en générant des permutations avec des caractères spéciaux, en alternant la casse des lettres, en inversant le mot et en le hachant avec SHA256. Elle peut également prendre en compte des formats de date pour générer des permutations mélangées spécifiques.

### MotHandler 

Ce code définit une classe MotHandler qui effectue différentes opérations sur un mot donné. Voici une explication concise du code :

Le code importe le module itertools et la fonction permutations.

La classe MotHandler est définie avec un constructeur __init__ qui initialise l'attribut mot avec la valeur passée en paramètre.

La méthode alterner_casse génère une liste de mots en alternant la casse des lettres du mot initial. Elle effectue les étapes suivantes :

Elle crée une liste vide mots_alternees.
Pour chaque indice i dans la plage de longueur du mot :
Le mot est converti en minuscules et stocké sous forme de liste dans mot_liste.
La lettre à l'indice i dans mot_liste est convertie en majuscule.
Le mot résultant est rejoint pour former une chaîne de caractères et ajouté à la liste mots_alternees.
La méthode retourne la liste mots_alternees.
La méthode inverser_mot retourne le mot inversé.

La méthode generer_permutations génère toutes les permutations possibles du mot en utilisant la fonction permutations de itertools. Elle retourne une liste de toutes les permutations obtenues.

En résumé, cette classe MotHandler permet d'effectuer des opérations sur un mot donné, telles que l'alternance de casse des lettres, l'inversion du mot et la génération de toutes les permutations possibles.

### LeetConverter

Ce code définit une classe LeetConverter qui permet de convertir une chaîne de caractères en langage "leet". Voici une explication concise du code :

Le code importe le module random.

La classe LeetConverter contient une méthode statique convertir_en_leet qui effectue la conversion en langage "leet". Cette méthode prend en paramètre une chaîne de caractères à convertir.

À l'intérieur de la méthode, un dictionnaire substitutions est défini pour spécifier les substitutions de caractères à effectuer. Par exemple, le caractère 'a' est substitué par '4', 'e' par '3', 'i' par '1', etc.

La chaîne de caractères chaine est convertie en minuscules et parcourue caractère par caractère. Pour chaque caractère :

Si le caractère est présent dans le dictionnaire substitutions et qu'un choix aléatoire entre True et False est évalué à True, le caractère est substitué par la valeur correspondante dans le dictionnaire.
Sinon, le caractère est conservé tel quel.
Les caractères convertis et non convertis sont concaténés pour former la chaîne de caractères chaine_leet en langage "leet".

La méthode retourne la chaîne de caractères chaine_leet convertie en langage "leet".

En résumé, cette classe LeetConverter permet de convertir une chaîne de caractères en langage "leet" en appliquant des substitutions aléatoires sur certains caractères spécifiques.

### DateHandler

Ce code définit une classe DateHandler qui contient une méthode statique relater_date. Voici une explication concise du code :

La classe DateHandler contient une seule méthode statique relater_date, qui prend en paramètre un objet date.

La méthode relater_date utilise la méthode strftime de l'objet date pour formater la date selon différents formats. Trois formats de date sont utilisés :

"%Y%m%d" : Format d'année, mois, jour (ex: 20210630).
"%d%m%Y" : Format de jour, mois, année (ex: 30062021).
"%m%d%Y" : Format de mois, jour, année (ex: 06302021).
La méthode retourne une liste contenant les dates formatées selon les trois formats mentionnés.

En résumé, cette classe DateHandler fournit une méthode statique pour formater une date selon différents formats et renvoyer une liste de dates formatées.




