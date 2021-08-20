
import random

class DataGenerator(object):
    """ Generateur de donnees
    """

    def __init__(self, alphabet=None, dataset=None, outtype=str):
        super(DataGenerator, self).__init__();
        
        # INITIALISATION DU GENERATEUR
        # ============================
        #
        # on definit un alphabet OU on definit base de donnees
        # si aucun des deux n'est definit, alors on leve une 
        # exception de type ValueError
        self._alphabet = alphabet;
        self._dataset  = dataset;

        # on definit la valeur generee par le generateur
        self.nullable = False;

        # on definit le type de sortie des donnees
        self._outtype = outtype;

        # on definit la longueur par defaut des donnees generees
        self._default_count = 4;

        # on verifie les donnees d'entrees
        # self.__check();
    


    # @property
    # def set_alphabet(self, value):
    #     self._alphabet = value;
    #     self.__check();
    


    # @property
    # def set_dataset(self, value):
    #     self._dataset = value;
    #     self.__check();

    def setAlphabet(self, alphabet):
        self._alphabet = alphabet;
        # self.__check();



    def setDataset(self, dataset):
        self._dataset = dataset;
        # self.__check();



    def setCount(self, value):
        if value >= 0:
            self._default_count = value;




    def __check(self):
        # si aucun des deux n'est definit, alors 
        # on leve l'exception
        if (self._alphabet is None or self._alphabet == '') \
            and (self._dataset is None or len(self._dataset) == 0):
            raise ValueError("`alphabet` or `dataset` is not defined !");



    def __call__(self, count=None, nullable=False):
        """ Algorithme de generation de jeux de donnees aleatoire
        """
        # si la valeur de  `count` n'est pas definie, alors
        # on prend la valeur par defaut
        if count is None:
            count = self._default_count;
        
        # si nullable n'est pas True, alors 
        # on prend la valeur du generateur
        if not nullable:
            nullable = self.nullable;

        # on definit la donnee de sortie
        outdata = None;

        # on verifie si c'est la dataset qui est definit, ou
        # si c'est l'alphabet qui est definit.
        # si c'est la dataset est definit, alors 
        # on selectionne `count` unites de donnees de facon aleatoire
        # sinon, si c'est l'alphabet qui est definit, alors
        # on genere `count` caracteres de facon aleatoire.

        if self._dataset is not None:
            # si `count` >= 0 alors,
            # on releve des echantillon de `count` donnees
            # si `count` = 1, alors on prend directement le premier element
            if count >= 0:
                outdata = self.__get_rand_values(self._dataset, count);
                outdata = outdata if count > 1 else outdata[0];

            else:
                # sinon,
                # on leve une exception de type ValueError
                raise ValueError("`count` value must be greate than {0}.");

        
        elif self._alphabet is not None:
            # si l'alphabet est une liste, alors
            # on releve des echantillon de k caracteres qu'on retourne
            # sous forme de chaine de caracteres
            if type(self._alphabet) is list:
                outdata = self.__format_to_outtype(''.join(self.__get_rand_values(self._alphabet, count)));

            elif type(self._alphabet) is str:
                # sinon, si l'alphabet est une chaine de caracteres, alors
                # on eclate cette chaine en un tableau de caracteres, avant
                # de composer la valeur
                outdata = self.__format_to_outtype(''.join(self.__get_rand_values([c for c in self._alphabet], count)));
        
        # si le resultat de sortie peut etre Null, alors
        # on fait un choix binaire et aleatoire entre le resultat et
        # la valeur Null
        if nullable:
            return random.choice([outdata, None]);
        else:
            # dans le cas contraire,alors
            # on retourne directement le resultat
            return outdata;
    



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
    


    def __format_to_outtype(self, data):
        """ Programme de formatage des donnees generees dans le type
            de sortie
        """
        # si la donnee generee n'est pas de type sequentiel, alors
        # on convertie cette derniere dans le type de sortie,
        # si le type de sortie a belle et bien ete specifie
        if type(data) in [int, str]:
            return (self._outtype)(data) if self._outtype is not None else data;








        

