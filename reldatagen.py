import random
import datagen as dg

class RelationalDataGenerator(object):
    """ Programme de generation de donnees relationnelles
    """

    # CONFIGURATION GLOBAL
    # ====================
    DEFAULT_DATA_COUNT = 2;
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

        # on definit la memoire de sortie
        self._data = {};

        # on initialise le nombre de donnees a generer par structure
        # pour chaque structure de donne
        self.init_counts_values();

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
    


    def getdata(self):
        """ Fonction de recuperation de donnees generees
        """
        return self._data;
    


    def __order_schemas(self):
        """ Fonction qui permet d'ordonner les schemas de donnees
            en fonction de leurs attributs
        """
        # on definit une liste ordonnees de schemas de donnees
        self._ordered_list = [];

        # print("schema: ", [struct for struct in self._schema]);
        # print("ordered_list: ", [struct for struct in self._ordered_list]);

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

        # dans la liste des structures ordonnees,
        # pour chaque structure,
        # pour chaque champs, de la structure
        # on recupere tous les champs de la structure
        # on initialise le tableau de donnee avec le nom de la structure
        for struct in self._ordered_list:
            struct_name = struct['struct_name'];
            fields      = struct['fields'];

            self._data[struct_name] = [];

            # on recupere le nombre d'exemple de donnees a generer
            count = self.COUNTS_VALUE[struct['struct_name']];

            # pour i allant de 0 a count - 1
            # on definit une ligne de donnee de type `dict`
            for i in range(count):
                row = {};

                for field in fields:
                    field_name = field['field_name'];
                    nullable   = self.__nullable(field);

                    # on recupere si possible le nom de la structure
                    # reference par le champ
                    ref_struct_name = self.__get_struct_name(field);

                    # on definit une colonne dans la ligne de donnees
                    row[field_name] = None;

                    # on recupere le type de donnee du champ
                    dtype = field['dtype'];

                    # si un generateur est specifie pour ce type, alors
                    if dtype in self._generators:
                        gen = self._generators[dtype];

                        # si le champs peut prendre la valeur Null, alors
                        # on configure le generateur pour qu'il puisse generer
                        # aussi des valeurs NULL de temps en temps
                        gen.nullable = nullable;

                        # on fait une etude suivant trois cas
                        # si le champs n'est ni un identifiant, ni reference, alors
                        # genere la valeur a stocker dans cette colonne
                        if not self.__is_id(field) and ref_struct_name is None:
                            row[field_name] = gen();
                        
                        elif self.__is_id(field) and ref_struct_name is None:
                            # si c'est seulement un champs d'identification unique, alors
                            # on appel la fonction de generation d'identifiant avec
                            # les arguments suivants:
                            # le nom de la structure;
                            # le nom du champs;
                            # et le generateur
                            row[field_name] = self.__generate_id(struct_name, field_name, gen);
                    
                    elif ref_struct_name is not None:
                        # si c'est uniquement un champs qui referencie une autre
                        # et que ce champs n'est pas un ID, alors
                        # on cree un generateur de donnee ayant pour dataset, 
                        # la liste des ID de la structure referencee
                        if not self.__is_id(field):
                            id_field_name = self.__get_id_field_name(ref_struct_name);
                            data_rows     = self._data[ref_struct_name];

                            # on definit une dataset vide
                            dataset  = [];

                            # pour chaque ligne de donnee,
                            # on recupere la valeur de son ID
                            for data_row in data_rows:
                                dataset.append(data_row[id_field_name]);
                            
                            # on construit un generateur avec la `dataset`
                            gen = dg.DataGenerator(dataset=dataset);

                            # on definit la longueur par defaut des donnees generees par
                            # le generateur
                            gen.set_default_count(1);

                            # on genere une valeur pour cette colonne
                            row[field_name] = gen(nullable=nullable);

                    else:
                        # si aucun generateur n'est specifie pour ce type 
                        # de donnees, alors
                        # on cree un log
                        self._logs.append(f"[ERROR] \t  No generator defined for {dtype} data type.");

                        

                # on ajoute la ligne de donnees
                self._data[struct['struct_name']].append(row);

        # print(self._data);

        return self._data;




    @staticmethod
    def __is_id(field):
        return 'id' in field;
    



    @staticmethod
    def __nullable(field):
        return 'nullable' in field;



    def __generate_id(self, struct_name, field_name, gen):
        """ Programme de generation d'ID
        """
        # on initialise la donnee a None
        # et on suppose que cette donnee est deja utilisee sur une 
        # autre ligne
        dgen = None;
        used    = True;

        # tand que cette donnee est deja utilisee sur une autre ligne
        # on regenere une autre
        while used:
            dgen = gen();

            # on verifie l'existance de cette donnees generee pour
            # chaque ligne de donnee deja genere
            for row in self._data[struct_name]:
                if dgen == row[field_name]:
                   used = True;
                   break;
            
            used = False;

        return dgen;
    


    def __get_id_field_name(self, struct_name):
        """ Programme recupere le champs ID d'une structure
            passee en argument
        """
        struct = None;

        # pour retrouve la structure dans la liste
        for st in self._ordered_list:
            if st['struct_name'] == struct_name:
                struct = st;
                break;

        # si la structure n'est pas null, alors
        # pour chaque champs de la structure
        if struct:
            fields = struct['fields'];

            for field in fields:
                # si ce champs est un ID, on retourne son nom
                if RelationalDataGenerator.__is_id(field):
                    return field['field_name'];
        
        else:
            return None;



    
    def printlog(self):
        """ Programme qui permet d'imprimer les logs
        """        
        for log in self._logs:
            print(log);
                    





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
