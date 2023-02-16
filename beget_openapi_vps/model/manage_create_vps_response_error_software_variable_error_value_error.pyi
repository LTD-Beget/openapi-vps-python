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


class ManageCreateVpsResponseErrorSoftwareVariableErrorValueError(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            variable = schemas.StrSchema
            error_text_ru = schemas.StrSchema
            error_text_en = schemas.StrSchema
            __annotations__ = {
                "variable": variable,
                "error_text_ru": error_text_ru,
                "error_text_en": error_text_en,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["variable"]) -> MetaOapg.properties.variable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error_text_ru"]) -> MetaOapg.properties.error_text_ru: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error_text_en"]) -> MetaOapg.properties.error_text_en: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["variable", "error_text_ru", "error_text_en", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["variable"]) -> typing.Union[MetaOapg.properties.variable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error_text_ru"]) -> typing.Union[MetaOapg.properties.error_text_ru, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error_text_en"]) -> typing.Union[MetaOapg.properties.error_text_en, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["variable", "error_text_ru", "error_text_en", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        variable: typing.Union[MetaOapg.properties.variable, str, schemas.Unset] = schemas.unset,
        error_text_ru: typing.Union[MetaOapg.properties.error_text_ru, str, schemas.Unset] = schemas.unset,
        error_text_en: typing.Union[MetaOapg.properties.error_text_en, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ManageCreateVpsResponseErrorSoftwareVariableErrorValueError':
        return super().__new__(
            cls,
            *args,
            variable=variable,
            error_text_ru=error_text_ru,
            error_text_en=error_text_en,
            _configuration=_configuration,
            **kwargs,
        )
