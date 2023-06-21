# Casualty

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | string, globally unique casualty identifier | 
**unstructured** | **str** | natural language text description of the casualty | 
**name** | **str** | the name of the casualty, omit if unknown | [optional] 
**demographics** | [**Demographics**](Demographics.md) |  | [optional] 
**injuries** | [**list[Injury]**](Injury.md) | an array of casualty injuries | [optional] 
**vitals** | [**Vitals**](Vitals.md) |  | [optional] 
**assessed** | **bool** | whether or not this casualty has been assessed in the current scenario | [optional] [default to False]
**tag** | **str** | the tag assigned to this casualty, omit if untagged | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

