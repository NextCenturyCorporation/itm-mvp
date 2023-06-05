# ScenarioState

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | a unique id for the scenario | [optional] 
**name** | **str** | the scenario name | [optional] 
**elapsed_time** | **float** | the elapsed time (in minutes) since the scenario started | [optional] 
**scenario_complete** | **bool** | set to true if the scenario is complete; subsequent calls to /scenario/probe will return an error code | [optional] 
**patients** | [**list[Patient]**](Patient.md) | the list of patients in the scenario | [optional] 
**medical_supplies** | [**list[MedicalSupply]**](MedicalSupply.md) | a list of medical supplies available to the medic | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

