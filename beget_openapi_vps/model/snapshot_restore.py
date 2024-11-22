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


class SnapshotRestore(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
        
            @staticmethod
            def items() -> typing.Type['SnapshotSnapshot']:
                return SnapshotSnapshot
            vps_id = schemas.StrSchema
            vps_name = schemas.StrSchema
            
            
            class target_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'enum'
                    enum_value_to_name = {
                        "EXISTING_VPS": "EXISTING_VPS",
                        "NEW_VPS": "NEW_VPS",
                    }
                
                @schemas.classproperty
                def EXISTING_VPS(cls):
                    return cls("EXISTING_VPS")
                
                @schemas.classproperty
                def NEW_VPS(cls):
                    return cls("NEW_VPS")
            date_create = schemas.StrSchema
            date_complete = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'enum'
                    enum_value_to_name = {
                        "PROCESSING": "PROCESSING",
                        "COMPLETED": "COMPLETED",
                    }
                
                @schemas.classproperty
                def PROCESSING(cls):
                    return cls("PROCESSING")
                
                @schemas.classproperty
                def COMPLETED(cls):
                    return cls("COMPLETED")
            __annotations__ = {
                "id": id,
                "items": items,
                "vps_id": vps_id,
                "vps_name": vps_name,
                "target_type": target_type,
                "date_create": date_create,
                "date_complete": date_complete,
                "status": status,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["items"]) -> 'SnapshotSnapshot': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vps_id"]) -> MetaOapg.properties.vps_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vps_name"]) -> MetaOapg.properties.vps_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target_type"]) -> MetaOapg.properties.target_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_create"]) -> MetaOapg.properties.date_create: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_complete"]) -> MetaOapg.properties.date_complete: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "items", "vps_id", "vps_name", "target_type", "date_create", "date_complete", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["items"]) -> typing.Union['SnapshotSnapshot', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vps_id"]) -> typing.Union[MetaOapg.properties.vps_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vps_name"]) -> typing.Union[MetaOapg.properties.vps_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target_type"]) -> typing.Union[MetaOapg.properties.target_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_create"]) -> typing.Union[MetaOapg.properties.date_create, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_complete"]) -> typing.Union[MetaOapg.properties.date_complete, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "items", "vps_id", "vps_name", "target_type", "date_create", "date_complete", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        items: typing.Union['SnapshotSnapshot', schemas.Unset] = schemas.unset,
        vps_id: typing.Union[MetaOapg.properties.vps_id, str, schemas.Unset] = schemas.unset,
        vps_name: typing.Union[MetaOapg.properties.vps_name, str, schemas.Unset] = schemas.unset,
        target_type: typing.Union[MetaOapg.properties.target_type, str, schemas.Unset] = schemas.unset,
        date_create: typing.Union[MetaOapg.properties.date_create, str, schemas.Unset] = schemas.unset,
        date_complete: typing.Union[MetaOapg.properties.date_complete, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SnapshotRestore':
        return super().__new__(
            cls,
            *args,
            id=id,
            items=items,
            vps_id=vps_id,
            vps_name=vps_name,
            target_type=target_type,
            date_create=date_create,
            date_complete=date_complete,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_vps.model.snapshot_snapshot import SnapshotSnapshot
