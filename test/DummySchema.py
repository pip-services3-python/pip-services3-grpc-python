# -*- coding: utf-8 -*-

from pip_services3_commons.convert.TypeCode import TypeCode
from pip_services3_commons.validate.ObjectSchema import ObjectSchema


class DummySchema(ObjectSchema):

    def __init__(self):
        super().__init__()
        # TODO add TypeCodes
        self.with_optional_property("id", None)
        self.with_required_property("key", None)
        self.with_optional_property("content", None)
