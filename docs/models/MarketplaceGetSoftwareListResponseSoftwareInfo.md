# beget_openapi_vps.model.marketplace_get_software_list_response_software_info.MarketplaceGetSoftwareListResponseSoftwareInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**display_name** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**description_en** | str,  | str,  |  | [optional] 
**metadata** | [**StructuresSoftwareMetadata**](StructuresSoftwareMetadata.md) | [**StructuresSoftwareMetadata**](StructuresSoftwareMetadata.md) |  | [optional] 
**[field_data](#field_data)** | list, tuple,  | tuple,  |  | [optional] 
**requirements** | [**MarketplaceGetSoftwareListResponseSoftwareInfoRequirements**](MarketplaceGetSoftwareListResponseSoftwareInfoRequirements.md) | [**MarketplaceGetSoftwareListResponseSoftwareInfoRequirements**](MarketplaceGetSoftwareListResponseSoftwareInfoRequirements.md) |  | [optional] 
**[category](#category)** | list, tuple,  | tuple,  |  | [optional] 
**slug** | str,  | str,  |  | [optional] 
**documentation_slug** | str,  | str,  |  | [optional] 
**unattended_install_available** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# field_data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MarketplaceFieldDesc**](MarketplaceFieldDesc.md) | [**MarketplaceFieldDesc**](MarketplaceFieldDesc.md) | [**MarketplaceFieldDesc**](MarketplaceFieldDesc.md) |  | 

# category

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**StructuresSoftwareCategory**](StructuresSoftwareCategory.md) | [**StructuresSoftwareCategory**](StructuresSoftwareCategory.md) | [**StructuresSoftwareCategory**](StructuresSoftwareCategory.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

