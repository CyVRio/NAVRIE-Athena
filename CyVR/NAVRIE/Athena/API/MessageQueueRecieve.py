from uuid import UUID
from multiprocessing import Process
import sys
import pika
import os
import logging
import time
import json

from arango import ArangoClient

from CyVR.NAVRIE.Athena.DatabaseConnection import DatabaseConnection
from CyVR.NAVRIE.Athena.DatabaseInfo import DatabaseInfo

from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.Types.NetworkAddress import NetworkAddress as attributeNetAddr
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.Types.Host import Host as attributeHost
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.Types.Application import Application as attributeApplication
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.Types.Port import Port as attributePort
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.Types.Protocol import Protocol as attributeProtocol

from CyVR.NAVRIE.Athena.API.Graph.Collections.Host import Host as hostCol
from CyVR.NAVRIE.Athena.API.Graph.Collections.Service import Service as serviceCol

from CyVR.NAVRIE.Athena.API.Graph.Edges.HasService import HasService

from CyVR.NAVRIE.Athena.Lib.MessageQueueUtils import MessageQueueUtils
from CyVR.NAVRIE.Athena.Lib.GraphDB import GraphDB
from CyVR.NAVRIE.Athena.Lib.SendMQ import SendMQ
from CyVR.NAVRIE.Athena.Lib.TypeTools import TypeTools
from CyVR.NAVRIE.Athena.Lib.RecieveMQ import RecieveMQ
from CyVR.NAVRIE.Athena.Lib.ScratchDicts import ScratchDicts

client = ArangoClient()
dbname = DatabaseConnection.getDBName()

db = client.db(dbname)

client = DatabaseConnection.getClient()
graphName = DatabaseInfo.getGraphName()
graphinst = db.graph(graphName)

current_graph = db.graph(graphName)

class MessageQueueRecieve(object):
    """description of class"""
    
    recievequeueName = 'navrie_athena_recieve_queue'

    # Parse CLODUAMQP_URL (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost/%2f')
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    connection = pika.BlockingConnection(params) # Connect to CloudAMQP
    channel = connection.channel() # start a channel

    msgbody = {}

    def setMsgBody(msgbodyts):
        msgbody = msgbodyts


    def getMsgBody():
        return msgbody

    def callback(ch, method, properties, msgbody):
        print(" [x] Network Address Callback Recieved %r" % msgbody)

        # parse incoming message
        mb = msgbody
        jsonmsgbody_data = json.loads(mb.decode("utf-8"))
        MessageQueueUtils.setMsgBody(jsonmsgbody_data)
        attributes = {}
        ddadict = {}        

        if jsonmsgbody_data['NAVRIE_CollectionType'] == "NAVRIE_Host":
            hostips4dict = {}
            ae = hostCol.addEntry(jsonmsgbody_data)    
            ddadict = TypeTools.dedupDict(attributes)
            HasService.setFromProcessedTrue()
            ScratchDicts.setSD1(hostCol.returnKeysForNetAddrIp4(jsonmsgbody_data))
        
        if jsonmsgbody_data['NAVRIE_CollectionType'] == "NAVRIE_Service":
            ae = serviceCol.addEntry(jsonmsgbody_data)
            ddadict = TypeTools.dedupDict(attributes)
            HasService.setToProcessedTrue()
            ScratchDicts.setSD2(serviceCol.returnKeysForNetAddrIp4(jsonmsgbody_data))

        if HasService.getFromProcessed() == True & HasService.getToProcessed() == True:
            hostips4dict = ScratchDicts.getSD1()
            svcips4dict = ScratchDicts.getSD2()
            for key, kvalue in hostips4dict.items():
                hkip4 = key
                hvip4 = kvalue
                for key, kvalue in svcips4dict.items():
                    if hvip4 == kvalue:
                        GraphDB.createEdge("Has_Service", hkip4, key)
      #                  GraphDB.createEdge("Has_Service", "Hosts", hkip4, "Services" , key)

    #set up subscription on the queue
    channel.basic_consume(callback,
    queue=recievequeueName,
    no_ack=True)

    # start consuming (blocks)
    channel.start_consuming()
    connection.close()

    RecieveMQ.createQueue(1, callback, recievequeueName)
            
        # Vertex collections have a similar interface to standard collections
        # return current_vertex_collection.insert({"_key": keykeyvalue, createdkey: createdvalue, lastUpdatedkey: lastUpdatedvalue, descriptionkey: descriptionvalue, interfacenamekey: interfacenamevalue, inScopenamekey: inScopenamevalue, lastKnownStatusnamekey: lastKnownStatusnamevalue, NetworkAddress_IPv4namekey: NetworkAddress_IPv4namevalue, NetworkAddress_IPv6namekey: NetworkAddress_IPv6namevalue, NetworkAddress_MACnamekey: NetworkAddress_MACnamevalue, NetworkAddress_DLCInamekey: NetworkAddress_DLCInamevalue, NetworkAddress_VPInamekey: NetworkAddress_VPInamevalue, NetworkAddress_VCInamekey: NetworkAddress_VCInamevalue, NetworkAddress_MPLS_Labelnamekey: NetworkAddress_MPLS_Labelnamevalue, NetworkAddress_VLAN_Tagnamekey: NetworkAddress_VLAN_Tagnamevalue})

if __name__ == '__main__':
    app.run(debug=True)

