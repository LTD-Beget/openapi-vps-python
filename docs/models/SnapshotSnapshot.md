# beget_openapi_vps.model.snapshot_snapshot.SnapshotSnapshot

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**vps_id** | str,  | str,  |  | [optional] 
**vps_name** | str,  | str,  |  | [optional] 
**vps_exists** | bool,  | BoolClass,  |  | [optional] 
**date_create** | str,  | str,  |  | [optional] 
**size** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] must be one of ["CREATING", "DONE", "RESTORING", "DELETED", ] 
**description** | str,  | str,  |  | [optional] 
**configuration** | [**SnapshotRequiredConfiguration**](SnapshotRequiredConfiguration.md) | [**SnapshotRequiredConfiguration**](SnapshotRequiredConfiguration.md) |  | [optional] 
**price_day** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**region** | str,  | str,  |  | [optional] 
**installed_software** | [**StructuresInstalledSoftwareInfo**](StructuresInstalledSoftwareInfo.md) | [**StructuresInstalledSoftwareInfo**](StructuresInstalledSoftwareInfo.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

