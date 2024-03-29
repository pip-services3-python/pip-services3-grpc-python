# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import commandable_pb2 as commandable__pb2


class CommandableStub(object):
    """The commandable service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.invoke = channel.unary_unary(
                '/commandable.Commandable/invoke',
                request_serializer=commandable__pb2.InvokeRequest.SerializeToString,
                response_deserializer=commandable__pb2.InvokeReply.FromString,
                )


class CommandableServicer(object):
    """The commandable service definition.
    """

    def invoke(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CommandableServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'invoke': grpc.unary_unary_rpc_method_handler(
                    servicer.invoke,
                    request_deserializer=commandable__pb2.InvokeRequest.FromString,
                    response_serializer=commandable__pb2.InvokeReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'commandable.Commandable', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Commandable(object):
    """The commandable service definition.
    """

    @staticmethod
    def invoke(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/commandable.Commandable/invoke',
            commandable__pb2.InvokeRequest.SerializeToString,
            commandable__pb2.InvokeReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
