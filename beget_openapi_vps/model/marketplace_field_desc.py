# coding: utf-8

"""
    API Облачных серверов

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.3.0
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


class MarketplaceFieldDesc(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def password_field() -> typing.Type['MarketplacePasswordField']:
                return MarketplacePasswordField
        
            @staticmethod
            def domain_field() -> typing.Type['MarketplaceDomainField']:
                return MarketplaceDomainField
        
            @staticmethod
            def text_field() -> typing.Type['MarketplaceTextField']:
                return MarketplaceTextField
        
            @staticmethod
            def email_field() -> typing.Type['MarketplaceEmailField']:
                return MarketplaceEmailField
            __annotations__ = {
                "password_field": password_field,
                "domain_field": domain_field,
                "text_field": text_field,
                "email_field": email_field,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password_field"]) -> 'MarketplacePasswordField': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["domain_field"]) -> 'MarketplaceDomainField': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["text_field"]) -> 'MarketplaceTextField': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_field"]) -> 'MarketplaceEmailField': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["password_field", "domain_field", "text_field", "email_field", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password_field"]) -> typing.Union['MarketplacePasswordField', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["domain_field"]) -> typing.Union['MarketplaceDomainField', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["text_field"]) -> typing.Union['MarketplaceTextField', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_field"]) -> typing.Union['MarketplaceEmailField', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["password_field", "domain_field", "text_field", "email_field", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        password_field: typing.Union['MarketplacePasswordField', schemas.Unset] = schemas.unset,
        domain_field: typing.Union['MarketplaceDomainField', schemas.Unset] = schemas.unset,
        text_field: typing.Union['MarketplaceTextField', schemas.Unset] = schemas.unset,
        email_field: typing.Union['MarketplaceEmailField', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MarketplaceFieldDesc':
        return super().__new__(
            cls,
            *args,
            password_field=password_field,
            domain_field=domain_field,
            text_field=text_field,
            email_field=email_field,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_vps.model.marketplace_domain_field import MarketplaceDomainField
from beget_openapi_vps.model.marketplace_email_field import MarketplaceEmailField
from beget_openapi_vps.model.marketplace_password_field import MarketplacePasswordField
from beget_openapi_vps.model.marketplace_text_field import MarketplaceTextField
