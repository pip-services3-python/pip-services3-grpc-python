# -*- coding: utf-8 -*-

from abc import ABC


class IDummyController(ABC):
    def get_page_by_filter(self, correlation_id, filterr, paging):
        pass

    def get_one_by_id(self, correlation_id, id):
        pass

    def create(self, correlation_id, entity):
        pass

    def update(self, correlation_id, entity):
        pass

    def delete_by_id(self, correlation_id, id):
        pass
