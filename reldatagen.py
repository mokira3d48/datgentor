

class RelationalDataGenerator(object):
    """ Programme de generation de donnees relationnelles
    """

    # CONFIGURATION GLOBAL
    # ====================
    DEFAULT_DATA_COUNT = 16;
    COUNTS_VALUE = {};



    def __init__(self, schema={}, generators={}):
        """ Constructeur du generateur de donnees 
            relationnelles
        """
        super(RelationalDataGenerator, self).__init__();

        # INITIALISATION DU GENERATEUR
        # ============================
        #
        # on definit un schema et un generateur de donnees
        self._generators = generators;
        self._schema     = schema;

        # on initialise le nombre de donnees a generer par structure
        # pour chaque structure de donne

        # on definit aussi le liste de messages pour renseigner 
        # le programmeur sur l'etat interne du generateur, afin de 
        # justifier le resultat de la generation
        self._logs = [];



    def init_counts_values(self):
        """ Programme d'initialisation de nombre de donnees a generer
            par structure
        """
        # pour chaque structure de donnees
        # on initialise a DEFAULT_DATA_COUNT
        for struct in self._schema:
            self.COUNTS_VALUE[struct] = self.DEFAULT_DATA_COUNT;



    def logs(self):
        """ Fonction de recuperation des messages
        """
        return self._logs;
    


    def __order_schemas(self):
        """ Fonction qui permet d'ordonner les schemas de donnees
            en fonction de leurs attributs
        """
        # on definit une liste ordonnees de schemas de donnees
        self._ordered_list = [];

        print("schema: ", [struct for struct in self._schema]);
        print("ordered_list: ", [struct for struct in self._ordered_list]);

        # tanqu'il y a de structure dans le dictionnaire des schemas
        # on clonne l'etat du schema actuel
        # pour chaque structure et pour chaque champ de celle-ci, 
        # on verifie si sa propriete `dtype` est une structure
        while self._schema:
            schema = self._schema.copy();

            for struct in schema:
                # on definit une variable supposant que la structure
                # peut etre ajouter a la liste ordonnee des structures
                appenable = True;

                # on recupere tous les champs de la structure
                fields = schema[struct];

                for field in fields:
                    # on recupere le nom de la structure referencee
                    struct_name = self.__get_struct_name(field);

                    # print("struct_name", struct_name);

                    if struct_name is not None:
                        appenable = appenable and self.__exists_in_ordered_list(struct_name);
                        
                        # si cette structure n'existe pas encore dans la liste
                        # ordonnee des structures, alors
                        # on arrete de parcourir les champs suivants de la structure
                        # actuelle, et on passe a la structure suivante
                        if not appenable:
                            break;
                    
                # si on peut ajouter la structure, alors 
                # on ajoute et on le supprime du schema
                if appenable:
                    self._ordered_list.append({
                        "struct_name" : struct, 
                        "fields"      : fields
                    });
                    del self._schema[struct];

            # import time
            # time.sleep(1);

            # print("schema: ", [struct for struct in self._schema]);
            # print("ordered_list: ", [struct['struct_name'] for struct in self._ordered_list]);
            # print("\n\n");


    
    @staticmethod
    def __get_struct_name(field):
        """ Programme qui permet d'extrait le nom d'une structure
            d'un champs
        """
        # on recupere la valeur de son dtype
        dtype = field['dtype'] if 'dtype' in field else None;

        # si le `dtype` n'est pas null, alors
        # on verifie si c'est le nom d'une structure particuliere
        if dtype is not None:
            if dtype[0] == '_':
                # on retourne le nom de la structure
                return dtype[1:];

        return None;




    def __exists_in_ordered_list(self, struct_name):
        """ Fonction qui verifie si un champ existe deja dans la liste
            ordonnee des structures
        """
        for struct in self._ordered_list:
            if struct['struct_name'] == struct_name:
                return True;
        
        return False;




    def generate(self):
        """ Implementation du programme de generation de donnees
            relationnelles
        """
        # on ordonne les structures du schema en fonction des champs
        # qui referencisent d'autre structure du meme schema
        self.__order_schemas();


#####################################################################################
######################################################################################
#
# schemas = {
#     "users": [
#         {"field_name": "email",     "dtype": "EMAIL", "id":True},
#         {"field_name": "name",      "dtype": "USERNAME"},
#         {"field_name": "password",  "dtype": "PASSWORD"},
        
#     ], 
#     "videos" : [
#         {"field_name": "name",   "dtype": "NAME"},
#         {"field_name": "owner",  "dtype": "_users"},
#     ]
# }

# data = {
#     "users": [
#         {"email": "kipose4@mail.com", "name": "malick3", "password": "omf3003mi"},
#         {"email": "obme90@mail.com", "name": "ertien", "password": "omf3003mi"},
#         {"email": "serfi32@mail.com", "name": "dime_depo", "password": "omf3003mi"}
#     ],
#     "videos": [
#         {"name": "Fortin Goloi", "owner": "serfi32@mail.com",},
#         {"name": "Isdor duCon",  "owner": "obme90@mail.com",}
#     ]
# }
