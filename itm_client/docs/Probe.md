# Probe

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | globally unique probe ID | 
**scenario_id** | **str** | scenario ID this probe is for | 
**type** | **str** | TAs will need to agree on the types of questions being asked; only MultipleChoice is supported for MVP | 
**prompt** | **str** | a plain text natural language question for the DM | 
**state** | [**State**](State.md) |  | [optional] 
**options** | [**list[ProbeOption]**](ProbeOption.md) | the list of valid choices for the DM to choose among | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

