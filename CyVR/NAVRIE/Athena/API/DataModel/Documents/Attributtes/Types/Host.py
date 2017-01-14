import logging
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.AttributeTools import AttributeTools

class Host(object):
    """description of class"""

    def set_HostName(value):
        attribute = AttributeTools.setAttribute("Host_HostName", value)
        return attribute

    def set_LastBoot(value):
        attribute = AttributeTools.setAttribute("Host_LastBoot", value)
        return attribute

    def set_Uptime(value):
        attribute = AttributeTools.setAttribute("Host_Uptime", value)
        return attribute

    def set_Vendor(value):
        attribute = AttributeTools.setAttribute("Host_Vendor", value)
        return attribute

    def set_OSFingerprint(value):
        attribute = AttributeTools.setAttribute("Host_OSFingerprint", value)
        return attribute

    def set_OSFingerprintd(value):
        attribute = AttributeTools.setAttribute("Host_OSFingerprintd", value)
        return attribute