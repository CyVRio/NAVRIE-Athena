import logging
from uuid import UUID

from flask import Flask, jsonify, abort, make_response


from CyVR.NAVRIE.Athena.DatabaseConnection import DatabaseConnection
from CyVR.NAVRIE.Athena.DatabaseInfo import DatabaseInfo

from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.AttributeTools import AttributeTools

from arango import ArangoClient
from arango.collections import VertexCollection


client = ArangoClient()
dbname = DatabaseConnection.getDBName()

db = client.db(dbname)

client = DatabaseConnection.getClient()
graphName = DatabaseInfo.getGraphName()
graphinst = db.graph(graphName)


class Common(object):
    """description of class"""

        
    def set_key(vertex_collection):
        vc =    (client, graphName, vertex_collection)
        uniqKey = False
        while uniqKey == False:
            key = UUID.uuid4            
            vc.has(key)
            if vc.has(key):
                uniqKey = False
            else:
                uniqKey = True
        
        attribute = AttributeTools.setAttribute("_key", _key)
        return attribute

    def set_Name(name):
        attribute = AttributeTools.setAttribute("Common_Name", name)
        return attribute

    def set_Description(description):
        attribute = AttributeTools.setAttribute("Common_Description", description)
        return attribute
