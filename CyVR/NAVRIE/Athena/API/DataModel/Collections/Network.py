from marshmallow import Schema
from marshmallow.fields import String, Date, Integer, Boolean

class NetworkInterface(object):
    """description of class"""


    __collection__ = 'NAVRIE_BuiltIn_Network'



    class _Schema(Schema):
        _key = String(required=True)  # registration number
        Network_Name = String(required=True, allow_none=False)
        Network_SSID = String(required=False)
        Network_Password = String(required=False)
        Network_Type = String(required=False)
        Network_IPRange = String(required=False)
        Network_Subnet = String(required=False)
        Network_Internal = Boolean(required=False)

    def __str__(self):
        return "<Network({})>".format(self.name)
