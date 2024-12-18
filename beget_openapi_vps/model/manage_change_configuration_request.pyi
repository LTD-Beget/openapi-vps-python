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


class ManageChangeConfigurationRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            configuration_id = schemas.StrSchema
        
            @staticmethod
            def configuration_params() -> typing.Type['StructuresConfigurationParams']:
                return StructuresConfigurationParams
            __annotations__ = {
                "id": id,
                "configuration_id": configuration_id,
                "configuration_params": configuration_params,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configuration_id"]) -> MetaOapg.properties.configuration_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configuration_params"]) -> 'StructuresConfigurationParams': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "configuration_id", "configuration_params", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configuration_id"]) -> typing.Union[MetaOapg.properties.configuration_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configuration_params"]) -> typing.Union['StructuresConfigurationParams', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "configuration_id", "configuration_params", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        configuration_id: typing.Union[MetaOapg.properties.configuration_id, str, schemas.Unset] = schemas.unset,
        configuration_params: typing.Union['StructuresConfigurationParams', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ManageChangeConfigurationRequest':
        return super().__new__(
            cls,
            *args,
            id=id,
            configuration_id=configuration_id,
            configuration_params=configuration_params,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_vps.model.structures_configuration_params import StructuresConfigurationParams
