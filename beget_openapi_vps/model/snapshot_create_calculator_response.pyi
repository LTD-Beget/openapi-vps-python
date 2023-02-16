# coding: utf-8

"""
    API Облачных серверов

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.4.1
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


class SnapshotCreateCalculatorResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            price_day = schemas.Float64Schema
            price_day_gb = schemas.Float64Schema
            size = schemas.IntSchema
            __annotations__ = {
                "price_day": price_day,
                "price_day_gb": price_day_gb,
                "size": size,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price_day"]) -> MetaOapg.properties.price_day: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price_day_gb"]) -> MetaOapg.properties.price_day_gb: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["price_day", "price_day_gb", "size", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price_day"]) -> typing.Union[MetaOapg.properties.price_day, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price_day_gb"]) -> typing.Union[MetaOapg.properties.price_day_gb, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> typing.Union[MetaOapg.properties.size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["price_day", "price_day_gb", "size", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        price_day: typing.Union[MetaOapg.properties.price_day, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        price_day_gb: typing.Union[MetaOapg.properties.price_day_gb, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        size: typing.Union[MetaOapg.properties.size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SnapshotCreateCalculatorResponse':
        return super().__new__(
            cls,
            *args,
            price_day=price_day,
            price_day_gb=price_day_gb,
            size=size,
            _configuration=_configuration,
            **kwargs,
        )
