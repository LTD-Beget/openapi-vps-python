# coding: utf-8

"""
    API Облачных серверов

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.5.1
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


class StatisticGetProcessListResponseProcessListProcessInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            pid = schemas.IntSchema
            nice = schemas.Int32Schema
            virt = schemas.StrSchema
            rss = schemas.StrSchema
            state = schemas.StrSchema
            cpu_percent = schemas.Float32Schema
            mem_percent = schemas.Float32Schema
            time_running = schemas.Float32Schema
            name = schemas.StrSchema
            user = schemas.StrSchema
            __annotations__ = {
                "pid": pid,
                "nice": nice,
                "virt": virt,
                "rss": rss,
                "state": state,
                "cpu_percent": cpu_percent,
                "mem_percent": mem_percent,
                "time_running": time_running,
                "name": name,
                "user": user,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pid"]) -> MetaOapg.properties.pid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nice"]) -> MetaOapg.properties.nice: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["virt"]) -> MetaOapg.properties.virt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rss"]) -> MetaOapg.properties.rss: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cpu_percent"]) -> MetaOapg.properties.cpu_percent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mem_percent"]) -> MetaOapg.properties.mem_percent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_running"]) -> MetaOapg.properties.time_running: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["pid", "nice", "virt", "rss", "state", "cpu_percent", "mem_percent", "time_running", "name", "user", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pid"]) -> typing.Union[MetaOapg.properties.pid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nice"]) -> typing.Union[MetaOapg.properties.nice, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["virt"]) -> typing.Union[MetaOapg.properties.virt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rss"]) -> typing.Union[MetaOapg.properties.rss, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cpu_percent"]) -> typing.Union[MetaOapg.properties.cpu_percent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mem_percent"]) -> typing.Union[MetaOapg.properties.mem_percent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_running"]) -> typing.Union[MetaOapg.properties.time_running, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union[MetaOapg.properties.user, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["pid", "nice", "virt", "rss", "state", "cpu_percent", "mem_percent", "time_running", "name", "user", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        pid: typing.Union[MetaOapg.properties.pid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        nice: typing.Union[MetaOapg.properties.nice, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        virt: typing.Union[MetaOapg.properties.virt, str, schemas.Unset] = schemas.unset,
        rss: typing.Union[MetaOapg.properties.rss, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        cpu_percent: typing.Union[MetaOapg.properties.cpu_percent, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        mem_percent: typing.Union[MetaOapg.properties.mem_percent, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        time_running: typing.Union[MetaOapg.properties.time_running, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        user: typing.Union[MetaOapg.properties.user, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StatisticGetProcessListResponseProcessListProcessInfo':
        return super().__new__(
            cls,
            *args,
            pid=pid,
            nice=nice,
            virt=virt,
            rss=rss,
            state=state,
            cpu_percent=cpu_percent,
            mem_percent=mem_percent,
            time_running=time_running,
            name=name,
            user=user,
            _configuration=_configuration,
            **kwargs,
        )
