import datagen as dtg

# CONFIGURATION DES ALPHABETS
# ===========================
STR_ALPHABET = ''.join([chr(code) for code in range(11, 256)]);
KEY_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-.";
INT_ALPHABET = "0123456789";


# CONFIGURATION DES DATASETS
# ==========================


# INITIALISATION DES GENERATEURS
# ==============================
strgen = dtg.DataGenerator(alphabet=STR_ALPHABET);
keygen = dtg.DataGenerator(alphabet=KEY_ALPHABET);
intgen = dtg.DataGenerator(alphabet=INT_ALPHABET);

# ASSOCIATION DES GENERATEURS AVEC DES TYPES DE DONNEES
# =====================================================
GENERATORS = {
    'STRING'    : strgen,
    'INTEGER'   : intgen,
    'KEY'       : keygen,
};

