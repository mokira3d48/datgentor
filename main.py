
import datagen
import reldatagen
import eloqdatagen
from settings.default import GENERATORS

# gen = datagen.DataGenerator(dataset=['mokira', 'therin', 'archille']);
# keygen = GENERATORS['KEY'];
# # gen = datagen.DataGenerator('0123456789');

# print(gen(6));
# print(keygen(16));

schemas = {
    "likes": [
        {"field_name": "user",   "dtype": "_users"},
        {"field_name": "vname",   "dtype": "_videos"},
        {"field_name": "comment",   "dtype": "TEXT"},
    ],
    "videos" : [
        {"field_name": "name",   "dtype": "NAME", "id": True},
        {"field_name": "owner",  "dtype": "_users", "nullable": True},
    ],
    "users": [
        {"field_name": "email",     "dtype": "EMAIL", "id":True},
        {"field_name": "name",      "dtype": "USERNAME", "nullable": True},
        {"field_name": "password",  "dtype": "PASSWORD"},
        
    ],
}

GENERATORS['PASSWORD'] = GENERATORS['INTEGER'];
GENERATORS['USERNAME'] = GENERATORS['KEY'];
GENERATORS['EMAIL']    = GENERATORS['KEY'];
GENERATORS['NAME']     = GENERATORS['KEY'];

# rdg = reldatagen.RelationalDataGenerator(schema=schemas, generators=GENERATORS);
rdg = eloqdatagen.EloquantDataGenerator(schema=schemas, generators=GENERATORS);

rdg.COUNTS_VALUE['likes'] = 5;

rdg.generate();
# print(rdg.generate());
print("\n");
rdg.printcode();
print("\n");
# rdg.printlog();

