import logging
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.AttributeTools import AttributeTools

class NetworkAddress(object):
    """description of class"""

    def set_Address(value):
        attribute = AttributeTools.setAttribute("NetworkAddress_Address", value)
        return attribute

    def set_IPv4Address(value):
        attribute = AttributeTools.setAttribute("NetworkAddress_IPv4Address", value)
        return attribute

    def set_IPv6Address(value):
        attribute = AttributeTools.setAttribute("NetworkAddress_IPv6Address", value)
        return attribute

    def set_MACAddress(value):
        attribute = AttributeTools.setAttribute("NetworkAddress_MACAddress", value)
        return attribute

    def set_FQDN(value):
        attribute = AttributeTools.setAttribute("NetworkAddress_FQDN", value)
        return attribute

    def set_SubDomain(value):
        attribute = AttributeTools.setAttribute("NetworkAddress_SubDomain", value)
        return attribute

    def set_URL(value):
        attribute = AttributeTools.setAttribute("NetworkAddress_URL", value)
        return attribute



    
