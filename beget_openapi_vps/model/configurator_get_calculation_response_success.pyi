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


class ConfiguratorGetCalculationResponseSuccess(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def settings() -> typing.Type['ConfiguratorConfiguratorSettings']:
                return ConfiguratorConfiguratorSettings
        
            @staticmethod
            def params() -> typing.Type['StructuresConfigurationParams']:
                return StructuresConfigurationParams
            price_day = schemas.Float64Schema
            price_month = schemas.Float64Schema
            __annotations__ = {
                "settings": settings,
                "params": params,
                "price_day": price_day,
                "price_month": price_month,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["settings"]) -> 'ConfiguratorConfiguratorSettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["params"]) -> 'StructuresConfigurationParams': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price_day"]) -> MetaOapg.properties.price_day: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price_month"]) -> MetaOapg.properties.price_month: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["settings", "params", "price_day", "price_month", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["settings"]) -> typing.Union['ConfiguratorConfiguratorSettings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["params"]) -> typing.Union['StructuresConfigurationParams', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price_day"]) -> typing.Union[MetaOapg.properties.price_day, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price_month"]) -> typing.Union[MetaOapg.properties.price_month, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["settings", "params", "price_day", "price_month", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        settings: typing.Union['ConfiguratorConfiguratorSettings', schemas.Unset] = schemas.unset,
        params: typing.Union['StructuresConfigurationParams', schemas.Unset] = schemas.unset,
        price_day: typing.Union[MetaOapg.properties.price_day, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        price_month: typing.Union[MetaOapg.properties.price_month, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConfiguratorGetCalculationResponseSuccess':
        return super().__new__(
            cls,
            *args,
            settings=settings,
            params=params,
            price_day=price_day,
            price_month=price_month,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_vps.model.configurator_configurator_settings import ConfiguratorConfiguratorSettings
from beget_openapi_vps.model.structures_configuration_params import StructuresConfigurationParams
