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


class ManageGetSoftwareListResponseSoftwareInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.IntSchema
            name = schemas.StrSchema
            display_name = schemas.StrSchema
            version = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'enum'
                    enum_value_to_name = {
                        "PANEL": "PANEL",
                        "SOFTWARE": "SOFTWARE",
                    }
                
                @schemas.classproperty
                def PANEL(cls):
                    return cls("PANEL")
                
                @schemas.classproperty
                def SOFTWARE(cls):
                    return cls("SOFTWARE")
            description = schemas.StrSchema
            description_version = schemas.StrSchema
            
            
            class image_id(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.IntSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'image_id':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class variable(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'variable':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def requirements() -> typing.Type['ManageGetSoftwareListResponseSoftwareInfoRequirements']:
                return ManageGetSoftwareListResponseSoftwareInfoRequirements
            __annotations__ = {
                "id": id,
                "name": name,
                "display_name": display_name,
                "version": version,
                "type": type,
                "description": description,
                "description_version": description_version,
                "image_id": image_id,
                "variable": variable,
                "requirements": requirements,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description_version"]) -> MetaOapg.properties.description_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_id"]) -> MetaOapg.properties.image_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["variable"]) -> MetaOapg.properties.variable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requirements"]) -> 'ManageGetSoftwareListResponseSoftwareInfoRequirements': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "display_name", "version", "type", "description", "description_version", "image_id", "variable", "requirements", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_name"]) -> typing.Union[MetaOapg.properties.display_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> typing.Union[MetaOapg.properties.version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description_version"]) -> typing.Union[MetaOapg.properties.description_version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_id"]) -> typing.Union[MetaOapg.properties.image_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["variable"]) -> typing.Union[MetaOapg.properties.variable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requirements"]) -> typing.Union['ManageGetSoftwareListResponseSoftwareInfoRequirements', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "display_name", "version", "type", "description", "description_version", "image_id", "variable", "requirements", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        display_name: typing.Union[MetaOapg.properties.display_name, str, schemas.Unset] = schemas.unset,
        version: typing.Union[MetaOapg.properties.version, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        description_version: typing.Union[MetaOapg.properties.description_version, str, schemas.Unset] = schemas.unset,
        image_id: typing.Union[MetaOapg.properties.image_id, list, tuple, schemas.Unset] = schemas.unset,
        variable: typing.Union[MetaOapg.properties.variable, list, tuple, schemas.Unset] = schemas.unset,
        requirements: typing.Union['ManageGetSoftwareListResponseSoftwareInfoRequirements', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ManageGetSoftwareListResponseSoftwareInfo':
        return super().__new__(
            cls,
            *args,
            id=id,
            name=name,
            display_name=display_name,
            version=version,
            type=type,
            description=description,
            description_version=description_version,
            image_id=image_id,
            variable=variable,
            requirements=requirements,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_vps.model.manage_get_software_list_response_software_info_requirements import ManageGetSoftwareListResponseSoftwareInfoRequirements
