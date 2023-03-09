# coding: utf-8

"""
    API Облачных серверов

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.5.1
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from beget_openapi_vps import schemas  # noqa: F401


class StatisticGetProcessListResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def processes() -> typing.Type['StatisticGetProcessListResponseProcessList']:
                return StatisticGetProcessListResponseProcessList
        
            @staticmethod
            def error() -> typing.Type['StatisticGetProcessListResponseError']:
                return StatisticGetProcessListResponseError
            __annotations__ = {
                "processes": processes,
                "error": error,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["processes"]) -> 'StatisticGetProcessListResponseProcessList': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> 'StatisticGetProcessListResponseError': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["processes", "error", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["processes"]) -> typing.Union['StatisticGetProcessListResponseProcessList', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union['StatisticGetProcessListResponseError', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["processes", "error", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        processes: typing.Union['StatisticGetProcessListResponseProcessList', schemas.Unset] = schemas.unset,
        error: typing.Union['StatisticGetProcessListResponseError', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StatisticGetProcessListResponse':
        return super().__new__(
            cls,
            *args,
            processes=processes,
            error=error,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_vps.model.statistic_get_process_list_response_error import StatisticGetProcessListResponseError
from beget_openapi_vps.model.statistic_get_process_list_response_process_list import StatisticGetProcessListResponseProcessList
