# swagger_client.ItmTa1Ta3Api

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_probe**](ItmTa1Ta3Api.md#add_probe) | **POST** /ta1/probe/{scenario_id} | Create a new evaluation probe
[**add_scenario**](ItmTa1Ta3Api.md#add_scenario) | **POST** /ta1/scenario | Create a new evaluation scenario
[**delete_probe**](ItmTa1Ta3Api.md#delete_probe) | **DELETE** /ta1/probe/{probe_id} | Delete an evaluation probe
[**delete_scenario**](ItmTa1Ta3Api.md#delete_scenario) | **DELETE** /ta1/scenario/{scenario_id} | Delete an evaluation scenario
[**ta1login**](ItmTa1Ta3Api.md#ta1login) | **GET** /ta1/login | Log in with TA3
[**update_probe**](ItmTa1Ta3Api.md#update_probe) | **PUT** /ta1/probe | Update an existing evaluation probe
[**update_scenario**](ItmTa1Ta3Api.md#update_scenario) | **PUT** /ta1/scenario | Update an existing evaluation scenario

# **add_probe**
> str add_probe(body, api_key, scenario_id)

Create a new evaluation probe

Create a new evaluation probe for the specified scenario.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa1Ta3Api()
body = swagger_client.Probe() # Probe | Create a new evaluation probe
api_key = 'api_key_example' # str | API Key received when logging in.  Can add robust authentication later.
scenario_id = 'scenario_id_example' # str | A scenario ID, as returned when adding a scenario

try:
    # Create a new evaluation probe
    api_response = api_instance.add_probe(body, api_key, scenario_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa1Ta3Api->add_probe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Probe**](Probe.md)| Create a new evaluation probe | 
 **api_key** | **str**| API Key received when logging in.  Can add robust authentication later. | 
 **scenario_id** | **str**| A scenario ID, as returned when adding a scenario | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_scenario**
> str add_scenario(body, api_key)

Create a new evaluation scenario

Create a new evaluation scenario

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa1Ta3Api()
body = swagger_client.Scenario() # Scenario | Create a new evaluation scenario
api_key = 'api_key_example' # str | API Key received when logging in.  Can add robust authentication later.

try:
    # Create a new evaluation scenario
    api_response = api_instance.add_scenario(body, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa1Ta3Api->add_scenario: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Scenario**](Scenario.md)| Create a new evaluation scenario | 
 **api_key** | **str**| API Key received when logging in.  Can add robust authentication later. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_probe**
> delete_probe(api_key, probe_id)

Delete an evaluation probe

Delete an evaluation probe by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa1Ta3Api()
api_key = 'api_key_example' # str | API Key received when logging in.  Can add robust authentication later.
probe_id = 'probe_id_example' # str | A scenario ID, as returned when adding a scenario

try:
    # Delete an evaluation probe
    api_instance.delete_probe(api_key, probe_id)
except ApiException as e:
    print("Exception when calling ItmTa1Ta3Api->delete_probe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| API Key received when logging in.  Can add robust authentication later. | 
 **probe_id** | **str**| A scenario ID, as returned when adding a scenario | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scenario**
> delete_scenario(api_key, scenario_id)

Delete an evaluation scenario

Delete an evaluation scenario by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa1Ta3Api()
api_key = 'api_key_example' # str | API Key received when logging in.  Can add robust authentication later.
scenario_id = 'scenario_id_example' # str | A scenario ID, as returned when adding a scenario

try:
    # Delete an evaluation scenario
    api_instance.delete_scenario(api_key, scenario_id)
except ApiException as e:
    print("Exception when calling ItmTa1Ta3Api->delete_scenario: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| API Key received when logging in.  Can add robust authentication later. | 
 **scenario_id** | **str**| A scenario ID, as returned when adding a scenario | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ta1login**
> str ta1login(username)

Log in with TA3

Start a new API session with the specified username

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa1Ta3Api()
username = 'username_example' # str | A self-assigned user name.  Can add authentication later.

try:
    # Log in with TA3
    api_response = api_instance.ta1login(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa1Ta3Api->ta1login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| A self-assigned user name.  Can add authentication later. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_probe**
> update_probe(body, api_key)

Update an existing evaluation probe

Update an existing evaluation probe by Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa1Ta3Api()
body = swagger_client.Probe() # Probe | new evaluation probe configuration
api_key = 'api_key_example' # str | API Key received when logging in.  Can add robust authentication later.

try:
    # Update an existing evaluation probe
    api_instance.update_probe(body, api_key)
except ApiException as e:
    print("Exception when calling ItmTa1Ta3Api->update_probe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Probe**](Probe.md)| new evaluation probe configuration | 
 **api_key** | **str**| API Key received when logging in.  Can add robust authentication later. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scenario**
> update_scenario(body, api_key)

Update an existing evaluation scenario

Update an existing evaluation scenario by Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa1Ta3Api()
body = swagger_client.Scenario() # Scenario | new evaluation scenario configuration
api_key = 'api_key_example' # str | API Key received when logging in.  Can add robust authentication later.

try:
    # Update an existing evaluation scenario
    api_instance.update_scenario(body, api_key)
except ApiException as e:
    print("Exception when calling ItmTa1Ta3Api->update_scenario: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Scenario**](Scenario.md)| new evaluation scenario configuration | 
 **api_key** | **str**| API Key received when logging in.  Can add robust authentication later. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

