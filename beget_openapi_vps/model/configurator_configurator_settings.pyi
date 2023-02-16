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


class ConfiguratorConfiguratorSettings(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def cpu_settings() -> typing.Type['ConfiguratorCpuSettings']:
                return ConfiguratorCpuSettings
        
            @staticmethod
            def disk_settings() -> typing.Type['ConfiguratorDiskSettings']:
                return ConfiguratorDiskSettings
        
            @staticmethod
            def memory_settings() -> typing.Type['ConfiguratorMemorySettings']:
                return ConfiguratorMemorySettings
            __annotations__ = {
                "cpu_settings": cpu_settings,
                "disk_settings": disk_settings,
                "memory_settings": memory_settings,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cpu_settings"]) -> 'ConfiguratorCpuSettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disk_settings"]) -> 'ConfiguratorDiskSettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["memory_settings"]) -> 'ConfiguratorMemorySettings': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cpu_settings", "disk_settings", "memory_settings", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cpu_settings"]) -> typing.Union['ConfiguratorCpuSettings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disk_settings"]) -> typing.Union['ConfiguratorDiskSettings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["memory_settings"]) -> typing.Union['ConfiguratorMemorySettings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cpu_settings", "disk_settings", "memory_settings", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cpu_settings: typing.Union['ConfiguratorCpuSettings', schemas.Unset] = schemas.unset,
        disk_settings: typing.Union['ConfiguratorDiskSettings', schemas.Unset] = schemas.unset,
        memory_settings: typing.Union['ConfiguratorMemorySettings', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConfiguratorConfiguratorSettings':
        return super().__new__(
            cls,
            *args,
            cpu_settings=cpu_settings,
            disk_settings=disk_settings,
            memory_settings=memory_settings,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_vps.model.configurator_cpu_settings import ConfiguratorCpuSettings
from beget_openapi_vps.model.configurator_disk_settings import ConfiguratorDiskSettings
from beget_openapi_vps.model.configurator_memory_settings import ConfiguratorMemorySettings
