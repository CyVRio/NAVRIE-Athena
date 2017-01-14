import logging
from arango import ArangoClient

from CyVR.NAVRIE.Athena.DatabaseConnection import DatabaseConnection
from CyVR.NAVRIE.Athena.DatabaseInfo import DatabaseInfo

db = DatabaseInfo.getDatabaseName
graphName = DatabaseInfo.arangodbGraphName
#current_graph = db.graph(graphName)

class AttributeTools(object):
    """description of class"""

    def setAttribute(collection, key, attribute, value):
#        collectionInUse = db.collection(collection)
        collectionInUse.update_match({'_key': key}, {attribute: value})

    def setAttribute(attribute, value):
 #       collectionInUse = db.collection(collection)
        return({attribute: value})



    def updateDoc(collection, key, attribute, value):
        collectionInUse = db.collection(collection)
        collectionInUse.update_match({'_key': key}, {attribute: value})
