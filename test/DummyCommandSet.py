# -*- coding: utf-8 -*-

from pip_services3_commons.commands.CommandSet import CommandSet
from pip_services3_commons.commands.ICommand import ICommand
from pip_services3_commons.commands.Command import Command
from pip_services3_commons.run.Parameters import Parameters
from pip_services3_commons.data.FilterParams import FilterParams
from pip_services3_commons.data.PagingParams import PagingParams
from pip_services3_commons.validate.ObjectSchema import ObjectSchema
from pip_services3_commons.convert.TypeCode import TypeCode
from pip_services3_commons.validate.FilterParamsSchema import FilterParamsSchema
from pip_services3_commons.validate.PagingParamsSchema import PagingParamsSchema

from .Dummy import Dummy
from .IDummyController import IDummyController
from .DummySchema import DummySchema


class DummyCommandSet(CommandSet):
    # TODO add TypeCodes for methods

    def __init__(self, controller):
        super().__init__()
        self.__controller = controller

        self.add_command(self.__make_page_by_filter_command())
        self.add_command(self._make_get_one_by_id_command())
        self.add_command(self._make_create_command())
        self.add_command(self._make_update_command())
        self.add_command(self._make_delete_by_id_command())

    def __make_page_by_filter_command(self):
        def handler(correlation_id, args):
            filter = FilterParams.from_value(args.get("filter"))
            paging = PagingParams.from_value(args.get("paging"))
            return self.__controller.get_page_by_filter(correlation_id, filter, paging)

        # TODO: add FilterParamsSchema and PagingParamsSchema
        return Command(
            'get_dummies',
            ObjectSchema().with_optional_property(
                'filter', None).with_optional_property(
                'paging', None),
            handler
        )

    def _make_get_one_by_id_command(self):
        def handler(correlation_id, args):
            id = args.get_as_string("dummy_id")
            return self.__controller.get_one_by_id(correlation_id, id)

        return Command(
            "get_dummy_by_id",
            ObjectSchema().with_required_property('dummy_id', None),
            handler
        )

    def _make_create_command(self):
        def handler(correlation_id, args):
            entity = args.get("dummy")
            return self.__controller.create(correlation_id, entity)

        return Command(
            "create_dummy",
            ObjectSchema().with_required_property('dummy', DummySchema()),
            handler
        )

    def _make_update_command(self):
        def handler(correlation_id, args):
            entity = args.get("dummy")
            return self.__controller.update(correlation_id, entity)

        return Command(
            "update_dummy",
            ObjectSchema().with_required_property('dummy', DummySchema()),
            handler
        )

    def _make_delete_by_id_command(self):
        def handler(correlation_id, args):
            id = args.get_as_string("dummy_id")
            return self.__controller.delete_by_id(correlation_id, id)

        return Command(
            "delete_dummy",
            ObjectSchema().with_required_property('dummy_id', None),
            handler
        )
