# coding: utf-8

"""
    API Облачных серверов

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.2.1
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


class StructuresSoftwareCategory(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            sys_name = schemas.StrSchema
            name = schemas.StrSchema
            name_en = schemas.StrSchema
            is_main = schemas.BoolSchema
            __annotations__ = {
                "sys_name": sys_name,
                "name": name,
                "name_en": name_en,
                "is_main": is_main,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sys_name"]) -> MetaOapg.properties.sys_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name_en"]) -> MetaOapg.properties.name_en: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_main"]) -> MetaOapg.properties.is_main: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["sys_name", "name", "name_en", "is_main", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sys_name"]) -> typing.Union[MetaOapg.properties.sys_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name_en"]) -> typing.Union[MetaOapg.properties.name_en, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_main"]) -> typing.Union[MetaOapg.properties.is_main, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sys_name", "name", "name_en", "is_main", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        sys_name: typing.Union[MetaOapg.properties.sys_name, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        name_en: typing.Union[MetaOapg.properties.name_en, str, schemas.Unset] = schemas.unset,
        is_main: typing.Union[MetaOapg.properties.is_main, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StructuresSoftwareCategory':
        return super().__new__(
            cls,
            *args,
            sys_name=sys_name,
            name=name,
            name_en=name_en,
            is_main=is_main,
            _configuration=_configuration,
            **kwargs,
        )
