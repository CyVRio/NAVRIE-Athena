import logging
from arango.collection import Collection
from CyVR.NAVRIE.Athena.DatabaseConnection import DatabaseConnection


class CollectionTools(object):
    """description of class"""

    prefix = "prefix"
    collectionName = "IntentionallyLeftBlank"
    fullCollectionName = "NAVRIE_Custom_IntentionallyLeftBlank"

    def createColection(collectionName):
        fullCollectionName = DatabaseConnection.db.createCollection(name= "NAVRIE_Custom_" + collectionName)

    def createColectionWithPrefix(prefix, collectionName):
        fullCollectionName = DatabaseConnection.db.createCollection(name= "NAVRIE_Custom_" + prefix + "_" + collectionName)

    def openCollectionDoc(collectionName, documentKey):
        doc = CollectionTools.fullCollectionName[documentKey]

    def createHostsCollectionDoc(collectionName):
        doc = CollectionTools.fullCollectionName.createDocument()

        e = Collection()
        e.has()
    def setKey(key):
        doc._key = key


    c = Collection()

    doc._key
    def saveEntry():
        doc.save()

    def generateKey(vertexCollectionName):
        # Create a new vertex collection
        try:
            current_vertex_collection = current_graph.create_vertex_collection(vertexCollectionName)
        except:
            # Retrieve an existing vertex collection
            current_vertex_collection = current_graph.vertex_collection(vertexCollectionName)
        
            
        key = set_key(current_vertex_collection)
        
        keykeyvalue = UUID.uuid4()