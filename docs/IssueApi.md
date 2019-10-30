# giteapy.IssueApi

All URIs are relative to *http://localhost:3000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**issue_add_label**](IssueApi.md#issue_add_label) | **POST** /repos/{owner}/{repo}/issues/{index}/labels | Add a label to an issue
[**issue_add_time**](IssueApi.md#issue_add_time) | **POST** /repos/{owner}/{repo}/issues/{id}/times | Add a tracked time to a issue
[**issue_clear_labels**](IssueApi.md#issue_clear_labels) | **DELETE** /repos/{owner}/{repo}/issues/{index}/labels | Remove all labels from an issue
[**issue_create_comment**](IssueApi.md#issue_create_comment) | **POST** /repos/{owner}/{repo}/issues/{index}/comments | Add a comment to an issue
[**issue_create_issue**](IssueApi.md#issue_create_issue) | **POST** /repos/{owner}/{repo}/issues | Create an issue. If using deadline only the date will be taken into account, and time of day ignored.
[**issue_create_label**](IssueApi.md#issue_create_label) | **POST** /repos/{owner}/{repo}/labels | Create a label
[**issue_create_milestone**](IssueApi.md#issue_create_milestone) | **POST** /repos/{owner}/{repo}/milestones | Create a milestone
[**issue_delete_comment**](IssueApi.md#issue_delete_comment) | **DELETE** /repos/{owner}/{repo}/issues/comments/{id} | Delete a comment
[**issue_delete_comment_deprecated**](IssueApi.md#issue_delete_comment_deprecated) | **DELETE** /repos/{owner}/{repo}/issues/{index}/comments/{id} | Delete a comment
[**issue_delete_label**](IssueApi.md#issue_delete_label) | **DELETE** /repos/{owner}/{repo}/labels/{id} | Delete a label
[**issue_delete_milestone**](IssueApi.md#issue_delete_milestone) | **DELETE** /repos/{owner}/{repo}/milestones/{id} | Delete a milestone
[**issue_edit_comment**](IssueApi.md#issue_edit_comment) | **PATCH** /repos/{owner}/{repo}/issues/comments/{id} | Edit a comment
[**issue_edit_comment_deprecated**](IssueApi.md#issue_edit_comment_deprecated) | **PATCH** /repos/{owner}/{repo}/issues/{index}/comments/{id} | Edit a comment
[**issue_edit_issue**](IssueApi.md#issue_edit_issue) | **PATCH** /repos/{owner}/{repo}/issues/{index} | Edit an issue. If using deadline only the date will be taken into account, and time of day ignored.
[**issue_edit_issue_deadline**](IssueApi.md#issue_edit_issue_deadline) | **POST** /repos/{owner}/{repo}/issues/{index}/deadline | Set an issue deadline. If set to null, the deadline is deleted. If using deadline only the date will be taken into account, and time of day ignored.
[**issue_edit_label**](IssueApi.md#issue_edit_label) | **PATCH** /repos/{owner}/{repo}/labels/{id} | Update a label
[**issue_edit_milestone**](IssueApi.md#issue_edit_milestone) | **PATCH** /repos/{owner}/{repo}/milestones/{id} | Update a milestone
[**issue_get_comments**](IssueApi.md#issue_get_comments) | **GET** /repos/{owner}/{repo}/issues/{index}/comments | List all comments on an issue
[**issue_get_issue**](IssueApi.md#issue_get_issue) | **GET** /repos/{owner}/{repo}/issues/{index} | Get an issue
[**issue_get_label**](IssueApi.md#issue_get_label) | **GET** /repos/{owner}/{repo}/labels/{id} | Get a single label
[**issue_get_labels**](IssueApi.md#issue_get_labels) | **GET** /repos/{owner}/{repo}/issues/{index}/labels | Get an issue&#39;s labels
[**issue_get_milestone**](IssueApi.md#issue_get_milestone) | **GET** /repos/{owner}/{repo}/milestones/{id} | Get a milestone
[**issue_get_milestones_list**](IssueApi.md#issue_get_milestones_list) | **GET** /repos/{owner}/{repo}/milestones | Get all of a repository&#39;s opened milestones
[**issue_get_repo_comments**](IssueApi.md#issue_get_repo_comments) | **GET** /repos/{owner}/{repo}/issues/comments | List all comments in a repository
[**issue_list_issues**](IssueApi.md#issue_list_issues) | **GET** /repos/{owner}/{repo}/issues | List a repository&#39;s issues
[**issue_list_labels**](IssueApi.md#issue_list_labels) | **GET** /repos/{owner}/{repo}/labels | Get all of a repository&#39;s labels
[**issue_remove_label**](IssueApi.md#issue_remove_label) | **DELETE** /repos/{owner}/{repo}/issues/{index}/labels/{id} | Remove a label from an issue
[**issue_replace_labels**](IssueApi.md#issue_replace_labels) | **PUT** /repos/{owner}/{repo}/issues/{index}/labels | Replace an issue&#39;s labels
[**issue_start_stop_watch**](IssueApi.md#issue_start_stop_watch) | **POST** /repos/{owner}/{repo}/issues/{index}/stopwatch/start | Start stopwatch on an issue.
[**issue_stop_watch**](IssueApi.md#issue_stop_watch) | **POST** /repos/{owner}/{repo}/issues/{index}/stopwatch/stop | Stop an issue&#39;s existing stopwatch.
[**issue_tracked_times**](IssueApi.md#issue_tracked_times) | **GET** /repos/{owner}/{repo}/issues/{id}/times | List an issue&#39;s tracked times


# **issue_add_label**
> list[Label] issue_add_label(owner, repo, index, body=body)

Add a label to an issue

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
index = 789 # int | index of the issue
body = giteapy.IssueLabelsOption() # IssueLabelsOption |  (optional)

try:
    # Add a label to an issue
    api_response = api_instance.issue_add_label(owner, repo, index, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_add_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **body** | [**IssueLabelsOption**](IssueLabelsOption.md)|  | [optional]

### Return type

[**list[Label]**](Label.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_add_time**
> TrackedTime issue_add_time(owner, repo, id, body=body)

Add a tracked time to a issue

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | index of the issue to add tracked time to
body = giteapy.AddTimeOption() # AddTimeOption |  (optional)

try:
    # Add a tracked time to a issue
    api_response = api_instance.issue_add_time(owner, repo, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_add_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| index of the issue to add tracked time to |
 **body** | [**AddTimeOption**](AddTimeOption.md)|  | [optional]

### Return type

[**TrackedTime**](TrackedTime.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_clear_labels**
> issue_clear_labels(owner, repo, index)

Remove all labels from an issue

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
index = 789 # int | index of the issue

try:
    # Remove all labels from an issue
    api_instance.issue_clear_labels(owner, repo, index)
except ApiException as e:
    print("Exception when calling IssueApi->issue_clear_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_create_comment**
> Comment issue_create_comment(owner, repo, index, body=body)

Add a comment to an issue

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
index = 789 # int | index of the issue
body = giteapy.CreateIssueCommentOption() # CreateIssueCommentOption |  (optional)

try:
    # Add a comment to an issue
    api_response = api_instance.issue_create_comment(owner, repo, index, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_create_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **body** | [**CreateIssueCommentOption**](CreateIssueCommentOption.md)|  | [optional]

### Return type

[**Comment**](Comment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_create_issue**
> Issue issue_create_issue(owner, repo, body=body)

Create an issue. If using deadline only the date will be taken into account, and time of day ignored.

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
body = giteapy.CreateIssueOption() # CreateIssueOption |  (optional)

try:
    # Create an issue. If using deadline only the date will be taken into account, and time of day ignored.
    api_response = api_instance.issue_create_issue(owner, repo, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_create_issue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **body** | [**CreateIssueOption**](CreateIssueOption.md)|  | [optional]

### Return type

[**Issue**](Issue.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_create_label**
> Label issue_create_label(owner, repo, body=body)

Create a label

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
body = giteapy.CreateLabelOption() # CreateLabelOption |  (optional)

try:
    # Create a label
    api_response = api_instance.issue_create_label(owner, repo, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_create_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **body** | [**CreateLabelOption**](CreateLabelOption.md)|  | [optional]

### Return type

[**Label**](Label.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_create_milestone**
> Milestone issue_create_milestone(owner, repo, body=body)

Create a milestone

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
body = giteapy.CreateMilestoneOption() # CreateMilestoneOption |  (optional)

try:
    # Create a milestone
    api_response = api_instance.issue_create_milestone(owner, repo, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_create_milestone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **body** | [**CreateMilestoneOption**](CreateMilestoneOption.md)|  | [optional]

### Return type

[**Milestone**](Milestone.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_delete_comment**
> issue_delete_comment(owner, repo, id)

Delete a comment

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | id of comment to delete

try:
    # Delete a comment
    api_instance.issue_delete_comment(owner, repo, id)
except ApiException as e:
    print("Exception when calling IssueApi->issue_delete_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of comment to delete |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_delete_comment_deprecated**
> issue_delete_comment_deprecated(owner, repo, index, id)

Delete a comment

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
index = 56 # int | this parameter is ignored
id = 789 # int | id of comment to delete

try:
    # Delete a comment
    api_instance.issue_delete_comment_deprecated(owner, repo, index, id)
except ApiException as e:
    print("Exception when calling IssueApi->issue_delete_comment_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| this parameter is ignored |
 **id** | **int**| id of comment to delete |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_delete_label**
> issue_delete_label(owner, repo, id)

Delete a label

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | id of the label to delete

try:
    # Delete a label
    api_instance.issue_delete_label(owner, repo, id)
except ApiException as e:
    print("Exception when calling IssueApi->issue_delete_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the label to delete |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_delete_milestone**
> issue_delete_milestone(owner, repo, id)

Delete a milestone

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | id of the milestone to delete

try:
    # Delete a milestone
    api_instance.issue_delete_milestone(owner, repo, id)
except ApiException as e:
    print("Exception when calling IssueApi->issue_delete_milestone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the milestone to delete |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_edit_comment**
> Comment issue_edit_comment(owner, repo, id, body=body)

Edit a comment

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | id of the comment to edit
body = giteapy.EditIssueCommentOption() # EditIssueCommentOption |  (optional)

try:
    # Edit a comment
    api_response = api_instance.issue_edit_comment(owner, repo, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_edit_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the comment to edit |
 **body** | [**EditIssueCommentOption**](EditIssueCommentOption.md)|  | [optional]

### Return type

[**Comment**](Comment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_edit_comment_deprecated**
> Comment issue_edit_comment_deprecated(owner, repo, index, id, body=body)

Edit a comment

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
index = 56 # int | this parameter is ignored
id = 789 # int | id of the comment to edit
body = giteapy.EditIssueCommentOption() # EditIssueCommentOption |  (optional)

try:
    # Edit a comment
    api_response = api_instance.issue_edit_comment_deprecated(owner, repo, index, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_edit_comment_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| this parameter is ignored |
 **id** | **int**| id of the comment to edit |
 **body** | [**EditIssueCommentOption**](EditIssueCommentOption.md)|  | [optional]

### Return type

[**Comment**](Comment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_edit_issue**
> Issue issue_edit_issue(owner, repo, index, body=body)

Edit an issue. If using deadline only the date will be taken into account, and time of day ignored.

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
index = 789 # int | index of the issue to edit
body = giteapy.EditIssueOption() # EditIssueOption |  (optional)

try:
    # Edit an issue. If using deadline only the date will be taken into account, and time of day ignored.
    api_response = api_instance.issue_edit_issue(owner, repo, index, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_edit_issue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue to edit |
 **body** | [**EditIssueOption**](EditIssueOption.md)|  | [optional]

### Return type

[**Issue**](Issue.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_edit_issue_deadline**
> IssueDeadline issue_edit_issue_deadline(owner, repo, index, body=body)

Set an issue deadline. If set to null, the deadline is deleted. If using deadline only the date will be taken into account, and time of day ignored.

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
index = 789 # int | index of the issue to create or update a deadline on
body = giteapy.EditDeadlineOption() # EditDeadlineOption |  (optional)

try:
    # Set an issue deadline. If set to null, the deadline is deleted. If using deadline only the date will be taken into account, and time of day ignored.
    api_response = api_instance.issue_edit_issue_deadline(owner, repo, index, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_edit_issue_deadline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue to create or update a deadline on |
 **body** | [**EditDeadlineOption**](EditDeadlineOption.md)|  | [optional]

### Return type

[**IssueDeadline**](IssueDeadline.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_edit_label**
> Label issue_edit_label(owner, repo, id, body=body)

Update a label

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | id of the label to edit
body = giteapy.EditLabelOption() # EditLabelOption |  (optional)

try:
    # Update a label
    api_response = api_instance.issue_edit_label(owner, repo, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_edit_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the label to edit |
 **body** | [**EditLabelOption**](EditLabelOption.md)|  | [optional]

### Return type

[**Label**](Label.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_edit_milestone**
> Milestone issue_edit_milestone(owner, repo, id, body=body)

Update a milestone

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | id of the milestone
body = giteapy.EditMilestoneOption() # EditMilestoneOption |  (optional)

try:
    # Update a milestone
    api_response = api_instance.issue_edit_milestone(owner, repo, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_edit_milestone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the milestone |
 **body** | [**EditMilestoneOption**](EditMilestoneOption.md)|  | [optional]

### Return type

[**Milestone**](Milestone.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_get_comments**
> list[Comment] issue_get_comments(owner, repo, index, since=since)

List all comments on an issue

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
index = 789 # int | index of the issue
since = 'since_example' # str | if provided, only comments updated since the specified time are returned. (optional)

try:
    # List all comments on an issue
    api_response = api_instance.issue_get_comments(owner, repo, index, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_get_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **since** | **str**| if provided, only comments updated since the specified time are returned. | [optional]

### Return type

[**list[Comment]**](Comment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_get_issue**
> Issue issue_get_issue(owner, repo, index)

Get an issue

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
index = 789 # int | index of the issue to get

try:
    # Get an issue
    api_response = api_instance.issue_get_issue(owner, repo, index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_get_issue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue to get |

### Return type

[**Issue**](Issue.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_get_label**
> Label issue_get_label(owner, repo, id)

Get a single label

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | id of the label to get

try:
    # Get a single label
    api_response = api_instance.issue_get_label(owner, repo, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_get_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the label to get |

### Return type

[**Label**](Label.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_get_labels**
> list[Label] issue_get_labels(owner, repo, index)

Get an issue's labels

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
index = 789 # int | index of the issue

try:
    # Get an issue's labels
    api_response = api_instance.issue_get_labels(owner, repo, index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_get_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |

### Return type

[**list[Label]**](Label.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_get_milestone**
> Milestone issue_get_milestone(owner, repo, id)

Get a milestone

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | id of the milestone

try:
    # Get a milestone
    api_response = api_instance.issue_get_milestone(owner, repo, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_get_milestone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the milestone |

### Return type

[**Milestone**](Milestone.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_get_milestones_list**
> list[Milestone] issue_get_milestones_list(owner, repo, state=state)

Get all of a repository's opened milestones

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
state = 'state_example' # str | Milestone state, Recognised values are open, closed and all. Defaults to \"open\" (optional)

try:
    # Get all of a repository's opened milestones
    api_response = api_instance.issue_get_milestones_list(owner, repo, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_get_milestones_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **state** | **str**| Milestone state, Recognised values are open, closed and all. Defaults to \&quot;open\&quot; | [optional]

### Return type

[**list[Milestone]**](Milestone.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_get_repo_comments**
> list[Comment] issue_get_repo_comments(owner, repo, since=since)

List all comments in a repository

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
since = 'since_example' # str | if provided, only comments updated since the provided time are returned. (optional)

try:
    # List all comments in a repository
    api_response = api_instance.issue_get_repo_comments(owner, repo, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_get_repo_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **since** | **str**| if provided, only comments updated since the provided time are returned. | [optional]

### Return type

[**list[Comment]**](Comment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_list_issues**
> list[Issue] issue_list_issues(owner, repo, state=state, labels=labels, page=page, q=q)

List a repository's issues

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
state = 'state_example' # str | whether issue is open or closed (optional)
labels = 'labels_example' # str | comma separated list of labels. Fetch only issues that have any of this labels. Non existent labels are discarded (optional)
page = 56 # int | page number of requested issues (optional)
q = 'q_example' # str | search string (optional)

try:
    # List a repository's issues
    api_response = api_instance.issue_list_issues(owner, repo, state=state, labels=labels, page=page, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_list_issues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **state** | **str**| whether issue is open or closed | [optional]
 **labels** | **str**| comma separated list of labels. Fetch only issues that have any of this labels. Non existent labels are discarded | [optional]
 **page** | **int**| page number of requested issues | [optional]
 **q** | **str**| search string | [optional]

### Return type

[**list[Issue]**](Issue.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_list_labels**
> list[Label] issue_list_labels(owner, repo)

Get all of a repository's labels

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo

try:
    # Get all of a repository's labels
    api_response = api_instance.issue_list_labels(owner, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_list_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |

### Return type

[**list[Label]**](Label.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_remove_label**
> issue_remove_label(owner, repo, index, id)

Remove a label from an issue

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
index = 789 # int | index of the issue
id = 789 # int | id of the label to remove

try:
    # Remove a label from an issue
    api_instance.issue_remove_label(owner, repo, index, id)
except ApiException as e:
    print("Exception when calling IssueApi->issue_remove_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **id** | **int**| id of the label to remove |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_replace_labels**
> list[Label] issue_replace_labels(owner, repo, index, body=body)

Replace an issue's labels

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
index = 789 # int | index of the issue
body = giteapy.IssueLabelsOption() # IssueLabelsOption |  (optional)

try:
    # Replace an issue's labels
    api_response = api_instance.issue_replace_labels(owner, repo, index, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_replace_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **body** | [**IssueLabelsOption**](IssueLabelsOption.md)|  | [optional]

### Return type

[**list[Label]**](Label.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_start_stop_watch**
> issue_start_stop_watch(owner, repo, index)

Start stopwatch on an issue.

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
index = 789 # int | index of the issue to create the stopwatch on

try:
    # Start stopwatch on an issue.
    api_instance.issue_start_stop_watch(owner, repo, index)
except ApiException as e:
    print("Exception when calling IssueApi->issue_start_stop_watch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue to create the stopwatch on |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_stop_watch**
> issue_stop_watch(owner, repo, index)

Stop an issue's existing stopwatch.

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
index = 789 # int | index of the issue to stop the stopwatch on

try:
    # Stop an issue's existing stopwatch.
    api_instance.issue_stop_watch(owner, repo, index)
except ApiException as e:
    print("Exception when calling IssueApi->issue_stop_watch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue to stop the stopwatch on |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_tracked_times**
> list[TrackedTime] issue_tracked_times(owner, repo, id)

List an issue's tracked times

### Example
```python
from __future__ import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = giteapy.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = giteapy.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = giteapy.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = giteapy.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = giteapy.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | index of the issue

try:
    # List an issue's tracked times
    api_response = api_instance.issue_tracked_times(owner, repo, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issue_tracked_times: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| index of the issue |

### Return type

[**list[TrackedTime]**](TrackedTime.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

