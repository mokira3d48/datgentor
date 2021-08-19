import datagen
import anagramdgen


class NameGenerator(anagramdgen.AnagramDataGenerator):
    """ Generateur de nom
    """


    def __init__(self, alphabet="1", dataset=["OK"], outtype=str, isupper=False):
        """ Construteur de generateur de nom
        """
        super().__init__(alphabet=alphabet, dataset=dataset, outtype=outtype, isupper=isupper, iscamelcase=True);



    def __call__(self, count=4, nullable=False):
        """ Algorithme de generation de nom
        """
        # on genere un mot avec le super generateur
        return super().__call__(count=count, nullable=nullable);





# if __name__=='__main__':
#     ug = NameGenerator();
#     ug.nullable = True;
#     print(ug());









