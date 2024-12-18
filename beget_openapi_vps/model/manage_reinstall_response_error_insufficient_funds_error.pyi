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


class ManageReinstallResponseErrorInsufficientFundsError(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            current_balance = schemas.Float64Schema
            needed_balance = schemas.Float64Schema
            charge_on_add = schemas.BoolSchema
            __annotations__ = {
                "current_balance": current_balance,
                "needed_balance": needed_balance,
                "charge_on_add": charge_on_add,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_balance"]) -> MetaOapg.properties.current_balance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["needed_balance"]) -> MetaOapg.properties.needed_balance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["charge_on_add"]) -> MetaOapg.properties.charge_on_add: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["current_balance", "needed_balance", "charge_on_add", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_balance"]) -> typing.Union[MetaOapg.properties.current_balance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["needed_balance"]) -> typing.Union[MetaOapg.properties.needed_balance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["charge_on_add"]) -> typing.Union[MetaOapg.properties.charge_on_add, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["current_balance", "needed_balance", "charge_on_add", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        current_balance: typing.Union[MetaOapg.properties.current_balance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        needed_balance: typing.Union[MetaOapg.properties.needed_balance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        charge_on_add: typing.Union[MetaOapg.properties.charge_on_add, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ManageReinstallResponseErrorInsufficientFundsError':
        return super().__new__(
            cls,
            *args,
            current_balance=current_balance,
            needed_balance=needed_balance,
            charge_on_add=charge_on_add,
            _configuration=_configuration,
            **kwargs,
        )
