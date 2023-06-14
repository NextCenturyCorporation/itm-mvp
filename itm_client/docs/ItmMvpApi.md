# swagger_client.ItmMvpApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_patient_heart_rate**](ItmMvpApi.md#get_patient_heart_rate) | **GET** /patient/{patientId}/getHeartRate | Retrieve patient heart rate
[**get_patient_vitals**](ItmMvpApi.md#get_patient_vitals) | **GET** /patient/{patientId}/getVitals | Retrieve all patient vital signs
[**get_probe**](ItmMvpApi.md#get_probe) | **GET** /scenario/probe | Request the next probe
[**get_scenario_state**](ItmMvpApi.md#get_scenario_state) | **GET** /scenario/{scenarioId}/getState | Retrieve scenario state
[**respond_to_probe**](ItmMvpApi.md#respond_to_probe) | **POST** /scenario/probe | Respond to a probe
[**start_scenario**](ItmMvpApi.md#start_scenario) | **GET** /scenario/start | Start a new scenario
[**tag_patient**](ItmMvpApi.md#tag_patient) | **POST** /patient/{patientId}/tag | Tag a patient with a triage category

# **get_patient_heart_rate**
> int get_patient_heart_rate(scenario_id, patient_id)

Retrieve patient heart rate

This is just here to discuss whether we will someday have/need this level of granularity, probably not for MVP

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmMvpApi()
scenario_id = 'scenario_id_example' # str | The ID of the scenario containing the specified patient
patient_id = 'patient_id_example' # str | The ID of the patient to for which to request heart rate

try:
    # Retrieve patient heart rate
    api_response = api_instance.get_patient_heart_rate(scenario_id, patient_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmMvpApi->get_patient_heart_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario_id** | **str**| The ID of the scenario containing the specified patient | 
 **patient_id** | **str**| The ID of the patient to for which to request heart rate | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_patient_vitals**
> Vitals get_patient_vitals(scenario_id, patient_id)

Retrieve all patient vital signs

Retrieve all vital signs of the specified patient in the specified scenario.  May not need this for MVP.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmMvpApi()
scenario_id = 'scenario_id_example' # str | The ID of the scenario for which to request patient vitals
patient_id = 'patient_id_example' # str | The ID of the patient to query

try:
    # Retrieve all patient vital signs
    api_response = api_instance.get_patient_vitals(scenario_id, patient_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmMvpApi->get_patient_vitals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario_id** | **str**| The ID of the scenario for which to request patient vitals | 
 **patient_id** | **str**| The ID of the patient to query | 

### Return type

[**Vitals**](Vitals.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_probe**
> Probe get_probe(scenario_id)

Request the next probe

Request the next probe of the scenario with the specified id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmMvpApi()
scenario_id = 'scenario_id_example' # str | The ID of the scenario for which to request a probe

try:
    # Request the next probe
    api_response = api_instance.get_probe(scenario_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmMvpApi->get_probe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario_id** | **str**| The ID of the scenario for which to request a probe | 

### Return type

[**Probe**](Probe.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenario_state**
> ScenarioState get_scenario_state(scenario_id)

Retrieve scenario state

Retrieve state of the scenario with the specified id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmMvpApi()
scenario_id = 'scenario_id_example' # str | The ID of the scenario for which to retrieve status

try:
    # Retrieve scenario state
    api_response = api_instance.get_scenario_state(scenario_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmMvpApi->get_scenario_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario_id** | **str**| The ID of the scenario for which to retrieve status | 

### Return type

[**ScenarioState**](ScenarioState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **respond_to_probe**
> ScenarioState respond_to_probe(probe_id, patient_id, explanation=explanation)

Respond to a probe

Respond to the specified probe with the specified patient_id (decision) and optional explanation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmMvpApi()
probe_id = 'probe_id_example' # str | The ID of the probe to which to respond
patient_id = 'patient_id_example' # str | The ID of the patient to treat
explanation = 'explanation_example' # str | An explanation of the response to the probe (optional)

try:
    # Respond to a probe
    api_response = api_instance.respond_to_probe(probe_id, patient_id, explanation=explanation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmMvpApi->respond_to_probe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **probe_id** | **str**| The ID of the probe to which to respond | 
 **patient_id** | **str**| The ID of the patient to treat | 
 **explanation** | **str**| An explanation of the response to the probe | [optional] 

### Return type

[**ScenarioState**](ScenarioState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_scenario**
> Scenario start_scenario(username)

Start a new scenario

Start a new scenario with the specified username, returning a Scenario object and unique id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmMvpApi()
username = 'username_example' # str | A self-assigned user name.  Can add authentication later.

try:
    # Start a new scenario
    api_response = api_instance.start_scenario(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmMvpApi->start_scenario: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| A self-assigned user name.  Can add authentication later. | 

### Return type

[**Scenario**](Scenario.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_patient**
> str tag_patient(scenario_id, patient_id, tag)

Tag a patient with a triage category

Apply a triage tag to the specified patient with the specified tag

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmMvpApi()
scenario_id = 'scenario_id_example' # str | The ID of the scenario containing the specified patient
patient_id = 'patient_id_example' # str | The ID of the patient to tag
tag = 'tag_example' # str | The tag to apply to the patient, chosen from triage categories

try:
    # Tag a patient with a triage category
    api_response = api_instance.tag_patient(scenario_id, patient_id, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmMvpApi->tag_patient: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario_id** | **str**| The ID of the scenario containing the specified patient | 
 **patient_id** | **str**| The ID of the patient to tag | 
 **tag** | **str**| The tag to apply to the patient, chosen from triage categories | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
