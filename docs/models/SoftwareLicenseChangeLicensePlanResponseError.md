# beget_openapi_vps.model.software_license_change_license_plan_response_error.SoftwareLicenseChangeLicensePlanResponseError

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  |  | [optional] must be one of ["INTERNAL_ERROR", "INSUFFICIENT_FUNDS", "SERVICE_DISABLED", ] 
**message** | str,  | str,  |  | [optional] 
**insufficient_funds_error** | [**SoftwareLicenseChangeLicensePlanResponseErrorInsufficientFundsError**](SoftwareLicenseChangeLicensePlanResponseErrorInsufficientFundsError.md) | [**SoftwareLicenseChangeLicensePlanResponseErrorInsufficientFundsError**](SoftwareLicenseChangeLicensePlanResponseErrorInsufficientFundsError.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

