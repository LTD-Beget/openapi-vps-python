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


class ManageCheckSoftwareRequirementsResponseError(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class wordpress_error(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'enum'
                    enum_value_to_name = {
                        "_": "_",
                        "DOMAIN_NOT_REGISTERED": "DOMAIN_NOT_REGISTERED",
                        "WRONG_NS_RECORD": "WRONG_NS_RECORD",
                        "DOMAIN_NOT_DELEGATED": "DOMAIN_NOT_DELEGATED",
                        "INVALID_DOMAIN": "INVALID_DOMAIN",
                        "DOMAIN_IS_NEW": "DOMAIN_IS_NEW",
                    }
                
                @schemas.classproperty
                def _(cls):
                    return cls("_")
                
                @schemas.classproperty
                def DOMAIN_NOT_REGISTERED(cls):
                    return cls("DOMAIN_NOT_REGISTERED")
                
                @schemas.classproperty
                def WRONG_NS_RECORD(cls):
                    return cls("WRONG_NS_RECORD")
                
                @schemas.classproperty
                def DOMAIN_NOT_DELEGATED(cls):
                    return cls("DOMAIN_NOT_DELEGATED")
                
                @schemas.classproperty
                def INVALID_DOMAIN(cls):
                    return cls("INVALID_DOMAIN")
                
                @schemas.classproperty
                def DOMAIN_IS_NEW(cls):
                    return cls("DOMAIN_IS_NEW")
            
            
            class domain_error(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'enum'
                    enum_value_to_name = {
                        "_": "_",
                        "DOMAIN_NOT_REGISTERED": "DOMAIN_NOT_REGISTERED",
                        "WRONG_NS_RECORD": "WRONG_NS_RECORD",
                        "DOMAIN_NOT_DELEGATED": "DOMAIN_NOT_DELEGATED",
                        "INVALID_DOMAIN": "INVALID_DOMAIN",
                        "DOMAIN_IS_NEW": "DOMAIN_IS_NEW",
                    }
                
                @schemas.classproperty
                def _(cls):
                    return cls("_")
                
                @schemas.classproperty
                def DOMAIN_NOT_REGISTERED(cls):
                    return cls("DOMAIN_NOT_REGISTERED")
                
                @schemas.classproperty
                def WRONG_NS_RECORD(cls):
                    return cls("WRONG_NS_RECORD")
                
                @schemas.classproperty
                def DOMAIN_NOT_DELEGATED(cls):
                    return cls("DOMAIN_NOT_DELEGATED")
                
                @schemas.classproperty
                def INVALID_DOMAIN(cls):
                    return cls("INVALID_DOMAIN")
                
                @schemas.classproperty
                def DOMAIN_IS_NEW(cls):
                    return cls("DOMAIN_IS_NEW")
            __annotations__ = {
                "wordpress_error": wordpress_error,
                "domain_error": domain_error,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wordpress_error"]) -> MetaOapg.properties.wordpress_error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["domain_error"]) -> MetaOapg.properties.domain_error: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["wordpress_error", "domain_error", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wordpress_error"]) -> typing.Union[MetaOapg.properties.wordpress_error, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["domain_error"]) -> typing.Union[MetaOapg.properties.domain_error, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["wordpress_error", "domain_error", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        wordpress_error: typing.Union[MetaOapg.properties.wordpress_error, str, schemas.Unset] = schemas.unset,
        domain_error: typing.Union[MetaOapg.properties.domain_error, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ManageCheckSoftwareRequirementsResponseError':
        return super().__new__(
            cls,
            *args,
            wordpress_error=wordpress_error,
            domain_error=domain_error,
            _configuration=_configuration,
            **kwargs,
        )
