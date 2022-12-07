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


class StructuresFileInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            is_link = schemas.BoolSchema
            is_dir = schemas.BoolSchema
            name = schemas.StrSchema
            ext = schemas.StrSchema
            path = schemas.StrSchema
            owner = schemas.StrSchema
            group = schemas.StrSchema
            size = schemas.StrSchema
            mtime = schemas.Float64Schema
            mtime_str = schemas.StrSchema
            mode = schemas.StrSchema
            __annotations__ = {
                "is_link": is_link,
                "is_dir": is_dir,
                "name": name,
                "ext": ext,
                "path": path,
                "owner": owner,
                "group": group,
                "size": size,
                "mtime": mtime,
                "mtime_str": mtime_str,
                "mode": mode,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_link"]) -> MetaOapg.properties.is_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_dir"]) -> MetaOapg.properties.is_dir: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ext"]) -> MetaOapg.properties.ext: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner"]) -> MetaOapg.properties.owner: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["group"]) -> MetaOapg.properties.group: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mtime"]) -> MetaOapg.properties.mtime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mtime_str"]) -> MetaOapg.properties.mtime_str: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mode"]) -> MetaOapg.properties.mode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["is_link", "is_dir", "name", "ext", "path", "owner", "group", "size", "mtime", "mtime_str", "mode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_link"]) -> typing.Union[MetaOapg.properties.is_link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_dir"]) -> typing.Union[MetaOapg.properties.is_dir, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ext"]) -> typing.Union[MetaOapg.properties.ext, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> typing.Union[MetaOapg.properties.path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner"]) -> typing.Union[MetaOapg.properties.owner, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["group"]) -> typing.Union[MetaOapg.properties.group, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> typing.Union[MetaOapg.properties.size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mtime"]) -> typing.Union[MetaOapg.properties.mtime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mtime_str"]) -> typing.Union[MetaOapg.properties.mtime_str, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mode"]) -> typing.Union[MetaOapg.properties.mode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["is_link", "is_dir", "name", "ext", "path", "owner", "group", "size", "mtime", "mtime_str", "mode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        is_link: typing.Union[MetaOapg.properties.is_link, bool, schemas.Unset] = schemas.unset,
        is_dir: typing.Union[MetaOapg.properties.is_dir, bool, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        ext: typing.Union[MetaOapg.properties.ext, str, schemas.Unset] = schemas.unset,
        path: typing.Union[MetaOapg.properties.path, str, schemas.Unset] = schemas.unset,
        owner: typing.Union[MetaOapg.properties.owner, str, schemas.Unset] = schemas.unset,
        group: typing.Union[MetaOapg.properties.group, str, schemas.Unset] = schemas.unset,
        size: typing.Union[MetaOapg.properties.size, str, schemas.Unset] = schemas.unset,
        mtime: typing.Union[MetaOapg.properties.mtime, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        mtime_str: typing.Union[MetaOapg.properties.mtime_str, str, schemas.Unset] = schemas.unset,
        mode: typing.Union[MetaOapg.properties.mode, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StructuresFileInfo':
        return super().__new__(
            cls,
            *args,
            is_link=is_link,
            is_dir=is_dir,
            name=name,
            ext=ext,
            path=path,
            owner=owner,
            group=group,
            size=size,
            mtime=mtime,
            mtime_str=mtime_str,
            mode=mode,
            _configuration=_configuration,
            **kwargs,
        )
