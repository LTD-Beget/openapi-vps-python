# coding: utf-8

"""
    API Облачных серверов

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.4.0
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


class ConfiguratorGetConfiguratorInfoResponse(
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
            is_available = schemas.BoolSchema
            __annotations__ = {
                "settings": settings,
                "is_available": is_available,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["settings"]) -> 'ConfiguratorConfiguratorSettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_available"]) -> MetaOapg.properties.is_available: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["settings", "is_available", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["settings"]) -> typing.Union['ConfiguratorConfiguratorSettings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_available"]) -> typing.Union[MetaOapg.properties.is_available, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["settings", "is_available", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        settings: typing.Union['ConfiguratorConfiguratorSettings', schemas.Unset] = schemas.unset,
        is_available: typing.Union[MetaOapg.properties.is_available, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConfiguratorGetConfiguratorInfoResponse':
        return super().__new__(
            cls,
            *args,
            settings=settings,
            is_available=is_available,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_vps.model.configurator_configurator_settings import ConfiguratorConfiguratorSettings