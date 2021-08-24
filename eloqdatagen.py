import re
import reldatagen as rdg



def strToCamelCase(text):
    """ Programme qui permet de transformer une chaine de caracteres
        en chaine camelcase.
    """

    # on definit la chaine de caracteres de sortie
    out_text = "";

    # on separe la chaine de caracteres en fonction des '_'
    # ensuite on met en camelcase chaque element de la liste
    # enfin on join tous ces elements en chaine de caracteres
    splited_str = re.split("_", text);
    out_text    = "".join([strc.capitalize() for strc in splited_str]);

    # on retourne le resultat trouve
    return out_text;





def getEloquantModelName(struct_name=""):
    """ Programme qui permet de transformer les nom des tables
        en nom de models sous le format Eloquant
    """
    # on met la premiere lettre en majuscule
    eloquant_class_name = strToCamelCase(struct_name);

    # si le nom de la tables se termine par 'ies', alors
    # on supprime les trois dernieres lettres
    # et on ajoute le caractere 'y' a la fin
    if re.search('ies$', eloquant_class_name):
        eloquant_class_name = eloquant_class_name[:-3];
        eloquant_class_name = "{}y".format(eloquant_class_name);

    elif re.search('s$', eloquant_class_name):
        # sinon, 
        # si le nom de la table se termine tous simplement par le 
        # caractere 's', alors
        # on supprime le dernier caractere a la fin.
        eloquant_class_name = eloquant_class_name[:-1];
    
    return eloquant_class_name;


# print(getEloquantModelName("currencies"));


class EloquantDataGenerator(rdg.RelationalDataGenerator):
    """ Generateur de code source de creation de donnees relationnelles
    """

    def __init__(self, schema={}, generators={}):
        """ Constructeur du generateur de code Eloquant
        """
        super(EloquantDataGenerator, self).__init__(schema=schema, generators=generators);

        # INITIALISATION DES DONNEES
        # ==========================

        # on definit le code source a generer
        self._code = "";
    


    def _add_code_line(self, code):
        """ Programme qui ajoute une ligne de code
        """
        self._code = "{}\n{}".format(self._code, code);
        return self._code;
    


    def printcode(self):
        """ Fonction qui imprime le code source
        """
        print(self._code);
        return self._code;



    def generate(self):
        """ Programme de generation du code source de creation
            de donnees
        """
        # on genere les donnees
        data = super().generate();

        # on initialise le code source en PHP
        self._add_code_line("<?php");
        self._add_code_line("\n");

        # IMPORTATION DES MODELS ELOQUANTS
        # ================================
        self._add_code_line("/** IMPORTATION DES MODELS */");

        # pour chaque structure de la liste des structures
        # on recupere le nom de la structure
        # on import le model Eloquant correspondant
        for struct in self._ordered_list:
            struct_name = struct['struct_name'];
            self._add_code_line("use App\Models\{};".format(getEloquantModelName(struct_name)));

        # on import le programme de hashage de Laravel
        self._add_code_line("use Illuminate\Support\Facades\Hash;");
        self._add_code_line("\n");


        # CREATION DES DONNEES
        # ====================
        self._add_code_line("/** CREATION DES DONNEES */");

        # pour chaque structure de la liste des structures
        # on recupere le nom de la structure
        # on cree un nom de variable
        for struct in self._ordered_list:
            struct_name = struct['struct_name'];
            var_name    = struct_name[:-1];

            # on recupere les donnees generees pour cette structure
            rows = data[struct_name];

            # pour chaque ligne de donnees generees pour cette structure
            # on instancie le models
            for row in rows:
                self._add_code_line("${} = new {};".format(var_name, getEloquantModelName(struct_name)));
                
                # pour chaque colonne de la ligne
                # on renseigne les champs du models eloquant
                for column, value in row.items():
                    if value is not None:
                        if column != 'password':
                            if type(value) is str:
                                self._add_code_line("${}->{} = \"{}\";".format(var_name, column, value));
                            else:
                                self._add_code_line("${}->{} = {};".format(var_name, column, value));
                        else:
                            self._add_code_line("${}->{} = Hash::make(\"{}\");".format(var_name, column, value));
                    else:
                        self._add_code_line("${}->{} = NULL;".format(var_name, column));

                # on sauvegarde cette ligne de donnees
                self._add_code_line("${}->save();".format(var_name));
                self._add_code_line("\n");


        return data;

        

