### 1. Polymorphisme:
Le polymorphisme est un principe en POO qui permet à un objet d'agir de différentes manières en fonction de son type ou de sa classe. Par exemple, vous pouvez avoir une méthode dans une classe qui se comportera différemment dans une classe dérivée.

### 2. Encapsulation:
L'encapsulation est un principe de la POO qui cache les détails internes d'une classe et expose seulement ce qui est nécessaire. Cela est généralement accompli en utilisant des méthodes privées (qui ne peuvent être accédées que depuis l'intérieur de la classe) et des accesseurs (méthodes qui permettent d'accéder aux attributs privés d'une classe).
[GenerateurMotsDePasse.py](GenerateurMotsDePasse.py)
Les méthodes et attributs commençant par un underscore (_) comme _init_date et _init_informations sont généralement destinées à être privées, même si Python n'impose pas réellement des restrictions d'accès. Ceci est un exemple d'encapsulation car ces méthodes sont utilisées pour cacher des détails d'implémentation à l'intérieur de la classe 
### 3. Composition:
La composition est un principe de la POO où une classe est utilisée pour construire une autre classe, souvent en l'utilisant comme attribut. Cela permet de créer des relations complexes entre les classes.
[GenerateurMotsDePasse.py](GenerateurMotsDePasse.py)
Ce code utilise des instances d'autres classes comme DateHandler, LeetConverter, CombinaisonIterateur et MelangeurLettres dans la classe GenerateurMotsDePasse. C'est un exemple de composition. Par exemple, un objet DateHandler est utilisé pour convertir une date, et un objet LeetConverter est utilisé pour convertir une chaîne en leet speak.
### 4. Héritage:
L'héritage est un principe de la POO qui permet à une classe d'hériter des attributs et des méthodes d'une autre classe.

### 5. Interface:
Une interface en programmation est un moyen de garantir qu'une classe respecte un certain contrat, c'est-à-dire qu'elle implémente certaines méthodes. Python n'a pas d'interfaces intégrées, mais on peut obtenir un comportement similaire avec des classes abstraites.

### 6. Méthodes et attributs d'objets:
Les méthodes d'objets sont des fonctions qui sont définies à l'intérieur d'une classe et peuvent modifier l'état de l'instance de la classe. Les attributs d'objets sont des variables qui sont également définies à l'intérieur de la classe et sont associées à des instances de la classe.
[GenerateurMotsDePasse.py](GenerateurMotsDePasse.py)
Dans la classe GenerateurMotsDePasse, self.donnees, self.formats_date, self.toutes_informations_melangees et self.toutes_informations_melangees_leet sont des exemples d'attributs d'objet, car ils sont définis avec self et sont accessibles à toutes les méthodes de la classe. Les méthodes comme generate_mots_de_passe sont des exemples de méthodes d'objet.
### 7. Méthodes et attributs statiques:
Les méthodes statiques sont des fonctions qui sont définies à l'intérieur d'une classe et qui ne modifient pas l'état de l'instance de la classe. Les attributs statiques sont des variables qui sont définies à l'intérieur de la classe et qui ne sont pas associées à des instances spécifiques de la classe.
[LeetConverter.py](LeetConverter.py)

### 8. Méthodes et attributs de classe:
Les méthodes de classe sont des méthodes qui sont liées à la classe et non à l'instance de la classe. Elles ne peuvent pas modifier l'état de l'instance, mais peuvent modifier l'état de la classe. Les attributs de classe sont des attributs qui sont partagés par toutes les instances de la classe.