# -*- coding: utf-8 -*-

from abc import ABC
from typing import Optional

from pip_services3_commons.data import FilterParams, PagingParams, DataPage
from test.Dummy import Dummy


class IDummyController(ABC):
    def get_page_by_filter(self, correlation_id: Optional[str], filter: FilterParams, paging: PagingParams) -> DataPage:
        pass

    def get_one_by_id(self, correlation_id: Optional[str], id: str) -> Dummy:
        pass

    def create(self, correlation_id: Optional[str], entity: Dummy) -> Dummy:
        pass

    def update(self, correlation_id: Optional[str], entity: Dummy) -> Dummy:
        pass

    def delete_by_id(self, correlation_id: Optional[str], id: str) -> Dummy:
        pass
