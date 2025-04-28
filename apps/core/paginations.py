# -*- coding: utf-8 -*-
"""
paging structs module.
"""

from rest_framework.pagination import PageNumberPagination


class CorePagination(PageNumberPagination):
    """
    core pagination class.
    """

    page_size_query_param = 'page_size'


class LargePagination(CorePagination):
    """
    large pagination class.
    """

    page_size = 15


class MediumPagination(CorePagination):
    """
    medium pagination class.
    """

    page_size = 10


class SmallPagination(CorePagination):
    """
    small pagination class.
    """

    page_size = 5
