# coding: utf-8

"""
    API Облачных серверов

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.2.0
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


class NetworkGetNetworkInfoResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class ip(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['StructuresIpInfo']:
                        return StructuresIpInfo
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['StructuresIpInfo'], typing.List['StructuresIpInfo']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ip':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'StructuresIpInfo':
                    return super().__getitem__(i)
            
            
            class additional_ip(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['StructuresAdditionalIpInfo']:
                        return StructuresAdditionalIpInfo
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['StructuresAdditionalIpInfo'], typing.List['StructuresAdditionalIpInfo']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'additional_ip':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'StructuresAdditionalIpInfo':
                    return super().__getitem__(i)
            
            
            class private_network(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['StructuresPrivateNetwork']:
                        return StructuresPrivateNetwork
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['StructuresPrivateNetwork'], typing.List['StructuresPrivateNetwork']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'private_network':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'StructuresPrivateNetwork':
                    return super().__getitem__(i)
            __annotations__ = {
                "ip": ip,
                "additional_ip": additional_ip,
                "private_network": private_network,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ip"]) -> MetaOapg.properties.ip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additional_ip"]) -> MetaOapg.properties.additional_ip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["private_network"]) -> MetaOapg.properties.private_network: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ip", "additional_ip", "private_network", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ip"]) -> typing.Union[MetaOapg.properties.ip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additional_ip"]) -> typing.Union[MetaOapg.properties.additional_ip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["private_network"]) -> typing.Union[MetaOapg.properties.private_network, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ip", "additional_ip", "private_network", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ip: typing.Union[MetaOapg.properties.ip, list, tuple, schemas.Unset] = schemas.unset,
        additional_ip: typing.Union[MetaOapg.properties.additional_ip, list, tuple, schemas.Unset] = schemas.unset,
        private_network: typing.Union[MetaOapg.properties.private_network, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NetworkGetNetworkInfoResponse':
        return super().__new__(
            cls,
            *args,
            ip=ip,
            additional_ip=additional_ip,
            private_network=private_network,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_vps.model.structures_additional_ip_info import StructuresAdditionalIpInfo
from beget_openapi_vps.model.structures_ip_info import StructuresIpInfo
from beget_openapi_vps.model.structures_private_network import StructuresPrivateNetwork