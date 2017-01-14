import logging
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.AttributeTools import AttributeTools

class Application(object):
    """description of class"""

    def set_ServiceName(serviceName):
        attribute = AttributeTools.setAttribute("Service_Name", serviceName)
        return attribute

    def set_Banner(banner):
        attribute = AttributeTools.setAttribute("Service_Banner", banner)
        return attribute

    def set_DefaultPortNumber(port):
        attribute = AttributeTools.setAttribute("Service_DefaultPortNumber", port)
        return attribute

    def set_DefaultPortProtocol(protocol):
        attribute = AttributeTools.setAttribute("Service_DefaultPortProtocol", protocol)
        return attribute

