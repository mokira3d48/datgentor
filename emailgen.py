import datagen
import usernamegen


class EmailGenerator(usernamegen.UsernameGenerator):
    """ Generateur de nom
    """


    def __init__(self, alphabet="1", dataset=["OK"], outtype=str):
        """ Construteur de generateur de nom
        """
        super().__init__(alphabet=alphabet, dataset=dataset, outtype=outtype, isupper=False, iscamelcase=False);



    def __call__(self, count1=None, count2=None, nullable=False):
        """ Algorithme de generation de nom
        """
        # on genere un mot avec le super generateur
        username = super().__call__(count1=count1, count2=count2, nullable=nullable);

        # si le mot est Null, alors
        if username is not None:
            return f"{username}@email.com";
        else:
            return None;





# if __name__=='__main__':
#     ug = EmailGenerator();
#     ug.nullable = True;
#     print(ug());


