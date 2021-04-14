# -*- coding: utf-8 -*-

from abc import ABC

from pip_services3_commons.commands.CommandSet import CommandSet

from .GrpcService import GrpcService


class CommandableGrpcService(GrpcService, ABC):
    """
    Abstract service that receives commands via GRPC protocol
    to operations automatically generated for commands defined in :class:`ICommandable <pip_services3_commons.commands.ICommandable.ICommandable>`.
    Each command is exposed as invoke method that receives command name and parameters.

    Commandable services require only 3 lines of code to implement a robust external
    GRPC-based remote interface.

     ### Configuration parameters ###
    - dependencies:
        - endpoint:              override for HTTP Endpoint dependency
        - controller:            override for Controller dependency
    - connection(s):
        - discovery_key:         (optional) a key to retrieve the connection from :class:`IDiscovery <pip_services3_components.connect.IDiscovery.IDiscovery>`
        - protocol:              connection protocol: http or https
        - host:                  host name or IP address
        - port:                  port number
        - uri:                   resource URI or connection string with all parameters in it

        ### References ###
        - `*:logger:*:*:1.0`           (optional) :class:`ILogger <pip_services3_components.log.ILogger.ILogger>` components to pass log messages
        - `*:counters:*:*:1.0`         (optional) :class:`ICounters <pip_services3_components.count.ICounters.ICounters>` components to pass collected measurements
        - `*:discovery:*:*:1.0`        (optional) :class:`IDiscovery <pip_services3_components.connect.IDiscovery.IDiscovery>` services to resolve connection
        - `*:endpoint:grpc:*:1.0`      (optional) :class:`GrpcEndpoint <pip_services3_grpc.services.GrpcEndpoint.GrpcEndpoint` reference

    See :class:`CommandableGrpcClient <pip_services3_grpc.clients.CommandableGrpcClient.CommandableGrpcClient`,
    :class:`GrpcService <pip_services3_grpc.services.GrpcService.GrpcService`

    .. code-block:: python

        class MyCommandableGrpcService(CommandableGrpcService):
           def __init__(self):
              super().__init__()

              self._dependency_resolver.put(
                    "controller",
                    Descriptor("mygroup","controller","*","*","1.0")
              )

        service = MyCommandableGrpcService()
        service.configure(ConfigParams.from_tuples(
            "connection.protocol", "http",
            "connection.host", "localhost",
            "connection.port", 8080
        ))
        service.set_references(References.from_tuples(
            Descriptor("mygroup","controller","default","default","1.0"), controller
        ))
        service.open("123")

    """

    def __init__(self, name: str):
        """
        Creates a new instance of the service.

        :param name: a service name.
        """
        super().__init__(None)
        self.__name = name
        self.__command_set: CommandSet = None
        self._dependency_resolver.put('controller', 'none')

    def register(self):
        """
        Registers all service routes in gRPC endpoint.
        Call automaticaly in open component procedure

        """
        controller = self._dependency_resolver.get_one_required('controller')
        self.__command_set = controller.get_command_set()

        commands = self.__command_set.get_commands()

        for index in range(0, len(commands)):
            command = commands[index]
            method = '' + self.__name + '.' + command.get_name()

            def inner(correlation_id, args, getted_method):
                for _index in range(0, len(commands)):
                    _command = commands[_index]
                    _method = '' + self.__name + '.' + _command.get_name()
                    if getted_method == _method:
                        timing = self._instrument(correlation_id, _method)

                        try:
                            result = _command.execute(correlation_id, args)
                            timing.end_timing()
                            return result
                        except Exception as ex:
                            timing.end_timing()
                            self._instrument_error(correlation_id, _method, ex, True)

            self.register_commadable_method(method, None, inner)
