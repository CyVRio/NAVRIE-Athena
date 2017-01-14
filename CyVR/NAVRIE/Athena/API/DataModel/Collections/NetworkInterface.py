from marshmallow import Schema
from marshmallow.fields import String, Date, Integer, Boolean, UUID, DateTime

class NetworkInterface(Collection):
    """description of class"""



    """
     returns CSV output as text

     Example :
     host;hostname;hostname_type;protocol;port;name;state;product;extrainfo;reason;version;conf;cpe
     127.0.0.1;localhost;PTR;tcp;22;ssh;open;OpenSSH;protocol 2.0;syn-ack;5.9p1 Debian 5ubuntu1;10;cpe
        127.0.0.1;localhost;PTR;tcp;23;telnet;closed;;;conn-refused;;3;
        127.0.0.1;localhost;PTR;tcp;24;priv-mail;closed;;;conn-refused;;3;
        """

    """description of class"""

    __collection__ = 'NAVRIE_BuiltIn_NetworkInterfaces'

    class _Schema(Schema):
        _key = String(required=True)  # registration number
        Created = String(required=True)
        LastUpdated = String(required=True)
        InScope = Boolean(required=False)
        LastKnownStatus = String(required=False)
        Description = String(required=False)
        HostName = String(required=False)
        set_IPv6 = String(required=False)
        set_IPv4Address = String(required=False)
        set_MAC = String(required=False)
        set_DLCI = String(required=False)
        set_VPI = String(required=False)
        set_VCI = String(required=False)
        set_MPLS_Label = String(required=False)
        set_VLAN_Tag = String(required=False)

    def __str__(self):
        return "<NetworkInterface({})>".format(self.name)
