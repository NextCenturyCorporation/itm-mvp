# swagger_client.ItmTa2EvalApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_vitals**](ItmTa2EvalApi.md#check_vitals) | **GET** /ta2/casualty/{casualty_id}/checkVitals | Assess and retrieve all casualty vital signs
[**get_alignment_target**](ItmTa2EvalApi.md#get_alignment_target) | **GET** /ta2/{scenario_id}/getAlignmentTarget | Retrieve alignment target for the scenario
[**get_heart_rate**](ItmTa2EvalApi.md#get_heart_rate) | **GET** /ta2/casualty/{casualty_id}/checkHeartRate | Check casualty heart rate
[**get_probe**](ItmTa2EvalApi.md#get_probe) | **GET** /ta2/probe | Request a probe
[**get_scenario_state**](ItmTa2EvalApi.md#get_scenario_state) | **GET** /ta2/{scenario_id}/getState | Retrieve scenario state
[**respond_to_probe**](ItmTa2EvalApi.md#respond_to_probe) | **POST** /ta2/probe | Respond to a probe
[**start_scenario**](ItmTa2EvalApi.md#start_scenario) | **GET** /ta2/start | Get the next scenario
[**start_session**](ItmTa2EvalApi.md#start_session) | **GET** /ta2/startSession | Start a new session
[**tag_casualty**](ItmTa2EvalApi.md#tag_casualty) | **POST** /ta2/casualty/{casualty_id}/tag | Tag a casualty with a triage category

# **check_vitals**
> Vitals check_vitals(casualty_id)

Assess and retrieve all casualty vital signs

Retrieve all vital signs of the specified casualty.  Not required for MVP, but anticipated as an example of finer-grained choices that may be available post-MVP

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi()
casualty_id = 'casualty_id_example' # str | The ID of the casualty to query

try:
    # Assess and retrieve all casualty vital signs
    api_response = api_instance.check_vitals(casualty_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->check_vitals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **casualty_id** | **str**| The ID of the casualty to query | 

### Return type

[**Vitals**](Vitals.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alignment_target**
> AlignmentTarget get_alignment_target(scenario_id)

Retrieve alignment target for the scenario

Retrieve alignment target for the scenario with the specified id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi()
scenario_id = 'scenario_id_example' # str | The ID of the scenario for which to retrieve alignment target

try:
    # Retrieve alignment target for the scenario
    api_response = api_instance.get_alignment_target(scenario_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->get_alignment_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario_id** | **str**| The ID of the scenario for which to retrieve alignment target | 

### Return type

[**AlignmentTarget**](AlignmentTarget.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heart_rate**
> int get_heart_rate(casualty_id)

Check casualty heart rate

Check the heart rate of the specified casualty.  Not required for MVP, but anticipated as an example of finer-grained choices that may be available post-MVP

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi()
casualty_id = 'casualty_id_example' # str | The ID of the casualty to for which to request heart rate

try:
    # Check casualty heart rate
    api_response = api_instance.get_heart_rate(casualty_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->get_heart_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **casualty_id** | **str**| The ID of the casualty to for which to request heart rate | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_probe**
> Probe get_probe(scenario_id)

Request a probe

Request the next probe of the scenario with the specified id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi()
scenario_id = 'scenario_id_example' # str | The ID of the scenario for which to request a probe

try:
    # Request a probe
    api_response = api_instance.get_probe(scenario_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->get_probe: %s\n" % e)
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
> State get_scenario_state(scenario_id)

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
api_instance = swagger_client.ItmTa2EvalApi()
scenario_id = 'scenario_id_example' # str | The ID of the scenario for which to retrieve status

try:
    # Retrieve scenario state
    api_response = api_instance.get_scenario_state(scenario_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->get_scenario_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario_id** | **str**| The ID of the scenario for which to retrieve status | 

### Return type

[**State**](State.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **respond_to_probe**
> State respond_to_probe(body=body)

Respond to a probe

Respond to a probe with a decision chosen from among its options

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi()
body = swagger_client.ProbeResponse() # ProbeResponse | the selection by a DM of an option in response to a probe (optional)

try:
    # Respond to a probe
    api_response = api_instance.respond_to_probe(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->respond_to_probe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProbeResponse**](ProbeResponse.md)| the selection by a DM of an option in response to a probe | [optional] 

### Return type

[**State**](State.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_scenario**
> Scenario start_scenario(adm_name, scenario_id=scenario_id)

Get the next scenario

Get the next scenario in a session with the specified ADM name, returning a Scenario object and unique id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi()
adm_name = 'adm_name_example' # str | A self-assigned ADM name.  Can add authentication later.
scenario_id = 'scenario_id_example' # str | a scenario id to start, used internally by TA3 (optional)

try:
    # Get the next scenario
    api_response = api_instance.start_scenario(adm_name, scenario_id=scenario_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->start_scenario: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adm_name** | **str**| A self-assigned ADM name.  Can add authentication later. | 
 **scenario_id** | **str**| a scenario id to start, used internally by TA3 | [optional] 

### Return type

[**Scenario**](Scenario.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_session**
> str start_session(adm_name, type, max_scenarios=max_scenarios)

Start a new session

Start a new session with the specified ADM name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi()
adm_name = 'adm_name_example' # str | A self-assigned ADM name.  Can add authentication later.
type = 'type_example' # str | the type of session to start (test, eval, or a ta1 name)
max_scenarios = 56 # int | the maximum number of scenarios requested (optional)

try:
    # Start a new session
    api_response = api_instance.start_session(adm_name, type, max_scenarios=max_scenarios)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->start_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adm_name** | **str**| A self-assigned ADM name.  Can add authentication later. | 
 **type** | **str**| the type of session to start (test, eval, or a ta1 name) | 
 **max_scenarios** | **int**| the maximum number of scenarios requested | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_casualty**
> str tag_casualty(casualty_id, tag)

Tag a casualty with a triage category

Apply a triage tag to the specified casualty with the specified tag

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi()
casualty_id = 'casualty_id_example' # str | The ID of the casualty to tag
tag = 'tag_example' # str | The tag to apply to the casualty, chosen from triage categories

try:
    # Tag a casualty with a triage category
    api_response = api_instance.tag_casualty(casualty_id, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->tag_casualty: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **casualty_id** | **str**| The ID of the casualty to tag | 
 **tag** | **str**| The tag to apply to the casualty, chosen from triage categories | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

