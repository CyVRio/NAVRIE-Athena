from CyVR.NAVRIE.Athena.API.MessageQueueRecieve import MessageQueueRecieve
from CyVR.NAVRIE.Athena.Lib.GraphDB import GraphDB

MessageQueueRecieve()
uuid = ReturnUUIDForKeyValueInCollection("NetworkAddresses", "NetworkAddress_Address", "8.8.8.8")

print(uuid)
