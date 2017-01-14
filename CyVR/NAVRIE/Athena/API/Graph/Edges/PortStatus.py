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
graphName = DatabaseInfo.arangodbGraphName()
graphinst = db.graph(graphName)

current_graph = db.graph(graphName)

class PortStatus(object):
    GraphDB.initEdgeCollection('Port_Open', ['NetworkAddresses', 'Services'], ['Ports'])    
    GraphDB.initEdgeCollection('Port_Filtered', ['NetworkAddresses', 'Services'], ['Ports'])
    GraphDB.initEdgeCollection('Port_Closed', ['NetworkAddresses', 'Services'], ['Ports'])
    
    # List existing edge definitions
    graphinst.edge_definitions()

