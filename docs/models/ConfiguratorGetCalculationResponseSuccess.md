# beget_openapi_vps.model.configurator_get_calculation_response_success.ConfiguratorGetCalculationResponseSuccess

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**settings** | [**ConfiguratorConfiguratorSettings**](ConfiguratorConfiguratorSettings.md) | [**ConfiguratorConfiguratorSettings**](ConfiguratorConfiguratorSettings.md) |  | [optional] 
**params** | [**StructuresConfigurationParams**](StructuresConfigurationParams.md) | [**StructuresConfigurationParams**](StructuresConfigurationParams.md) |  | [optional] 
**price_day** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**price_month** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

