import random
import datagen


class IntegerGenerator(datagen.DataGenerator):
    """ Generateur de nombre entier
    """


    def __init__(self, alphabet=None, dataset=None, intervalle=None):
        """ Constructeur d'un generateur de nombre entier
        """
        super().__init__(alphabet=alphabet, dataset=dataset, outtype=int);

        # on difinit l'intervalle dans lequel, on choisi le nombre
        self._intervalle = intervalle;



    def setIntervalle(self, value):
        self._intervalle = value;



    def __check(self):
        # si aucun des deux n'est definit, alors 
        # on leve l'exception
        if (self._alphabet is None or self._alphabet == '') \
                and (self._dataset is None or len(self._dataset) == 0) \
                and (self._intervalle is None or len(self._intervalle) == 0):
            raise ValueError("`alphabet` or `dataset` is not defined !");



    def __call__(self, count=None, nullable=False):
        """ Algorithme de generation de nombre entier
        """
        # number = super().__call__(count=count, nullable=nullable);
        # on verifie si une des entrees de donnees sont renseignees
        self.__check();

        if not nullable:
            nullable = self.nullable;

        if count is None:
            count = self._default_count;

        # si l'intervalle est definit, alors
        # on definit une liste de nombres
        if self._intervalle is not None:
            numbers = [];
            numbers.extend(range(self._intervalle[0], (self._intervalle[1] + 1)));
            numbers.append(None);

            # print(numbers);

            # on fait le tirage d'un nombre
            number = self._generate(numbers, count);

        return number;



    def _generate(self, dataset, count):
        """ Algorithme de generation de donnees
        """

        # si le nombre a generer est supperieur a 1, alors
        # on retourne une liste de resultats
        if count > 1:
            numbers = [];

            for i in range(count):
                numbers.append(random.choice(dataset));

            return numbers;

        else:
            # sinon,
            # on retourne une liste de resultats
            return random.choice(dataset);




if __name__ == '__main__':
    intgen = IntegerGenerator(intervalle=(9, 100));
    intgen.nullable = True;
    intgen.setCount(0);

    print(intgen());


