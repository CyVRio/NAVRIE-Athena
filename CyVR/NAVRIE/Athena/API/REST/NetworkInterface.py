
from CyVR.NAVRIE.Athena.API.RESTApp import RESTApp
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Models.NetworkInterface import NetworkInterface

class NetworkInterface(object):
    """description of class"""

    @RESTApp.path(model=NetworkInterface, path='api/v1/NAVRIE/Athena/NetworkInterface/{id}')
    def get_document(id=0):
        return document_by_id(id)

        
    @RESTApp.json(model=NetworkInterface)
    def document_default(self, request):
        return {
            'type': 'NetworkInterface',
            'id': self.id,
            'runTimestamp': self.runTimestamp,
            'author': self.author,
            'content': self.content
        }


    @RESTApp.json(model=DocumentCollection, request_method='POST')
    def document_collection_post(self, request):
        json = request.json
        result = self.add(Document(title=json['RunTimestamp'],
                               author=json['author'],
                               content=json['content']))
        return request.view(result)
  