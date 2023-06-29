# Scenario

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | a globally unique id for the scenario | [default to '1234']
**name** | **str** | human-readable scenario name, not necessarily unique | 
**session_complete** | **bool** | set to true if the session is complete; that is, there are no more scenarios | [optional] 
**start_time** | **str** | the wall clock local start time of the scenario, expressed as hh:mm | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**triage_categories** | [**list[TriageCategory]**](TriageCategory.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

