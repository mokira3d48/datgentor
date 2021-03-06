import datagen
import anagramdgen


class NameGenerator(anagramdgen.AnagramDataGenerator):
    """ Generateur de nom
    """


    def __init__(self, alphabet="1", dataset=["OK"], outtype=str, isupper=False):
        """ Construteur de generateur de nom
        """
        super().__init__(alphabet=alphabet, dataset=dataset, outtype=outtype, isupper=isupper, iscamelcase=True);



    def __call__(self, count=None, nullable=False):
        """ Algorithme de generation de nom
        """
        # si le nombre de donnees a generees
        if count is None:
            count = self._default_count;

        # on genere un mot avec le super generateur
        return super().__call__(count=count, nullable=nullable);





# if __name__=='__main__':
#     ug = NameGenerator();
#     ug.nullable = True;
#     print(ug());









