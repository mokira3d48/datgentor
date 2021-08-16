
import reldatagen as rdg


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
            self._add_code_line("use App\Models\{};".format(struct_name));

        # on saute une ligne dans le code source        
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
                self._add_code_line(f"${var_name} = new {struct_name};");
                
                # pour chaque colonne de la ligne
                # on renseigne les champs du models eloquant
                for column, value in row.items():
                    if value is not None:
                        self._add_code_line(f"${var_name}->{column} = \"{value}\"");
                    else:
                        self._add_code_line(f"${var_name}->{column} = NULL;");

                # on sauvegarde cette ligne de donnees
                self._add_code_line(f"${var_name}->save();");
                self._add_code_line("\n");


        return data;

        

