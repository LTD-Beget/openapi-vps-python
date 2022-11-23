# coding: utf-8

"""
    API Облачных серверов

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.2.0
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


class StatisticGetDiskResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def data_read() -> typing.Type['StatisticSeriesData']:
                return StatisticSeriesData
        
            @staticmethod
            def data_write() -> typing.Type['StatisticSeriesData']:
                return StatisticSeriesData
            __annotations__ = {
                "data_read": data_read,
                "data_write": data_write,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data_read"]) -> 'StatisticSeriesData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data_write"]) -> 'StatisticSeriesData': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data_read", "data_write", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data_read"]) -> typing.Union['StatisticSeriesData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data_write"]) -> typing.Union['StatisticSeriesData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data_read", "data_write", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data_read: typing.Union['StatisticSeriesData', schemas.Unset] = schemas.unset,
        data_write: typing.Union['StatisticSeriesData', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StatisticGetDiskResponse':
        return super().__new__(
            cls,
            *args,
            data_read=data_read,
            data_write=data_write,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_vps.model.statistic_series_data import StatisticSeriesData