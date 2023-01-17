# coding: utf-8

"""
    API Облачных серверов

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.3.0
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


class StatisticGetNetworkResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def data_rx() -> typing.Type['StatisticSeriesData']:
                return StatisticSeriesData
        
            @staticmethod
            def data_tx() -> typing.Type['StatisticSeriesData']:
                return StatisticSeriesData
        
            @staticmethod
            def data_rx_private() -> typing.Type['StatisticSeriesData']:
                return StatisticSeriesData
        
            @staticmethod
            def data_tx_private() -> typing.Type['StatisticSeriesData']:
                return StatisticSeriesData
            __annotations__ = {
                "data_rx": data_rx,
                "data_tx": data_tx,
                "data_rx_private": data_rx_private,
                "data_tx_private": data_tx_private,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data_rx"]) -> 'StatisticSeriesData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data_tx"]) -> 'StatisticSeriesData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data_rx_private"]) -> 'StatisticSeriesData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data_tx_private"]) -> 'StatisticSeriesData': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data_rx", "data_tx", "data_rx_private", "data_tx_private", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data_rx"]) -> typing.Union['StatisticSeriesData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data_tx"]) -> typing.Union['StatisticSeriesData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data_rx_private"]) -> typing.Union['StatisticSeriesData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data_tx_private"]) -> typing.Union['StatisticSeriesData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data_rx", "data_tx", "data_rx_private", "data_tx_private", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data_rx: typing.Union['StatisticSeriesData', schemas.Unset] = schemas.unset,
        data_tx: typing.Union['StatisticSeriesData', schemas.Unset] = schemas.unset,
        data_rx_private: typing.Union['StatisticSeriesData', schemas.Unset] = schemas.unset,
        data_tx_private: typing.Union['StatisticSeriesData', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StatisticGetNetworkResponse':
        return super().__new__(
            cls,
            *args,
            data_rx=data_rx,
            data_tx=data_tx,
            data_rx_private=data_rx_private,
            data_tx_private=data_tx_private,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_vps.model.statistic_series_data import StatisticSeriesData
