# coding: utf-8

"""
    API Облачных серверов

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.6.1
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


class MarketplacePasswordField(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def common() -> typing.Type['MarketplaceFieldCommon']:
                return MarketplaceFieldCommon
            auto_generated = schemas.BoolSchema
            __annotations__ = {
                "common": common,
                "auto_generated": auto_generated,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["common"]) -> 'MarketplaceFieldCommon': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_generated"]) -> MetaOapg.properties.auto_generated: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["common", "auto_generated", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["common"]) -> typing.Union['MarketplaceFieldCommon', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_generated"]) -> typing.Union[MetaOapg.properties.auto_generated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["common", "auto_generated", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        common: typing.Union['MarketplaceFieldCommon', schemas.Unset] = schemas.unset,
        auto_generated: typing.Union[MetaOapg.properties.auto_generated, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MarketplacePasswordField':
        return super().__new__(
            cls,
            *args,
            common=common,
            auto_generated=auto_generated,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_vps.model.marketplace_field_common import MarketplaceFieldCommon
