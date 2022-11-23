# beget_openapi_vps.model.structures_installed_software_info.StructuresInstalledSoftwareInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**display_name** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**address** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] must be one of ["PENDING", "INSTALLING", "INSTALLED", "ERROR", "CANCEL", ] 
**[field_value](#field_value)** | list, tuple,  | tuple,  |  | [optional] 
**metadata** | [**StructuresSoftwareMetadata**](StructuresSoftwareMetadata.md) | [**StructuresSoftwareMetadata**](StructuresSoftwareMetadata.md) |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**description_en** | str,  | str,  |  | [optional] 
**[category](#category)** | list, tuple,  | tuple,  |  | [optional] 
**slug** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# field_value

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**StructuresInstalledSoftwareInfoFieldValue**](StructuresInstalledSoftwareInfoFieldValue.md) | [**StructuresInstalledSoftwareInfoFieldValue**](StructuresInstalledSoftwareInfoFieldValue.md) | [**StructuresInstalledSoftwareInfoFieldValue**](StructuresInstalledSoftwareInfoFieldValue.md) |  | 

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

