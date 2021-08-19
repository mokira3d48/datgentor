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



    def __call__(self, count1=4, count2=3, nullable=False):
        """ Algorithme de generation de nom d'utilisateur
        """
        # on genere un mot avec le super generateur
        word = super().__call__(count=count1, nullable=nullable);

        # si le mot n'est pas null, alors
        # on genere un numero
        if word is not None:
            num = self._numgen(count2);
            word = f"{word}{num}";

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

