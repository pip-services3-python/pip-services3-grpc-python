# -*- coding: utf-8 -*-

from concurrent.futures import Future
from typing import Any

from pip_services3_grpc.protos.commandable_pb2 import InvokeRequest

from pip_services3_grpc.clients.GrpcClient import GrpcClient


class TestGrpcClient(GrpcClient):
    """
    GRPC client used for automated testing.
    """

    def __init__(self, client_name: str):
        super().__init__(client_name)

    def call(self, method: str, client: Any, request: Any) -> Any:
        """
        Calls a remote method via GRPC protocol.

        :param method: a method name to called
        :param client: current client
        :param request: (optional) request object.
        :return: the received result.
        """
        return super(TestGrpcClient, self).call(method, client, request)