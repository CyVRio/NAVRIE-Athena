class NetworkInterface(object):
    """description of class"""

    def __init__(self, runTimestamp, created, lastUpdated, inScope,  lastKnownStatus,  description,  hostName,  set_IPv6,  set_IPv4,  set_MAC,  set_DLCI,  set_VPI,  set_VCI,  set_MPLS_Label, set_VLAN_Tag):
        self.runTimestamp = runTimestamp
        self.created = created
        self.lastUpdated = lastUpdated
        self.inScope = inScope
        self.lastKnownStatus = lastKnownStatus
        self.description = description
        self.hostName = hostName
        self.set_IPv6 = set_IPv6
        self.set_IPv4 = set_IPv4
        self.set_MAC = set_MAC
        self.set_DLCI = set_DLCI
        self.set_VPI = set_VPI
        self.set_VCI = set_VCI
        self.set_MPLS_Label = set_MPLS_Label
        self.set_VLAN_Tag = set_VLAN_Tag
