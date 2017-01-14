import logging
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.AttributeTools import AttributeTools

class Port(object):
    """description of class"""

    def PortNumber(value):
        attribute = AttributeTools.setAttribute("Port_Number", value)
        return attribute

    def PortStatus_Open():
        attribute = AttributeTools.setAttribute("Port_Status", "Open")
        return attribute

    def PortStatus_Closed():
        attribute = AttributeTools.setAttribute("Port_Status", "Closed")
        return attribute

    def PortStatus_Filtered():
        attribute = AttributeTools.setAttribute("Port_Status", "Filtered")
        return attribute
