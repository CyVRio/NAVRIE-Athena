import logging
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.AttributeTools import AttributeTools

class Device(object):
    """description of class"""
    def setStatus_LastKnownStatus(value):
        if value == "Alive":
            setStatus_Alive()
        elif value == "Unknown":
            setStatus_Unknown()
        elif value == "Dead":
            setStatus_Dead()
        else:
            print("Invalid status, or status not set")

    def setStatus_Alive():
        attribute = AttributeTools.setAttribute("Device_Status", "Alive")
        return attribute

    def setStatus_Unknown():
        attribute = AttributeTools.setAttribute("Device_Status", "Unknown")
        return attribute

    def setStatus_Dead():
        attribute = AttributeTools.setAttribute("Device_Status", "Dead")
        return attribute
