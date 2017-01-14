#!/usr/bin/python
import logging

class DatabaseInfo(object):
    """Establish a connection to ArangoDB"""

    arangodbprotocol = "http"
    arangodbhost = "localhost"
    arangodbport = "8529"
    arangodbuser = "navrie"
    arangodbpw = "navrie"
    arangodbdatabasename = "navrie"
    arangodbGraphName = "navrie"

    def setDatabaseProtocol(graphName):
        DatabaseInfo.arangodbGraphName = graphName

    def setDatabaseProtocol(arangodbprotocol):
        DatabaseInfo.arangodbprotocol = arangodbprotocol

    def setDatabaseHost(arangodbhost):
        DatabaseInfo.arangodbhost = arangodbhost

    def setDatabasePort(arangodbport):
        DatabaseInfo.arangodbport = arangodbport

    def setDatabaseUser(arangodbuser):
        DatabaseInfo.arangodbuser = arangodbuser

    def setDatabasePW(arangodbpw):
        DatabaseInfo.arangodbpw = arangodbpw

    def setDatabaseName(arangodbdatabasename):
        DatabaseInfo.arangodbdatabasename = arangodbdatabasename

    def getDatabaseProtocol():
        return DatabaseInfo.arangodbprotocol

    def getDatabaseHost():
        return DatabaseInfo.arangodbhost

    def getDatabasePort():
        return DatabaseInfo.arangodbport

    def getDatabaseUser():
        return DatabaseInfo.arangodbuser

    def getGraphName():
        return DatabaseInfo.arangodbGraphName

    def getDatabasePW():
        return DatabaseInfo.arangodbpw

    def getDatabaseName():
        return DatabaseInfo.arangodbdatabasename
