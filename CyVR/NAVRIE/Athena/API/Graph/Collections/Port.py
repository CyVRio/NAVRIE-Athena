from arango import ArangoClient
from uuid import UUID

import json

from CyVR.NAVRIE.Athena.DatabaseConnection import DatabaseConnection
from CyVR.NAVRIE.Athena.DatabaseInfo import DatabaseInfo
from CyVR.NAVRIE.Athena.Lib.SendMQ import SendMQ
from CyVR.NAVRIE.Athena.Lib.TypeTools import TypeTools

from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.Types.NetworkAddress import NetworkAddress as attributeNetAddr
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.Types.Protocol import Protocol as attributeProtocol
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.Types.Port import Port as attributePort
from CyVR.NAVRIE.Athena.Lib.GraphDB import GraphDB
from CyVR.NAVRIE.Athena.Lib.RecieveMQ import RecieveMQ

client = ArangoClient()
dbname = DatabaseConnection.getDBName()

db = client.db(dbname)

client = DatabaseConnection.getClient()
graphName = DatabaseInfo.getGraphName()
graphinst = db.graph(graphName)

current_graph = db.graph(graphName)

vertexCollection = "Ports"

class Port(object):
    """description of class"""

    vertexCollection = "Ports"
    GraphDB.initVertexCollection(vertexCollection)

    recievequeueName = 'navrie_athena_create_queue'
    
    def callback(ch, method, properties, msgbody):
        print(" [x] Port Callback Recieved %r" % msgbody)

        # parse incoming message
        mb = msgbody
        jsonmsgbody_data = json.loads(mb.decode("utf-8"))

        port = jsonmsgbody_data['port']
        protocol = jsonmsgbody_data['protocol']

        portNum = attributePort.PortNumber(port)

        if protocol == "udp":
            protocolAttr = attributeProtocol.Protocol_UDP()

        if protocol == "tcp":
            protocolAttr = attributeProtocol.Protocol_TCP()

        if protocol == "igp":
            protocolAttr = attributeProtocol.Protocol_IGP()

        if protocol == "stream":
            protocolAttr = attributeProtocol.Protocol_Stream()

        if protocol == "icmp":
            protocolAttr = attributeProtocol.Protocol_ICMP()

        if protocol == "igmp":
            protocolAttr = attributeProtocol.Protocol_IGMP()

        if protocol == "ipv4":
            protocolAttr = attributeProtocol.Protocol_IPv4()

        if protocol == "egp":
            protocolAttr = attributeProtocol.Protocol_EGP()

        if protocol == "cbt":
            protocolAttr = attributeProtocol.Protocol_CBT()

        if protocol == "ggp":
            protocolAttr = attributeProtocol.Protocol_GGP()

        if protocol == "igp":
            protocolAttr = attributeProtocol.Protocol_IGP()

        if protocol == "igmp":
            protocolAttr = attributeProtocol.Protocol_IGMP()

        if protocol == "hopopt":
            protocolAttr = attributeProtocol.Protocol_IPv6_Hop_Option()

        if protocol == "ipv6":
            protocolAttr = attributeProtocol.Protocol_IPv6()

        if protocol == "ipv6-frag":
            protocolAttr = attributeProtocol.Protocol_IPv6_Frag()

        if protocol == "ipv6-route":
            protocolAttr = attributeProtocol.Protocol_IPv6_Route()

        if protocol == "ipv6-icmp":
            protocolAttr = attributeProtocol.Protocol_IPv6_ICMP()

        if protocol == "ipv6-nonxt":
            protocolAttr = attributeProtocol.Protocol_IPv6_Nonxt()

        if protocol == "ipv6-opts":
            protocolAttr = attributeProtocol.Protocol_IPv6_Opts()

        if protocol == "prm":
            protocolAttr = attributeProtocol.Protocol_PRM()

        if protocol == "trunk-1":
            protocolAttr = attributeProtocol.Protocol_Trunk_1()

        if protocol == "trunk-2":
            protocolAttr = attributeProtocol.Protocol_Trunk_2()

        if protocol == "mux":
            protocolAttr = attributeProtocol.Protocol_MUX()

        if protocol == "dcn-meas":
            protocolAttr = attributeProtocol.Protocol_DCN_MEAS()

        if protocol == "hmp":
            protocolAttr = attributeProtocol.Protocol_HMP()

        if protocol == "bbn-rcc-mon":
            protocolAttr = attributeProtocol.Protocol_BBN_RCC_MON()

        if protocol == "nvp-ii":
            protocolAttr = attributeProtocol.Protocol_NVP_II()

        if protocol == "pup":
            protocolAttr = attributeProtocol.Protocol_PUP()

        if protocol == "argus":
            protocolAttr = attributeProtocol.Protocol_ARGUS()

        if protocol == "emcon":
            protocolAttr = attributeProtocol.Protocol_EMCON()

        if protocol == "xnet":
            protocolAttr = attributeProtocol.Protocol_XNET()

        if protocol == "chaos":
            protocolAttr = attributeProtocol.Protocol_Chaos()


        kvps = TypeTools.merge_two_dicts(portNum, protocolAttr)
            
        # add incoming to new document
        GraphDB.CreateEntry(vertexCollection, kvps)

    RecieveMQ.createQueue(1, callback, recievequeueName)

if __name__ == '__main__':
    app.run(debug=True)