import logging
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.AttributeTools import AttributeTools

class Scope(object):
    """description of class"""

    def set_WindowStart(unixtimestamp):
        attribute = AttributeTools.setAttribute("Scope_WindowStart", unixtimestamp)
        return attribute

    def set_WindowEnd(unixtimestamp):
        attribute = AttributeTools.setAttribute("Scope_WindowEnd", unixtimestamp)
        return attribute

    def set_InScope(inScopeBool):
        attribute = AttributeTools.setAttribute("Scope_InScope", inScopeBool)
        return attribute

