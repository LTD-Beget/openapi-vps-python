# coding: utf-8

"""
    API Облачных серверов

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.2.1
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


class ManageGetStatusesResponseStatusInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
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
            rescue_mode = schemas.BoolSchema
            migrating = schemas.BoolSchema
            manage_enabled = schemas.BoolSchema
            restoring = schemas.BoolSchema
            archived = schemas.BoolSchema
            unblocking = schemas.BoolSchema
            unarchiving = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "status": status,
                "rescue_mode": rescue_mode,
                "migrating": migrating,
                "manage_enabled": manage_enabled,
                "restoring": restoring,
                "archived": archived,
                "unblocking": unblocking,
                "unarchiving": unarchiving,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rescue_mode"]) -> MetaOapg.properties.rescue_mode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["migrating"]) -> MetaOapg.properties.migrating: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["manage_enabled"]) -> MetaOapg.properties.manage_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["restoring"]) -> MetaOapg.properties.restoring: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["archived"]) -> MetaOapg.properties.archived: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unblocking"]) -> MetaOapg.properties.unblocking: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unarchiving"]) -> MetaOapg.properties.unarchiving: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "status", "rescue_mode", "migrating", "manage_enabled", "restoring", "archived", "unblocking", "unarchiving", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rescue_mode"]) -> typing.Union[MetaOapg.properties.rescue_mode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["migrating"]) -> typing.Union[MetaOapg.properties.migrating, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["manage_enabled"]) -> typing.Union[MetaOapg.properties.manage_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["restoring"]) -> typing.Union[MetaOapg.properties.restoring, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["archived"]) -> typing.Union[MetaOapg.properties.archived, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unblocking"]) -> typing.Union[MetaOapg.properties.unblocking, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unarchiving"]) -> typing.Union[MetaOapg.properties.unarchiving, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "status", "rescue_mode", "migrating", "manage_enabled", "restoring", "archived", "unblocking", "unarchiving", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        rescue_mode: typing.Union[MetaOapg.properties.rescue_mode, bool, schemas.Unset] = schemas.unset,
        migrating: typing.Union[MetaOapg.properties.migrating, bool, schemas.Unset] = schemas.unset,
        manage_enabled: typing.Union[MetaOapg.properties.manage_enabled, bool, schemas.Unset] = schemas.unset,
        restoring: typing.Union[MetaOapg.properties.restoring, bool, schemas.Unset] = schemas.unset,
        archived: typing.Union[MetaOapg.properties.archived, bool, schemas.Unset] = schemas.unset,
        unblocking: typing.Union[MetaOapg.properties.unblocking, bool, schemas.Unset] = schemas.unset,
        unarchiving: typing.Union[MetaOapg.properties.unarchiving, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ManageGetStatusesResponseStatusInfo':
        return super().__new__(
            cls,
            *args,
            id=id,
            status=status,
            rescue_mode=rescue_mode,
            migrating=migrating,
            manage_enabled=manage_enabled,
            restoring=restoring,
            archived=archived,
            unblocking=unblocking,
            unarchiving=unarchiving,
            _configuration=_configuration,
            **kwargs,
        )
