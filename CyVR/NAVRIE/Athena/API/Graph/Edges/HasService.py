from arango import ArangoClient
from uuid import UUID

import json

from CyVR.NAVRIE.Athena.DatabaseConnection import DatabaseConnection
from CyVR.NAVRIE.Athena.DatabaseInfo import DatabaseInfo

from CyVR.NAVRIE.Athena.Lib.GraphDB import GraphDB
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.Types.Host import Host
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.Types.NetworkAddress import NetworkAddress
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.Types.Time import Time
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.Types.Common import Common
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.Types.Scope import Scope
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.Types.Device import Device

client = ArangoClient()
dbname = DatabaseConnection.getDBName()

db = client.db(dbname)

client = DatabaseConnection.getClient()
graphName = DatabaseInfo.arangodbGraphName
graphinst = db.graph(graphName)

current_graph = db.graph(graphName)

class HasService(object):
    GraphDB.initEdgeCollection('Has_Service', ['Hosts', 'NetworkAddresses'], ['Services'])
    
    # List existing edge definitions
    graphinst.edge_definitions()

    toProcessed = False
    fromProcessed = False

    def getToProcessed():
        return HasService.toProcessed

    def setToProcessedTrue():
        HasService.toProcessed = True

    def setToProcessedFalse():
        HasService.toProcessed = False

    def getFromProcessed():
        return HasService.fromProcessed

    def setFromProcessedTrue():
        HasService.fromProcessed = True

    def setFromProcessedFalse():
        HasService.fromProcessed = False

    def processVertsForEdges():
        if HasService.getFromProcessed() == True & HasService.getToProcessed() == True:
            jsonmsgdata = MessageQueueUtils.getMsgBody()
            hostips4dict = hostCol.returnKeysForNetAddrIp4(jsonmsgdata)
            svcips4dict = serviceCol.returnKeysForNetAddrIp4(jsonmsgdata)
            if not hostips4dict:
               if not svcips4dict:
                    for key, kvalue in hostips4dict.items():
                        hkip4 = key
                        hvip4 = kvalue
                        for key, kvalue in svcip4dict.items():
                            if hvip4 == kvalue:
                                HasService.createEdge("Has_Service", hkip4 , key)
