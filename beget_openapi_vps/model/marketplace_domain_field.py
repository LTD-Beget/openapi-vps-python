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


class MarketplaceDomainField(
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
            allow_tech_domain = schemas.BoolSchema
            __annotations__ = {
                "common": common,
                "allow_tech_domain": allow_tech_domain,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["common"]) -> 'MarketplaceFieldCommon': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allow_tech_domain"]) -> MetaOapg.properties.allow_tech_domain: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["common", "allow_tech_domain", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["common"]) -> typing.Union['MarketplaceFieldCommon', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allow_tech_domain"]) -> typing.Union[MetaOapg.properties.allow_tech_domain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["common", "allow_tech_domain", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        common: typing.Union['MarketplaceFieldCommon', schemas.Unset] = schemas.unset,
        allow_tech_domain: typing.Union[MetaOapg.properties.allow_tech_domain, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MarketplaceDomainField':
        return super().__new__(
            cls,
            *args,
            common=common,
            allow_tech_domain=allow_tech_domain,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_vps.model.marketplace_field_common import MarketplaceFieldCommon
