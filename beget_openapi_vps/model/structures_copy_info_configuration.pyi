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


class StructuresCopyInfoConfiguration(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            cpu_count = schemas.IntSchema
            disk_size = schemas.IntSchema
            memory = schemas.IntSchema
            __annotations__ = {
                "cpu_count": cpu_count,
                "disk_size": disk_size,
                "memory": memory,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cpu_count"]) -> MetaOapg.properties.cpu_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disk_size"]) -> MetaOapg.properties.disk_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["memory"]) -> MetaOapg.properties.memory: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cpu_count", "disk_size", "memory", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cpu_count"]) -> typing.Union[MetaOapg.properties.cpu_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disk_size"]) -> typing.Union[MetaOapg.properties.disk_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["memory"]) -> typing.Union[MetaOapg.properties.memory, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cpu_count", "disk_size", "memory", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cpu_count: typing.Union[MetaOapg.properties.cpu_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        disk_size: typing.Union[MetaOapg.properties.disk_size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        memory: typing.Union[MetaOapg.properties.memory, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StructuresCopyInfoConfiguration':
        return super().__new__(
            cls,
            *args,
            cpu_count=cpu_count,
            disk_size=disk_size,
            memory=memory,
            _configuration=_configuration,
            **kwargs,
        )
