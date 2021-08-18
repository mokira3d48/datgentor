import datagen as dtg
import random


class AnagramDataGenerator(dtg.DataGenerator):
    """ Programme de generation de mots avec des silabes
        coherantes de facon aleatoire
    """


    def __init__(self, alphabet="1", dataset=["OK"], outtype=str, isupper=False, iscamelcase=False):
        """ Constructeur du generateur d'anagrammes
        """
        super().__init__(alphabet=alphabet, dataset=dataset, outtype=outtype);

        # on cree deux generateurs :
        # un generateur de voyelles
        # et un generateur de consonnes
        self._gen1 = dtg.DataGenerator(alphabet="BCDFGHJKLMNPQRSTVWXZ");
        self._gen2 = dtg.DataGenerator(alphabet="bcdfghjklmnpqrstvwxz");
        self._gen3 = dtg.DataGenerator(alphabet="AEIOUY");
        self._gen4 = dtg.DataGenerator(alphabet="aeiouy");

        # on prend les paramettres suplementaires
        self._iscamelcase = iscamelcase;
        self._isupper = isupper;



    def __call__(self, count=None, nullable=False):
        """ Algorithme de generation de jeux de donnees aleatoire
        """
        # on definit la donnee textuelle a generer
        word = "";

        # on genere un element avec le super generateur
        x = super().__call__(count=count, nullable=nullable);

        # si le super generateur n'a pas generer une valeur nulle, alors
        # si on doit generer rien que des lettres majuscules, alors
        # pour chaque tour de boucle
        if x is not None:
            congen = None;
            voygen = None;

            if self._isupper:
                congen = self._gen1;
                voygen = self._gen3;

            else:
                # sinon,
                # prend les deux autres generateurs restants
                congen = self._gen2;
                voygen = self._gen4;

            # on fait le choix aleatoire de commencer par un consorne
            # ou une voyelle
            choice = random.choice(['c', 'v']);

            for i in range(count):
                # on utilise les generateurs 2 et 4
                # si on commence par un consorne, alors
                # on utilise le generateur numeros 2
                if choice == 'c':
                    word = f"{word}{congen(1)}{voygen(1)}";

                else:
                    # sinon
                    # on utilise le generateur 4
                    word = f"{word}{voygen(1)}{congen(1)}";
            
            # une fois les donnees sont generees,
            # si les mots generes doivent etre en CamelCase, alors
            # on transforme les donnees avec la fonction capitalize()
            if self._iscamelcase:
                return word.capitalize();
            else:
                return word;
        
        else:
            # sinon,
            # la donnee generee par le super generateur est Null
            # on retourne None
            return None;






# if __name__ == '__main__':
#     gen = AnagramDataGenerator( isupper=True);
#     print(gen(4));


