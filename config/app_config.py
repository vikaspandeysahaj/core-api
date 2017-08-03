class Config(object):
    DEBUG = False

    SQL_CONNECTION_URL = "mysql://coredev:!abcd1234@localhost:3306/coredevdb"
    ROOT_CONNECTION_URL = "mysql://root:pass@localhost:3306"
    SQL_ROOT_PASSWORD = "pass"
    SQL_DB_NAME = "coredevdb"
    SQL_DB_USERNAME = "coredev"
    SQL_DB_PASSWORD = "!abcd1234"
    SQL_DB_HOST = "localhost"
    SQL_DB_PORT = "3306"

class Development(Config):
    DEBUG = True

class Test(Config):
    DEBUG = True
    SQL_CONNECTION_URL = "mysql://coretest:!abcd1234@localhost:3306/coretestdb"
    ROOT_CONNECTION_URL = "mysql://root:pass@localhost:3306"
    SQL_ROOT_PASSWORD = "pass"
    SQL_DB_NAME = "coretestdb"
    SQL_DB_USERNAME = "coretest"
    SQL_DB_PASSWORD = "!abcd1234"
    SQL_DB_HOST = "localhost"
    SQL_DB_PORT = "3306"

# use coredevdb
# db.createUser(
#    {
#      user: "coredev",
#      pwd: "passw0rd1234",
#      roles: [ "readWrite", "dbAdmin" ]
#    }
# )