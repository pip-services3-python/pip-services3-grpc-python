# -*- coding: utf-8 -*-

from pip_services3_commons.data.IStringIdentifiable import IStringIdentifiable
from pip_services3_commons.data.ICloneable import ICloneable


class Dummy(IStringIdentifiable, dict):
    """
    Implement dict for json serialization
    """
    id = ''
    key = ''
    content = ''

    def __init__(self, id, key, content):

        dict.__init__(self, id=id, key=key, content=content)
        self.id = id
        self.key = key
        self.content = content

    def clone(self):
        return Dummy(self.id, self.key, self.content)

    @staticmethod
    def from_grpc_to_json(dummy):
        return {'id': dummy.id, 'key': dummy.key, 'content': dummy.content}
