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


class ManageVpsInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            slug = schemas.StrSchema
            display_name = schemas.StrSchema
            hostname = schemas.StrSchema
        
            @staticmethod
            def configuration() -> typing.Type['ManageVpsConfiguration']:
                return ManageVpsConfiguration
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'enum'
                    enum_value_to_name = {
                        "UNKNOWN": "UNKNOWN",
                        "CREATING": "CREATING",
                        "RUNNING": "RUNNING",
                        "STOPPING": "STOPPING",
                        "RESTARTING": "RESTARTING",
                        "REMOVING": "REMOVING",
                        "REMOVED": "REMOVED",
                        "STOPPED": "STOPPED",
                        "STARTING": "STARTING",
                        "RECONFIGURING": "RECONFIGURING",
                        "REINSTALLING": "REINSTALLING",
                    }
                
                @schemas.classproperty
                def UNKNOWN(cls):
                    return cls("UNKNOWN")
                
                @schemas.classproperty
                def CREATING(cls):
                    return cls("CREATING")
                
                @schemas.classproperty
                def RUNNING(cls):
                    return cls("RUNNING")
                
                @schemas.classproperty
                def STOPPING(cls):
                    return cls("STOPPING")
                
                @schemas.classproperty
                def RESTARTING(cls):
                    return cls("RESTARTING")
                
                @schemas.classproperty
                def REMOVING(cls):
                    return cls("REMOVING")
                
                @schemas.classproperty
                def REMOVED(cls):
                    return cls("REMOVED")
                
                @schemas.classproperty
                def STOPPED(cls):
                    return cls("STOPPED")
                
                @schemas.classproperty
                def STARTING(cls):
                    return cls("STARTING")
                
                @schemas.classproperty
                def RECONFIGURING(cls):
                    return cls("RECONFIGURING")
                
                @schemas.classproperty
                def REINSTALLING(cls):
                    return cls("REINSTALLING")
            
            
            class ssh_keys(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['StructuresSshKeyInfo']:
                        return StructuresSshKeyInfo
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['StructuresSshKeyInfo'], typing.List['StructuresSshKeyInfo']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ssh_keys':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'StructuresSshKeyInfo':
                    return super().__getitem__(i)
            has_password = schemas.BoolSchema
            manage_enabled = schemas.BoolSchema
            description = schemas.StrSchema
            date_create = schemas.StrSchema
            ip_address = schemas.StrSchema
            rescue_mode = schemas.BoolSchema
            migrating = schemas.BoolSchema
            host_unavailable = schemas.BoolSchema
            unblocking = schemas.BoolSchema
            restoring = schemas.BoolSchema
            disk_used = schemas.StrSchema
            disk_left = schemas.StrSchema
            
            
            class additional_ip_address(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'additional_ip_address':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            beget_ssh_access_allowed = schemas.BoolSchema
            archived = schemas.BoolSchema
            unarchiving = schemas.BoolSchema
            
            
            class private_network(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['StructuresAttachedPrivateNetwork']:
                        return StructuresAttachedPrivateNetwork
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['StructuresAttachedPrivateNetwork'], typing.List['StructuresAttachedPrivateNetwork']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'private_network':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'StructuresAttachedPrivateNetwork':
                    return super().__getitem__(i)
            technical_domain = schemas.StrSchema
            software_domain = schemas.StrSchema
        
            @staticmethod
            def software() -> typing.Type['StructuresInstalledSoftwareInfo']:
                return StructuresInstalledSoftwareInfo
            link_slug = schemas.StrSchema
            region = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "slug": slug,
                "display_name": display_name,
                "hostname": hostname,
                "configuration": configuration,
                "status": status,
                "ssh_keys": ssh_keys,
                "has_password": has_password,
                "manage_enabled": manage_enabled,
                "description": description,
                "date_create": date_create,
                "ip_address": ip_address,
                "rescue_mode": rescue_mode,
                "migrating": migrating,
                "host_unavailable": host_unavailable,
                "unblocking": unblocking,
                "restoring": restoring,
                "disk_used": disk_used,
                "disk_left": disk_left,
                "additional_ip_address": additional_ip_address,
                "beget_ssh_access_allowed": beget_ssh_access_allowed,
                "archived": archived,
                "unarchiving": unarchiving,
                "private_network": private_network,
                "technical_domain": technical_domain,
                "software_domain": software_domain,
                "software": software,
                "link_slug": link_slug,
                "region": region,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostname"]) -> MetaOapg.properties.hostname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configuration"]) -> 'ManageVpsConfiguration': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssh_keys"]) -> MetaOapg.properties.ssh_keys: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_password"]) -> MetaOapg.properties.has_password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["manage_enabled"]) -> MetaOapg.properties.manage_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_create"]) -> MetaOapg.properties.date_create: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ip_address"]) -> MetaOapg.properties.ip_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rescue_mode"]) -> MetaOapg.properties.rescue_mode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["migrating"]) -> MetaOapg.properties.migrating: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["host_unavailable"]) -> MetaOapg.properties.host_unavailable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unblocking"]) -> MetaOapg.properties.unblocking: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["restoring"]) -> MetaOapg.properties.restoring: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disk_used"]) -> MetaOapg.properties.disk_used: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disk_left"]) -> MetaOapg.properties.disk_left: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additional_ip_address"]) -> MetaOapg.properties.additional_ip_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["beget_ssh_access_allowed"]) -> MetaOapg.properties.beget_ssh_access_allowed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["archived"]) -> MetaOapg.properties.archived: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unarchiving"]) -> MetaOapg.properties.unarchiving: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["private_network"]) -> MetaOapg.properties.private_network: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["technical_domain"]) -> MetaOapg.properties.technical_domain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["software_domain"]) -> MetaOapg.properties.software_domain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["software"]) -> 'StructuresInstalledSoftwareInfo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link_slug"]) -> MetaOapg.properties.link_slug: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["region"]) -> MetaOapg.properties.region: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "slug", "display_name", "hostname", "configuration", "status", "ssh_keys", "has_password", "manage_enabled", "description", "date_create", "ip_address", "rescue_mode", "migrating", "host_unavailable", "unblocking", "restoring", "disk_used", "disk_left", "additional_ip_address", "beget_ssh_access_allowed", "archived", "unarchiving", "private_network", "technical_domain", "software_domain", "software", "link_slug", "region", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slug"]) -> typing.Union[MetaOapg.properties.slug, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_name"]) -> typing.Union[MetaOapg.properties.display_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostname"]) -> typing.Union[MetaOapg.properties.hostname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configuration"]) -> typing.Union['ManageVpsConfiguration', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssh_keys"]) -> typing.Union[MetaOapg.properties.ssh_keys, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_password"]) -> typing.Union[MetaOapg.properties.has_password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["manage_enabled"]) -> typing.Union[MetaOapg.properties.manage_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_create"]) -> typing.Union[MetaOapg.properties.date_create, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ip_address"]) -> typing.Union[MetaOapg.properties.ip_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rescue_mode"]) -> typing.Union[MetaOapg.properties.rescue_mode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["migrating"]) -> typing.Union[MetaOapg.properties.migrating, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["host_unavailable"]) -> typing.Union[MetaOapg.properties.host_unavailable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unblocking"]) -> typing.Union[MetaOapg.properties.unblocking, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["restoring"]) -> typing.Union[MetaOapg.properties.restoring, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disk_used"]) -> typing.Union[MetaOapg.properties.disk_used, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disk_left"]) -> typing.Union[MetaOapg.properties.disk_left, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additional_ip_address"]) -> typing.Union[MetaOapg.properties.additional_ip_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["beget_ssh_access_allowed"]) -> typing.Union[MetaOapg.properties.beget_ssh_access_allowed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["archived"]) -> typing.Union[MetaOapg.properties.archived, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unarchiving"]) -> typing.Union[MetaOapg.properties.unarchiving, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["private_network"]) -> typing.Union[MetaOapg.properties.private_network, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["technical_domain"]) -> typing.Union[MetaOapg.properties.technical_domain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["software_domain"]) -> typing.Union[MetaOapg.properties.software_domain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["software"]) -> typing.Union['StructuresInstalledSoftwareInfo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link_slug"]) -> typing.Union[MetaOapg.properties.link_slug, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["region"]) -> typing.Union[MetaOapg.properties.region, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "slug", "display_name", "hostname", "configuration", "status", "ssh_keys", "has_password", "manage_enabled", "description", "date_create", "ip_address", "rescue_mode", "migrating", "host_unavailable", "unblocking", "restoring", "disk_used", "disk_left", "additional_ip_address", "beget_ssh_access_allowed", "archived", "unarchiving", "private_network", "technical_domain", "software_domain", "software", "link_slug", "region", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        slug: typing.Union[MetaOapg.properties.slug, str, schemas.Unset] = schemas.unset,
        display_name: typing.Union[MetaOapg.properties.display_name, str, schemas.Unset] = schemas.unset,
        hostname: typing.Union[MetaOapg.properties.hostname, str, schemas.Unset] = schemas.unset,
        configuration: typing.Union['ManageVpsConfiguration', schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        ssh_keys: typing.Union[MetaOapg.properties.ssh_keys, list, tuple, schemas.Unset] = schemas.unset,
        has_password: typing.Union[MetaOapg.properties.has_password, bool, schemas.Unset] = schemas.unset,
        manage_enabled: typing.Union[MetaOapg.properties.manage_enabled, bool, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        date_create: typing.Union[MetaOapg.properties.date_create, str, schemas.Unset] = schemas.unset,
        ip_address: typing.Union[MetaOapg.properties.ip_address, str, schemas.Unset] = schemas.unset,
        rescue_mode: typing.Union[MetaOapg.properties.rescue_mode, bool, schemas.Unset] = schemas.unset,
        migrating: typing.Union[MetaOapg.properties.migrating, bool, schemas.Unset] = schemas.unset,
        host_unavailable: typing.Union[MetaOapg.properties.host_unavailable, bool, schemas.Unset] = schemas.unset,
        unblocking: typing.Union[MetaOapg.properties.unblocking, bool, schemas.Unset] = schemas.unset,
        restoring: typing.Union[MetaOapg.properties.restoring, bool, schemas.Unset] = schemas.unset,
        disk_used: typing.Union[MetaOapg.properties.disk_used, str, schemas.Unset] = schemas.unset,
        disk_left: typing.Union[MetaOapg.properties.disk_left, str, schemas.Unset] = schemas.unset,
        additional_ip_address: typing.Union[MetaOapg.properties.additional_ip_address, list, tuple, schemas.Unset] = schemas.unset,
        beget_ssh_access_allowed: typing.Union[MetaOapg.properties.beget_ssh_access_allowed, bool, schemas.Unset] = schemas.unset,
        archived: typing.Union[MetaOapg.properties.archived, bool, schemas.Unset] = schemas.unset,
        unarchiving: typing.Union[MetaOapg.properties.unarchiving, bool, schemas.Unset] = schemas.unset,
        private_network: typing.Union[MetaOapg.properties.private_network, list, tuple, schemas.Unset] = schemas.unset,
        technical_domain: typing.Union[MetaOapg.properties.technical_domain, str, schemas.Unset] = schemas.unset,
        software_domain: typing.Union[MetaOapg.properties.software_domain, str, schemas.Unset] = schemas.unset,
        software: typing.Union['StructuresInstalledSoftwareInfo', schemas.Unset] = schemas.unset,
        link_slug: typing.Union[MetaOapg.properties.link_slug, str, schemas.Unset] = schemas.unset,
        region: typing.Union[MetaOapg.properties.region, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ManageVpsInfo':
        return super().__new__(
            cls,
            *args,
            id=id,
            slug=slug,
            display_name=display_name,
            hostname=hostname,
            configuration=configuration,
            status=status,
            ssh_keys=ssh_keys,
            has_password=has_password,
            manage_enabled=manage_enabled,
            description=description,
            date_create=date_create,
            ip_address=ip_address,
            rescue_mode=rescue_mode,
            migrating=migrating,
            host_unavailable=host_unavailable,
            unblocking=unblocking,
            restoring=restoring,
            disk_used=disk_used,
            disk_left=disk_left,
            additional_ip_address=additional_ip_address,
            beget_ssh_access_allowed=beget_ssh_access_allowed,
            archived=archived,
            unarchiving=unarchiving,
            private_network=private_network,
            technical_domain=technical_domain,
            software_domain=software_domain,
            software=software,
            link_slug=link_slug,
            region=region,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_vps.model.manage_vps_configuration import ManageVpsConfiguration
from beget_openapi_vps.model.structures_attached_private_network import StructuresAttachedPrivateNetwork
from beget_openapi_vps.model.structures_installed_software_info import StructuresInstalledSoftwareInfo
from beget_openapi_vps.model.structures_ssh_key_info import StructuresSshKeyInfo
