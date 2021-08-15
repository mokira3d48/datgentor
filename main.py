import datagen
import reldatagen
from settings.default import GENERATORS

# gen = datagen.DataGenerator(dataset=['mokira', 'therin', 'archille']);
# keygen = GENERATORS['KEY'];
# # gen = datagen.DataGenerator('0123456789');

# print(gen(6));
# print(keygen(16));

schemas = {
    "likes": [
        {"field_name": "name",   "dtype": "_users"},
        {"field_name": "name",   "dtype": "_videos"},
        {"field_name": "comment",   "dtype": "TEXT"},
    ],
    "videos" : [
        {"field_name": "name",   "dtype": "NAME", "id": True},
        {"field_name": "owner",  "dtype": "_users"},
    ],
    "users": [
        {"field_name": "email",     "dtype": "EMAIL", "id":True},
        {"field_name": "name",      "dtype": "USERNAME"},
        {"field_name": "password",  "dtype": "PASSWORD"},
        
    ],
}

rdg = reldatagen.RelationalDataGenerator(schema=schemas);

rdg.generate();
