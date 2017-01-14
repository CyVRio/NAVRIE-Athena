import logging
from pyArango.connection import *
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.AttributeTools import AttributeTools

class Time(object):
    """description of class"""

    def set_CreationTime(value):
        attribute = AttributeTools.setAttribute("Time_CreatedAt", value)
        return attribute

    def set_UpdatedAt(value):
        attribute = AttributeTools.setAttribute("Time_UpdatedAt", value)
        return attribute

    def set_Timestamp(value):
        attribute = AttributeTools.setAttribute("Time_Timestamp", value)
        return attribute

    def set_TimeZone(value):
        attribute = AttributeTools.setAttribute("Time_TimeZone", value)
        return attribute

    def set_SavingsTimeObservedTrue():
        attribute = AttributeTools.setAttribute("Time_SavingsTime", "True")
        return attribute

    def set_SavingsTimeObservedFalse():
        attribute = AttributeTools.setAttribute("Time_SavingsTime", "False")
        return attribute