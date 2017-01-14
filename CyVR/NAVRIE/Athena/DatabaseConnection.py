from CyVR.NAVRIE.Athena.DatabaseInfo import DatabaseInfo

from arango import ArangoClient

dbName = DatabaseInfo.arangodbdatabasename

client = ArangoClient(
    protocol=DatabaseInfo.arangodbprotocol,
    host=DatabaseInfo.arangodbhost,
    port=DatabaseInfo.arangodbport,
    username=DatabaseInfo.arangodbuser,
    password=DatabaseInfo.arangodbpw,
    enable_logging=True
    )

db = client.db(dbName)
graphName = DatabaseInfo.getGraphName()

class DatabaseConnection(object):
    """description of class"""

    try:
         client.create_database(dbName, username=client.username, password=client.password)
    except:
         print("Database: " + dbName + " already exists")

    try:
         db.create_graph(graphName)
    except:
         print("Graph: " + graphName + " already exists")

    def getDBName():
        return dbName 

    def getClient():
        return client   

    def createDb(dbName):
        conn.createDatabase(name = dbName)       

    def switchDb(dbName):
         db = self.conn[dbName]    