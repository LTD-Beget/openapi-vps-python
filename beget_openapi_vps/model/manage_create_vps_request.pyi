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


class ManageCreateVpsRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            display_name = schemas.StrSchema
            hostname = schemas.StrSchema
            description = schemas.StrSchema
            configuration_id = schemas.StrSchema
        
            @staticmethod
            def software() -> typing.Type['ManageSoftwareInstallInfo']:
                return ManageSoftwareInstallInfo
            snapshot_id = schemas.StrSchema
            
            
            class ssh_keys(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.IntSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ssh_keys':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            password = schemas.StrSchema
            beget_ssh_access_allowed = schemas.BoolSchema
            
            
            class private_networks(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ManagePrivateNetworkInfo']:
                        return ManagePrivateNetworkInfo
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ManagePrivateNetworkInfo'], typing.List['ManagePrivateNetworkInfo']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'private_networks':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ManagePrivateNetworkInfo':
                    return super().__getitem__(i)
            __annotations__ = {
                "display_name": display_name,
                "hostname": hostname,
                "description": description,
                "configuration_id": configuration_id,
                "software": software,
                "snapshot_id": snapshot_id,
                "ssh_keys": ssh_keys,
                "password": password,
                "beget_ssh_access_allowed": beget_ssh_access_allowed,
                "private_networks": private_networks,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostname"]) -> MetaOapg.properties.hostname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configuration_id"]) -> MetaOapg.properties.configuration_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["software"]) -> 'ManageSoftwareInstallInfo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["snapshot_id"]) -> MetaOapg.properties.snapshot_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssh_keys"]) -> MetaOapg.properties.ssh_keys: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["beget_ssh_access_allowed"]) -> MetaOapg.properties.beget_ssh_access_allowed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["private_networks"]) -> MetaOapg.properties.private_networks: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["display_name", "hostname", "description", "configuration_id", "software", "snapshot_id", "ssh_keys", "password", "beget_ssh_access_allowed", "private_networks", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_name"]) -> typing.Union[MetaOapg.properties.display_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostname"]) -> typing.Union[MetaOapg.properties.hostname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configuration_id"]) -> typing.Union[MetaOapg.properties.configuration_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["software"]) -> typing.Union['ManageSoftwareInstallInfo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["snapshot_id"]) -> typing.Union[MetaOapg.properties.snapshot_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssh_keys"]) -> typing.Union[MetaOapg.properties.ssh_keys, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union[MetaOapg.properties.password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["beget_ssh_access_allowed"]) -> typing.Union[MetaOapg.properties.beget_ssh_access_allowed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["private_networks"]) -> typing.Union[MetaOapg.properties.private_networks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["display_name", "hostname", "description", "configuration_id", "software", "snapshot_id", "ssh_keys", "password", "beget_ssh_access_allowed", "private_networks", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        display_name: typing.Union[MetaOapg.properties.display_name, str, schemas.Unset] = schemas.unset,
        hostname: typing.Union[MetaOapg.properties.hostname, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        configuration_id: typing.Union[MetaOapg.properties.configuration_id, str, schemas.Unset] = schemas.unset,
        software: typing.Union['ManageSoftwareInstallInfo', schemas.Unset] = schemas.unset,
        snapshot_id: typing.Union[MetaOapg.properties.snapshot_id, str, schemas.Unset] = schemas.unset,
        ssh_keys: typing.Union[MetaOapg.properties.ssh_keys, list, tuple, schemas.Unset] = schemas.unset,
        password: typing.Union[MetaOapg.properties.password, str, schemas.Unset] = schemas.unset,
        beget_ssh_access_allowed: typing.Union[MetaOapg.properties.beget_ssh_access_allowed, bool, schemas.Unset] = schemas.unset,
        private_networks: typing.Union[MetaOapg.properties.private_networks, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ManageCreateVpsRequest':
        return super().__new__(
            cls,
            *args,
            display_name=display_name,
            hostname=hostname,
            description=description,
            configuration_id=configuration_id,
            software=software,
            snapshot_id=snapshot_id,
            ssh_keys=ssh_keys,
            password=password,
            beget_ssh_access_allowed=beget_ssh_access_allowed,
            private_networks=private_networks,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_vps.model.manage_private_network_info import ManagePrivateNetworkInfo
from beget_openapi_vps.model.manage_software_install_info import ManageSoftwareInstallInfo
