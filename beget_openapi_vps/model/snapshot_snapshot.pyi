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


class SnapshotSnapshot(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            vps_id = schemas.StrSchema
            vps_name = schemas.StrSchema
            date_create = schemas.StrSchema
            size = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CREATING(cls):
                    return cls("CREATING")
                
                @schemas.classproperty
                def DONE(cls):
                    return cls("DONE")
                
                @schemas.classproperty
                def RESTORING(cls):
                    return cls("RESTORING")
                
                @schemas.classproperty
                def DELETED(cls):
                    return cls("DELETED")
            description = schemas.StrSchema
        
            @staticmethod
            def configuration() -> typing.Type['SnapshotRequiredConfiguration']:
                return SnapshotRequiredConfiguration
            price_day = schemas.Float64Schema
        
            @staticmethod
            def installed_software() -> typing.Type['StructuresInstalledSoftwareInfo']:
                return StructuresInstalledSoftwareInfo
            __annotations__ = {
                "id": id,
                "vps_id": vps_id,
                "vps_name": vps_name,
                "date_create": date_create,
                "size": size,
                "status": status,
                "description": description,
                "configuration": configuration,
                "price_day": price_day,
                "installed_software": installed_software,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vps_id"]) -> MetaOapg.properties.vps_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vps_name"]) -> MetaOapg.properties.vps_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_create"]) -> MetaOapg.properties.date_create: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configuration"]) -> 'SnapshotRequiredConfiguration': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price_day"]) -> MetaOapg.properties.price_day: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["installed_software"]) -> 'StructuresInstalledSoftwareInfo': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "vps_id", "vps_name", "date_create", "size", "status", "description", "configuration", "price_day", "installed_software", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vps_id"]) -> typing.Union[MetaOapg.properties.vps_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vps_name"]) -> typing.Union[MetaOapg.properties.vps_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_create"]) -> typing.Union[MetaOapg.properties.date_create, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> typing.Union[MetaOapg.properties.size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configuration"]) -> typing.Union['SnapshotRequiredConfiguration', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price_day"]) -> typing.Union[MetaOapg.properties.price_day, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["installed_software"]) -> typing.Union['StructuresInstalledSoftwareInfo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "vps_id", "vps_name", "date_create", "size", "status", "description", "configuration", "price_day", "installed_software", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        vps_id: typing.Union[MetaOapg.properties.vps_id, str, schemas.Unset] = schemas.unset,
        vps_name: typing.Union[MetaOapg.properties.vps_name, str, schemas.Unset] = schemas.unset,
        date_create: typing.Union[MetaOapg.properties.date_create, str, schemas.Unset] = schemas.unset,
        size: typing.Union[MetaOapg.properties.size, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        configuration: typing.Union['SnapshotRequiredConfiguration', schemas.Unset] = schemas.unset,
        price_day: typing.Union[MetaOapg.properties.price_day, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        installed_software: typing.Union['StructuresInstalledSoftwareInfo', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SnapshotSnapshot':
        return super().__new__(
            cls,
            *args,
            id=id,
            vps_id=vps_id,
            vps_name=vps_name,
            date_create=date_create,
            size=size,
            status=status,
            description=description,
            configuration=configuration,
            price_day=price_day,
            installed_software=installed_software,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_vps.model.snapshot_required_configuration import SnapshotRequiredConfiguration
from beget_openapi_vps.model.structures_installed_software_info import StructuresInstalledSoftwareInfo
