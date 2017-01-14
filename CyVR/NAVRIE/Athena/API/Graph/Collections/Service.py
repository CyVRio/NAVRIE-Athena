from uuid import UUID

import pika, os, logging, time

from arango import ArangoClient

import json

from CyVR.NAVRIE.Athena.DatabaseConnection import DatabaseConnection
from CyVR.NAVRIE.Athena.DatabaseInfo import DatabaseInfo
from CyVR.NAVRIE.Athena.Lib.SendMQ import SendMQ
from CyVR.NAVRIE.Athena.Lib.TypeTools import TypeTools

from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.Types.NetworkAddress import NetworkAddress as attributeNetAddr
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.Types.Host import Host as attributeHost
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.Types.Application import Application as attributeApplication
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.Types.Port import Port as attributePort
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.Types.Protocol import Protocol as attributeProtocol
from CyVR.NAVRIE.Athena.Lib.GraphDB import GraphDB
from CyVR.NAVRIE.Athena.Lib.RecieveMQ import RecieveMQ

client = ArangoClient()
dbname = DatabaseConnection.getDBName()

db = client.db(dbname)

client = DatabaseConnection.getClient()
graphName = DatabaseInfo.getGraphName()
graphinst = db.graph(graphName)

current_graph = db.graph(graphName)

vertexCollection = "Services"
svcCol = db.collection(vertexCollection)

class Service(object):
    """description of class"""

    vertexCollection = "Services"
    GraphDB.initVertexCollection(vertexCollection)

    def addEntry(jsonmsgbody_data):
        if jsonmsgbody_data['NAVRIE_CollectionType'] == "NAVRIE_Service":
            serviceName = jsonmsgbody_data['serviceName']
            banner = jsonmsgbody_data['banner']
            port = jsonmsgbody_data['port']
            state = jsonmsgbody_data['state']
            protocol = jsonmsgbody_data['protocol']
            tunnel = jsonmsgbody_data['tunnel']
            owner = jsonmsgbody_data['owner']
            cpelist = jsonmsgbody_data['cpelist']
            reason = jsonmsgbody_data['reason']
            reason_ip = jsonmsgbody_data['reason_ip']
            reason_ttl = jsonmsgbody_data['reason_ttl']
            ip4 = jsonmsgbody_data['ip4Address']
            ip6 = jsonmsgbody_data['ip6Address']
            mac = jsonmsgbody_data['macAddress']    

            vertexCollection = "Services"
            GraphDB.initVertexCollection(vertexCollection)
            
            serviceNameattr = attributeApplication.set_ServiceName(serviceName)
            bannerattr = attributeApplication.set_Banner(banner)
            portattr = attributePort.PortNumber(port)
            protocolattr = attributeProtocol.Protcol_SelfSet(protocol)
            ipv4attr = attributeNetAddr.set_IPv4Address(ip4)
            ipv6attr = attributeNetAddr.set_IPv6Address(ip6)
            macattr = attributeNetAddr.set_MACAddress(mac)
            mkvps = {}
            mkvps.update(serviceNameattr)
            mkvps.update(bannerattr)
            mkvps.update(portattr)
            mkvps.update(protocolattr)
            mkvps.update(ipv4attr)
            mkvps.update(ipv6attr)
            mkvps.update(macattr)

            # add incoming to new document
            GraphDB.CreateEntry(vertexCollection, mkvps)

    def returnAttributeDict(jsonmsgbody_data):
        if jsonmsgbody_data['NAVRIE_CollectionType'] == "NAVRIE_Service":
            serviceName = jsonmsgbody_data['serviceName']
            banner = jsonmsgbody_data['banner']
            port = jsonmsgbody_data['port']
            state = jsonmsgbody_data['state']
            protocol = jsonmsgbody_data['protocol']
            tunnel = jsonmsgbody_data['tunnel']
            owner = jsonmsgbody_data['owner']
            cpelist = jsonmsgbody_data['cpelist']
            reason = jsonmsgbody_data['reason']
            reason_ip = jsonmsgbody_data['reason_ip']
            reason_ttl = jsonmsgbody_data['reason_ttl']
            ip4 = jsonmsgbody_data['ip4Address']
            ip6 = jsonmsgbody_data['ip6Address']
            mac = jsonmsgbody_data['macAddress']    
            
            serviceNameattr = attributeApplication.set_ServiceName(serviceName)
            bannerattr = attributeApplication.set_Banner(banner)
            portattr = attributePort.PortNumber(port)
            protocolattr = attributeProtocol.Protcol_SelfSet(protocol)
            ipv4attr = attributeNetAddr.set_IPv4Address(ip4)
            ipv6attr = attributeNetAddr.set_IPv6Address(ip6)
            macattr = attributeNetAddr.set_MACAddress(mac)
            mkvps = {}
            mkvps.update(serviceNameattr)
            mkvps.update(bannerattr)
            mkvps.update(portattr)
            mkvps.update(protocolattr)
            mkvps.update(ipv4attr)
            mkvps.update(ipv6attr)
            mkvps.update(macattr)
            return mkvps

    def returnKeysForNetAddrIp4(jsonmsgbody_data):
        keysDict = {}        
        svcCol = db.collection(vertexCollection)
        if jsonmsgbody_data['NAVRIE_CollectionType'] == "NAVRIE_Service":
            ip4 = jsonmsgbody_data['ip4Address']
            for svcCol in svcCol.find({'NetworkAddress_IPv4Address': ip4}):
                key = svcCol['_id']
                keysDict.update({key: ip4})
            return keysDict
        return {}

#                key = hostsCol['_key']

'''
    def returnFindAttributeDictNetAddrIp4(jsonmsgbody_data):
        if jsonmsgbody_data['NAVRIE_CollectionType'] == "NAVRIE_Service":
            ip4 = jsonmsgbody_data['ip4Address']
            ip4attr = attributeNetAddr.set_IPv4Address(ip4)
            mkvps = {}
            mkvps.update(ip4attr)
            ipkey = {}    
            for key, kvalue in mkvps.items():
                if key == "NetworkAddress_IPv4Address":
                    #(search aql for ipv4, ipv6, and mac matches between net address and svc vertices)   
                    cservices = db.collection('Services')
                    for service in cservices.find({'NetworkAddress_IPv4Address': kvalue}):
                        servicekey = (service['_key', kvalue])
                        ipkey.update(servicekey)

            return ipkey
'''