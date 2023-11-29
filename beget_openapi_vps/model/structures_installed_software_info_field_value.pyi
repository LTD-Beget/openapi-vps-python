# coding: utf-8

"""
    API Облачных серверов

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.6.0
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


class StructuresInstalledSoftwareInfoFieldValue(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            label_ru = schemas.StrSchema
            label_en = schemas.StrSchema
            value = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def UNKNOWN(cls):
                    return cls("UNKNOWN")
                
                @schemas.classproperty
                def DOMAIN(cls):
                    return cls("DOMAIN")
                
                @schemas.classproperty
                def TEXT(cls):
                    return cls("TEXT")
                
                @schemas.classproperty
                def EMAIL(cls):
                    return cls("EMAIL")
                
                @schemas.classproperty
                def PASSWORD(cls):
                    return cls("PASSWORD")
            variable = schemas.StrSchema
            __annotations__ = {
                "label_ru": label_ru,
                "label_en": label_en,
                "value": value,
                "type": type,
                "variable": variable,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label_ru"]) -> MetaOapg.properties.label_ru: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label_en"]) -> MetaOapg.properties.label_en: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["variable"]) -> MetaOapg.properties.variable: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["label_ru", "label_en", "value", "type", "variable", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label_ru"]) -> typing.Union[MetaOapg.properties.label_ru, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label_en"]) -> typing.Union[MetaOapg.properties.label_en, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["variable"]) -> typing.Union[MetaOapg.properties.variable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["label_ru", "label_en", "value", "type", "variable", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        label_ru: typing.Union[MetaOapg.properties.label_ru, str, schemas.Unset] = schemas.unset,
        label_en: typing.Union[MetaOapg.properties.label_en, str, schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        variable: typing.Union[MetaOapg.properties.variable, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StructuresInstalledSoftwareInfoFieldValue':
        return super().__new__(
            cls,
            *args,
            label_ru=label_ru,
            label_en=label_en,
            value=value,
            type=type,
            variable=variable,
            _configuration=_configuration,
            **kwargs,
        )
