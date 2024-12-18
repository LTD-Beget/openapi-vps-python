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


class StructuresOrderInfo(
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
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'enum'
                    enum_value_to_name = {
                        "DOWNLOAD": "DOWNLOAD",
                        "RESTORE": "RESTORE",
                    }
                
                @schemas.classproperty
                def DOWNLOAD(cls):
                    return cls("DOWNLOAD")
                
                @schemas.classproperty
                def RESTORE(cls):
                    return cls("RESTORE")
            date_create = schemas.StrSchema
            date_complete = schemas.StrSchema
            
            
            class path(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'path':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'enum'
                    enum_value_to_name = {
                        "PROCESSING": "PROCESSING",
                        "COMPLETED": "COMPLETED",
                        "ERROR": "ERROR",
                        "COMPLETED_PARTIALLY": "COMPLETED_PARTIALLY",
                    }
                
                @schemas.classproperty
                def PROCESSING(cls):
                    return cls("PROCESSING")
                
                @schemas.classproperty
                def COMPLETED(cls):
                    return cls("COMPLETED")
                
                @schemas.classproperty
                def ERROR(cls):
                    return cls("ERROR")
                
                @schemas.classproperty
                def COMPLETED_PARTIALLY(cls):
                    return cls("COMPLETED_PARTIALLY")
        
            @staticmethod
            def copy_info() -> typing.Type['StructuresCopyInfo']:
                return StructuresCopyInfo
            affect_live = schemas.BoolSchema
            target = schemas.StrSchema
        
            @staticmethod
            def error_details() -> typing.Type['StructuresOrderInfoErrorDetails']:
                return StructuresOrderInfoErrorDetails
            __annotations__ = {
                "id": id,
                "vps_id": vps_id,
                "vps_name": vps_name,
                "type": type,
                "date_create": date_create,
                "date_complete": date_complete,
                "path": path,
                "status": status,
                "copy_info": copy_info,
                "affect_live": affect_live,
                "target": target,
                "error_details": error_details,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vps_id"]) -> MetaOapg.properties.vps_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vps_name"]) -> MetaOapg.properties.vps_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_create"]) -> MetaOapg.properties.date_create: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_complete"]) -> MetaOapg.properties.date_complete: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copy_info"]) -> 'StructuresCopyInfo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["affect_live"]) -> MetaOapg.properties.affect_live: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target"]) -> MetaOapg.properties.target: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error_details"]) -> 'StructuresOrderInfoErrorDetails': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "vps_id", "vps_name", "type", "date_create", "date_complete", "path", "status", "copy_info", "affect_live", "target", "error_details", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vps_id"]) -> typing.Union[MetaOapg.properties.vps_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vps_name"]) -> typing.Union[MetaOapg.properties.vps_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_create"]) -> typing.Union[MetaOapg.properties.date_create, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_complete"]) -> typing.Union[MetaOapg.properties.date_complete, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> typing.Union[MetaOapg.properties.path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copy_info"]) -> typing.Union['StructuresCopyInfo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["affect_live"]) -> typing.Union[MetaOapg.properties.affect_live, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target"]) -> typing.Union[MetaOapg.properties.target, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error_details"]) -> typing.Union['StructuresOrderInfoErrorDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "vps_id", "vps_name", "type", "date_create", "date_complete", "path", "status", "copy_info", "affect_live", "target", "error_details", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        vps_id: typing.Union[MetaOapg.properties.vps_id, str, schemas.Unset] = schemas.unset,
        vps_name: typing.Union[MetaOapg.properties.vps_name, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        date_create: typing.Union[MetaOapg.properties.date_create, str, schemas.Unset] = schemas.unset,
        date_complete: typing.Union[MetaOapg.properties.date_complete, str, schemas.Unset] = schemas.unset,
        path: typing.Union[MetaOapg.properties.path, list, tuple, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        copy_info: typing.Union['StructuresCopyInfo', schemas.Unset] = schemas.unset,
        affect_live: typing.Union[MetaOapg.properties.affect_live, bool, schemas.Unset] = schemas.unset,
        target: typing.Union[MetaOapg.properties.target, str, schemas.Unset] = schemas.unset,
        error_details: typing.Union['StructuresOrderInfoErrorDetails', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StructuresOrderInfo':
        return super().__new__(
            cls,
            *args,
            id=id,
            vps_id=vps_id,
            vps_name=vps_name,
            type=type,
            date_create=date_create,
            date_complete=date_complete,
            path=path,
            status=status,
            copy_info=copy_info,
            affect_live=affect_live,
            target=target,
            error_details=error_details,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_vps.model.structures_copy_info import StructuresCopyInfo
from beget_openapi_vps.model.structures_order_info_error_details import StructuresOrderInfoErrorDetails
