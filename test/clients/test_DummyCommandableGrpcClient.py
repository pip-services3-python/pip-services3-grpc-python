# -*- coding: utf-8 -*-

from pip_services3_commons.config.ConfigParams import ConfigParams
from pip_services3_commons.refer.Descriptor import Descriptor
from pip_services3_commons.refer.References import References

from .DummyClientFixture import DummyClientFixture
from .DummyCommandableGrpcClient import DummyCommandableGrpcClient
from ..DummyController import DummyController
from ..services.DummyCommandableGrpcService import DummyCommandableGrpcService

grpc_config = ConfigParams.from_tuples(
    'connection.protocol',
    'http',
    'connection.host',
    'localhost',
    'connection.port',
    3002
)


class TestDummyCommandableGrpcClient:
    service = None
    client = None
    fixture = None

    @classmethod
    def setup_class(cls):
        ctrl = DummyController()

        cls.service = DummyCommandableGrpcService()
        cls.service.configure(grpc_config)

        references = References.from_tuples(
            Descriptor(
                'pip-services-dummies', 'controller', 'default', 'default', '1.0'),
            ctrl,
            Descriptor('pip-services-dummies', 'service', 'grpc', 'default', '1.0'),
            cls.service
        )

        cls.service.set_references(references)
        cls.service.open(None)

    @classmethod
    def teardown_class(cls):
        cls.service.close(None)

    def setup_method(self, method=None):
        self.client = DummyCommandableGrpcClient()
        self.fixture = DummyClientFixture(self.client)

        self.client.configure(grpc_config)
        self.client.set_references(References())
        self.client.open(None)

    def test_crud_operations(self):
        self.fixture.test_crud_operations()
