
import random

class DataGenerator(object):
    """ Generateur de donnees
    """

    def __init__(self, alphabet=None, dataset=None):
        # super(DataGenerator).__init__(self);
        
        # INITIALISATION DU GENERATEUR
        # ============================
        #
        # on definit un alphabet OU on definit base de donnees
        # si aucun des deux n'est definit, alors on leve une 
        # exception de type ValueError
        self._alphabet = alphabet;
        self._dataset  = dataset;

        # si aucun des deux n'est definit, alors 
        # on leve l'exception
        if (self._alphabet is None or self._alphabet == '') \
            and (self._dataset is None or len(self._dataset) == 0):
            raise ValueError("`alphabet` or `dataset` is not defined !");




    def __call__(self, count=8):
        """ Algorithme de generation de jeux de donnees aleatoire
        """

        # on verifie si c'est la dataset qui est definit, ou
        # si c'est l'alphabet qui est definit.
        # si c'est la dataset est definit, alors 
        # on selectionne `count` unites de donnees de facon aleatoire
        # sinon, si c'est l'alphabet qui est definit, alors
        # on genere `count` caracteres de facon aleatoire.
        
        if self._dataset is not None:
            # si `count` >= 0 alors,
            # on releve des echantillon de `count` donnees
            if count >= 0:
                return self.__get_rand_values(self._dataset, count);
            
            else:
                # sinon,
                # on leve une exception de type ValueError
                raise ValueError("`count` value must be greate than {0}.");

        
        elif self._alphabet is not None:
            # si l'alphabet est une liste, alors
            # on releve des echantillon de k caracteres qu'on retourne
            # sous forme de chaine de caracteres
            if type(self._alphabet) is list:
                return ''.join(self.__get_rand_values(self._alphabet, count));
            
            elif type(self._alphabet) is str:
                # sinon, si l'alphabet est une chaine de caracteres, alors
                # on eclate cette chaine en un tableau de caracteres, avant
                # de composer la valeur
                return ''.join(self.__get_rand_values([c for c in self._alphabet], count));
    



    def __get_rand_values(self, dataset, k):
        """ Programme qui permet de faire le choix aleatoire 
            de `count` elements d'une liste `dataset` de `n` elements.
        """
        selected_elems = [];

        # on calcule le nombre d'element
        n = len(dataset);

        # pour i allant de 0 a count - 1
        # on choisi un nombre `number` au hasard entre 0 et `len(dataset)`
        # et on ajoute l'element numero `number` dans la liste des elements
        # selectionnes
        for i in range(k):
            number = random.randrange(n);
            data   = dataset[number];
            selected_elems.append(data);


        # on retourne les elements selectionnes
        return selected_elems;







        

