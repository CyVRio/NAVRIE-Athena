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

vertexCollection = "Hosts"

hostsCol = db.collection(vertexCollection)

class Host(object):
    def addEntry(jsonmsgbody_data):
       if jsonmsgbody_data['NAVRIE_CollectionType'] == "NAVRIE_Host":
            lastboot = jsonmsgbody_data['lastboot']
            uptime = jsonmsgbody_data['uptime']
            vendor = jsonmsgbody_data['vendor']
            os_fingerprint = jsonmsgbody_data['os_fingerprint']
            os_fingerprinted = jsonmsgbody_data['os_fingerprinted']
            ip4 = jsonmsgbody_data['ip4Address']
            ip6 = jsonmsgbody_data['ip6Address']
            mac = jsonmsgbody_data['macAddress']
           
            vertexCollection = "Hosts"
            GraphDB.initVertexCollection(vertexCollection)
            
            lastbootattr = attributeHost.set_LastBoot(lastboot)
            uptimeattr = attributeHost.set_Uptime(uptime)
            vendorattr = attributeHost.set_Vendor(vendor)
            os_fingerprintattr = attributeHost.set_OSFingerprint(os_fingerprint)
            os_fingerprintedattr = attributeHost.set_OSFingerprintd(os_fingerprinted)
            ip4attr = attributeNetAddr.set_IPv4Address(ip4)
            ip6attr = attributeNetAddr.set_IPv6Address(ip6)
            macattr = attributeNetAddr.set_MACAddress(mac)
            mkvps = {}
            mkvps.update(uptimeattr)
            mkvps.update(lastbootattr)
            mkvps.update(vendorattr)
            mkvps.update(os_fingerprintattr)
            mkvps.update(os_fingerprintedattr)
            mkvps.update(ip4attr)
            mkvps.update(ip6attr)
            mkvps.update(macattr)
            # add incoming to new document
            hce = GraphDB.CreateEntry(vertexCollection, mkvps)

    def returnKeysForNetAddrIp4(jsonmsgbody_data):
        keysDict = {}        
        hostsCol = db.collection(vertexCollection)
        if jsonmsgbody_data['NAVRIE_CollectionType'] == "NAVRIE_Host":
            ip4 = jsonmsgbody_data['ip4Address']
            for hostsCol in hostsCol.find({'NetworkAddress_IPv4Address': ip4}):
#                key = hostsCol['_key']
                key = hostsCol['_id']
                keysDict.update({key: ip4})
            return keysDict
        return {}