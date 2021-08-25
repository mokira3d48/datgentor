# import time

import datagen
import emailgen
import anagramdgen
import namegen
import usernamegen
import integergen

import eloqdatagen


schemas = {
    "users": [
        {"field_name": "username",  "dtype": "USERNAME", "id":True},
        {"field_name": "email",     "dtype": "EMAIL"},
        {"field_name": "firstname",  "dtype": "NAME"},
        {"field_name": "lastname",  "dtype": "NAME"},
        {"field_name": "lang",  "dtype": "STRING"},
        {"field_name": "password",  "dtype": "PASSWORD"},
        {"field_name": "registration_dt", "dtype": "TIMESTAMPS"},
    ],
    "adms": [
        {"field_name": "username",  "dtype": "USERNAME", "id":True},
        {"field_name": "email",     "dtype": "EMAIL"},
        {"field_name": "firstname",  "dtype": "NAME"},
        {"field_name": "lastname",  "dtype": "NAME"},
        {"field_name": "password",  "dtype": "PASSWORD"},
        {"field_name": "registration_dt", "dtype": "TIMESTAMPS"},
    ],
    "std_subscriptions": [
        {"field_name": "pid",  "dtype": "KEY(4)", "id":True},
        {"field_name": "name",  "dtype": "NAME"},
        {"field_name": "value",  "dtype": "DECIMAL"},
        {"field_name": "limit",  "dtype": "LIMIT", "nullable": True},
        {"field_name": "size",  "dtype": "SIZE", "nullable": True},
        {"field_name": "duration",  "dtype": "DURATION", "nullable": True},
        {"field_name": "registration_dt", "dtype": "TIMESTAMPS", "nullable": True},
    ],
    "subscriptions": [
        {"field_name": "pid",  "dtype": "KEY(16)", "id": True},
        {"field_name": "earned",  "dtype": "PURCE"},
        {"field_name": "activated_at", "dtype": "TIMESTAMPS", "nullable": True},
        {"field_name": "expired_at", "dtype": "TIMESTAMPS", "nullable": True},
        {"field_name": "status",  "dtype": "STATUS"},
        {"field_name": "owner",  "dtype": "_users"},
        {"field_name": "subscription_type",  "dtype": "_std_subscriptions"},
    ],
    "trading_accounts": [
        {"field_name": "account_id",  "dtype": "ID", "id":True},
        {"field_name": "acc_password",  "dtype": "PASSWORD"},
        {"field_name": "server_name",  "dtype": "USERNAME"},
        {"field_name": "type",  "dtype": "ACCOUNT_TYPE"},
        {"field_name": "gain",  "dtype": "GAIN"},
        {"field_name": "status",  "dtype": "STATUS"},
        {"field_name": "registration_dt", "dtype": "TIMESTAMPS"},
        {"field_name": "owner",  "dtype": "_users"},
        {"field_name": "subscription",  "dtype": "_subscriptions", "nullable": True},
    ]
};

# configuration des generateurs
# =============================
account_type = datagen.DataGenerator(dataset=['type1', 'type2', 'type3']);
# timestamp = integergen.IntegerGenerator(intervalle=(160000, int(time.time())));
timestamp = integergen.IntegerGenerator(intervalle=(160000000, 170000000));
password  = usernamegen.UsernameGenerator();
username  = usernamegen.UsernameGenerator();
duration  = integergen.IntegerGenerator(intervalle=(15, 365));
integer   = integergen.IntegerGenerator(intervalle=(0, 6000));
purcent   = integergen.IntegerGenerator(intervalle=(0, 20));
limit     = integergen.IntegerGenerator(intervalle=(0, 20));
gain      = integergen.IntegerGenerator(intervalle=(0, 800));
status    = datagen.DataGenerator(alphabet="012");
email     = emailgen.EmailGenerator();
name      = namegen.NameGenerator();
size      = integergen.IntegerGenerator(intervalle=(0, 10));
key16     = datagen.DataGenerator(alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789|-.");
key4      = datagen.DataGenerator(alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789|-.");
_id       = datagen.DataGenerator(alphabet="0123456789");

account_type.setCount(1);
username.setCount(4);
username.setDigitCount(2);

password.setCount(2);
status.setCount(1);
email.setCount(4);
name.setCount(3);
key16.setCount(16);
key4.setCount(4);
_id.setCount(12);


GENERATORS = {};
GENERATORS['ACCOUNT_TYPE'] = account_type;
GENERATORS['TIMESTAMPS'] = timestamp;
GENERATORS['PASSWORD']   = password;
GENERATORS['USERNAME']   = username;
GENERATORS['DURATION']   = duration;
GENERATORS['DECIMAL']    = integer;
GENERATORS['STATUS']     = status;
GENERATORS['EMAIL']      = email;
GENERATORS['PURCE']      = purcent;
GENERATORS['NAME']       = name;
GENERATORS['GAIN']       = gain;
GENERATORS['SIZE']       = size;
GENERATORS['LIMIT']       = limit;
GENERATORS['KEY(16)']    = key16;
GENERATORS['KEY(4)']     = key4;
GENERATORS['ID']         = _id;

# construction du generateur
rdg = eloqdatagen.EloquantDataGenerator(schema=schemas, generators=GENERATORS);

rdg.DEFAULT_DATA_COUNT = 500;
rdg.init_counts_values();

rdg.COUNTS_VALUE['std_subscriptions'] = 3;
rdg.COUNTS_VALUE['users'] = 100;
rdg.COUNTS_VALUE['adms']  = 2;

rdg.generate();
rdg.printcode();
print("\n");
