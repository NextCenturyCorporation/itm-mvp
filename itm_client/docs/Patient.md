# Patient

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the patient id, having scenario scope | [optional] 
**name** | **str** | the name of the patient | [optional] 
**age** | **int** | the age of the patient | [optional] 
**sex** | **str** | the sex of the patient, or unknown | [optional] 
**injuries** | [**list[Injury]**](Injury.md) | an array of patient injuries | [optional] 
**vitals** | [**Vitals**](Vitals.md) |  | [optional] 
**mental_status** | **str** | mood and apparent mental state | [optional] 
**assessed** | **bool** | whether or not this patient has been assessed in the current scenario | [optional] 
**tag** | **str** | the tag assigned to this patient, or none if untagged | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

