import datagen
import anagramdgen

class UsernameGenerator(anagramdgen.AnagramDataGenerator):
    """ Programme de generation de nom d'utilisateur
    """


    def __init__(self, alphabet="1", dataset=["OK"], outtype=str, isupper=False, iscamelcase=False):
        """ Construteur de generateur  de nom d'utilisateur
        """
        super().__init__(alphabet=alphabet, dataset=dataset, outtype=outtype, isupper=isupper, iscamelcase=iscamelcase);

        # on cree un generateur de numero
        self._numgen = datagen.DataGenerator(alphabet="0123456789");

        # on definit le nombre de chiffres
        self._digit_count = 3;



    def setDigitCount(self, value):
        if value >= 0:
            self._digit_count = value;



    def __call__(self, count1=None, count2=None, nullable=False):
        """ Algorithme de generation de nom d'utilisateur
        """
        # si le nombre de donnees a generees
        if count1 is None:
            count1 = self._default_count;
        
        # si le nombre de donnees a generees
        if count1 is None:
            count1 = self._default_count;


        # on genere un mot avec le super generateur
        word = super().__call__(count=count1, nullable=nullable);

        # si le nombre de chiffre specifie en argument est None, alors
        # on utilise le nombre de chiffres par defaut du generateur
        if count2 is None:
            count2 = self._digit_count;

        # si le mot n'est pas null, alors
        # on genere un numero
        if word is not None:
            num = self._numgen(count2);
            word = "{}{}".format(word, num);

            # on retourne 
            return word;

        else:
            # sinon,
            # on retourne None
            return None;




# if __name__=='__main__':
#     ug = UsernameGenerator();
#     ug.nullable = True;
#     print(ug());

