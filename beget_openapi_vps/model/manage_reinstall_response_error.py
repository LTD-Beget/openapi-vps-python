# coding: utf-8

"""
    API Облачных серверов

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.4.0
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


class ManageReinstallResponseError(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class code(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'enum'
                    enum_value_to_name = {
                        "INTERNAL_ERROR": "INTERNAL_ERROR",
                        "INVALID_STATE": "INVALID_STATE",
                        "SERVICE_DISABLED": "SERVICE_DISABLED",
                        "INVALID_CONFIGURATION": "INVALID_CONFIGURATION",
                        "INVALID_SECURITY_CONFIGURATION": "INVALID_SECURITY_CONFIGURATION",
                        "INVALID_PASSWORD": "INVALID_PASSWORD",
                        "SOFTWARE_INVALID_TYPE": "SOFTWARE_INVALID_TYPE",
                        "SOFTWARE_NOT_ENOUGH_RESOURCES": "SOFTWARE_NOT_ENOUGH_RESOURCES",
                        "INVALID_PARAMS": "INVALID_PARAMS",
                        "SOFTWARE_VARIABLE_REQUIRED": "SOFTWARE_VARIABLE_REQUIRED",
                        "SOFTWARE_VARIABLE_INVALID": "SOFTWARE_VARIABLE_INVALID",
                        "BLACKLISTED_PASSWORD": "BLACKLISTED_PASSWORD",
                    }
                
                @schemas.classproperty
                def INTERNAL_ERROR(cls):
                    return cls("INTERNAL_ERROR")
                
                @schemas.classproperty
                def INVALID_STATE(cls):
                    return cls("INVALID_STATE")
                
                @schemas.classproperty
                def SERVICE_DISABLED(cls):
                    return cls("SERVICE_DISABLED")
                
                @schemas.classproperty
                def INVALID_CONFIGURATION(cls):
                    return cls("INVALID_CONFIGURATION")
                
                @schemas.classproperty
                def INVALID_SECURITY_CONFIGURATION(cls):
                    return cls("INVALID_SECURITY_CONFIGURATION")
                
                @schemas.classproperty
                def INVALID_PASSWORD(cls):
                    return cls("INVALID_PASSWORD")
                
                @schemas.classproperty
                def SOFTWARE_INVALID_TYPE(cls):
                    return cls("SOFTWARE_INVALID_TYPE")
                
                @schemas.classproperty
                def SOFTWARE_NOT_ENOUGH_RESOURCES(cls):
                    return cls("SOFTWARE_NOT_ENOUGH_RESOURCES")
                
                @schemas.classproperty
                def INVALID_PARAMS(cls):
                    return cls("INVALID_PARAMS")
                
                @schemas.classproperty
                def SOFTWARE_VARIABLE_REQUIRED(cls):
                    return cls("SOFTWARE_VARIABLE_REQUIRED")
                
                @schemas.classproperty
                def SOFTWARE_VARIABLE_INVALID(cls):
                    return cls("SOFTWARE_VARIABLE_INVALID")
                
                @schemas.classproperty
                def BLACKLISTED_PASSWORD(cls):
                    return cls("BLACKLISTED_PASSWORD")
            message = schemas.StrSchema
        
            @staticmethod
            def variable_error() -> typing.Type['ManageReinstallResponseErrorSoftwareVariableError']:
                return ManageReinstallResponseErrorSoftwareVariableError
            __annotations__ = {
                "code": code,
                "message": message,
                "variable_error": variable_error,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["variable_error"]) -> 'ManageReinstallResponseErrorSoftwareVariableError': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["code", "message", "variable_error", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["variable_error"]) -> typing.Union['ManageReinstallResponseErrorSoftwareVariableError', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["code", "message", "variable_error", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        variable_error: typing.Union['ManageReinstallResponseErrorSoftwareVariableError', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ManageReinstallResponseError':
        return super().__new__(
            cls,
            *args,
            code=code,
            message=message,
            variable_error=variable_error,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_vps.model.manage_reinstall_response_error_software_variable_error import ManageReinstallResponseErrorSoftwareVariableError
