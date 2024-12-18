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


class StructuresInstalledSoftwareInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            display_name = schemas.StrSchema
            version = schemas.StrSchema
            address = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'enum'
                    enum_value_to_name = {
                        "PENDING": "PENDING",
                        "INSTALLING": "INSTALLING",
                        "INSTALLED": "INSTALLED",
                        "ERROR": "ERROR",
                        "CANCEL": "CANCEL",
                    }
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("PENDING")
                
                @schemas.classproperty
                def INSTALLING(cls):
                    return cls("INSTALLING")
                
                @schemas.classproperty
                def INSTALLED(cls):
                    return cls("INSTALLED")
                
                @schemas.classproperty
                def ERROR(cls):
                    return cls("ERROR")
                
                @schemas.classproperty
                def CANCEL(cls):
                    return cls("CANCEL")
            
            
            class field_value(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['StructuresInstalledSoftwareInfoFieldValue']:
                        return StructuresInstalledSoftwareInfoFieldValue
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['StructuresInstalledSoftwareInfoFieldValue'], typing.List['StructuresInstalledSoftwareInfoFieldValue']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'field_value':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'StructuresInstalledSoftwareInfoFieldValue':
                    return super().__getitem__(i)
        
            @staticmethod
            def metadata() -> typing.Type['StructuresSoftwareMetadata']:
                return StructuresSoftwareMetadata
            description = schemas.StrSchema
            description_en = schemas.StrSchema
            
            
            class category(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['StructuresSoftwareCategory']:
                        return StructuresSoftwareCategory
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['StructuresSoftwareCategory'], typing.List['StructuresSoftwareCategory']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'category':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'StructuresSoftwareCategory':
                    return super().__getitem__(i)
            slug = schemas.StrSchema
            post_install_alert = schemas.BoolSchema
            
            
            class license(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['StructuresIssuedSoftwareLicense']:
                        return StructuresIssuedSoftwareLicense
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['StructuresIssuedSoftwareLicense'], typing.List['StructuresIssuedSoftwareLicense']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'license':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'StructuresIssuedSoftwareLicense':
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "display_name": display_name,
                "version": version,
                "address": address,
                "status": status,
                "field_value": field_value,
                "metadata": metadata,
                "description": description,
                "description_en": description_en,
                "category": category,
                "slug": slug,
                "post_install_alert": post_install_alert,
                "license": license,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field_value"]) -> MetaOapg.properties.field_value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'StructuresSoftwareMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description_en"]) -> MetaOapg.properties.description_en: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["post_install_alert"]) -> MetaOapg.properties.post_install_alert: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["license"]) -> MetaOapg.properties.license: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "display_name", "version", "address", "status", "field_value", "metadata", "description", "description_en", "category", "slug", "post_install_alert", "license", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_name"]) -> typing.Union[MetaOapg.properties.display_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> typing.Union[MetaOapg.properties.version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union[MetaOapg.properties.address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field_value"]) -> typing.Union[MetaOapg.properties.field_value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['StructuresSoftwareMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description_en"]) -> typing.Union[MetaOapg.properties.description_en, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union[MetaOapg.properties.category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slug"]) -> typing.Union[MetaOapg.properties.slug, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["post_install_alert"]) -> typing.Union[MetaOapg.properties.post_install_alert, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["license"]) -> typing.Union[MetaOapg.properties.license, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "display_name", "version", "address", "status", "field_value", "metadata", "description", "description_en", "category", "slug", "post_install_alert", "license", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        display_name: typing.Union[MetaOapg.properties.display_name, str, schemas.Unset] = schemas.unset,
        version: typing.Union[MetaOapg.properties.version, str, schemas.Unset] = schemas.unset,
        address: typing.Union[MetaOapg.properties.address, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        field_value: typing.Union[MetaOapg.properties.field_value, list, tuple, schemas.Unset] = schemas.unset,
        metadata: typing.Union['StructuresSoftwareMetadata', schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        description_en: typing.Union[MetaOapg.properties.description_en, str, schemas.Unset] = schemas.unset,
        category: typing.Union[MetaOapg.properties.category, list, tuple, schemas.Unset] = schemas.unset,
        slug: typing.Union[MetaOapg.properties.slug, str, schemas.Unset] = schemas.unset,
        post_install_alert: typing.Union[MetaOapg.properties.post_install_alert, bool, schemas.Unset] = schemas.unset,
        license: typing.Union[MetaOapg.properties.license, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StructuresInstalledSoftwareInfo':
        return super().__new__(
            cls,
            *args,
            name=name,
            display_name=display_name,
            version=version,
            address=address,
            status=status,
            field_value=field_value,
            metadata=metadata,
            description=description,
            description_en=description_en,
            category=category,
            slug=slug,
            post_install_alert=post_install_alert,
            license=license,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_vps.model.structures_installed_software_info_field_value import StructuresInstalledSoftwareInfoFieldValue
from beget_openapi_vps.model.structures_issued_software_license import StructuresIssuedSoftwareLicense
from beget_openapi_vps.model.structures_software_category import StructuresSoftwareCategory
from beget_openapi_vps.model.structures_software_metadata import StructuresSoftwareMetadata
