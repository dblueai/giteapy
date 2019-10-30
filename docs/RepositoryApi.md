# giteapy.RepositoryApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_current_user_repo**](RepositoryApi.md#create_current_user_repo) | **POST** /user/repos | Create a repository
[**create_fork**](RepositoryApi.md#create_fork) | **POST** /repos/{owner}/{repo}/forks | Fork a repository
[**get_blob**](RepositoryApi.md#get_blob) | **GET** /repos/{owner}/{repo}/git/blobs/{sha} | Gets the blob of a repository.
[**get_tag**](RepositoryApi.md#get_tag) | **GET** /repos/{owner}/{repo}/git/tags/{sha} | Gets the tag object of an annotated tag (not lightweight tags)
[**get_tree**](RepositoryApi.md#get_tree) | **GET** /repos/{owner}/{repo}/git/trees/{sha} | Gets the tree of a repository.
[**list_forks**](RepositoryApi.md#list_forks) | **GET** /repos/{owner}/{repo}/forks | List a repository&#39;s forks
[**repo_add_collaborator**](RepositoryApi.md#repo_add_collaborator) | **PUT** /repos/{owner}/{repo}/collaborators/{collaborator} | Add a collaborator to a repository
[**repo_add_topc**](RepositoryApi.md#repo_add_topc) | **PUT** /repos/{owner}/{repo}/topics/{topic} | Add a topic to a repository
[**repo_check_collaborator**](RepositoryApi.md#repo_check_collaborator) | **GET** /repos/{owner}/{repo}/collaborators/{collaborator} | Check if a user is a collaborator of a repository
[**repo_create_file**](RepositoryApi.md#repo_create_file) | **POST** /repos/{owner}/{repo}/contents/{filepath} | Create a file in a repository
[**repo_create_hook**](RepositoryApi.md#repo_create_hook) | **POST** /repos/{owner}/{repo}/hooks | Create a hook
[**repo_create_key**](RepositoryApi.md#repo_create_key) | **POST** /repos/{owner}/{repo}/keys | Add a key to a repository
[**repo_create_pull_request**](RepositoryApi.md#repo_create_pull_request) | **POST** /repos/{owner}/{repo}/pulls | Create a pull request
[**repo_create_release**](RepositoryApi.md#repo_create_release) | **POST** /repos/{owner}/{repo}/releases | Create a release
[**repo_create_release_attachment**](RepositoryApi.md#repo_create_release_attachment) | **POST** /repos/{owner}/{repo}/releases/{id}/assets | Create a release attachment
[**repo_create_status**](RepositoryApi.md#repo_create_status) | **POST** /repos/{owner}/{repo}/statuses/{sha} | Create a commit status
[**repo_delete**](RepositoryApi.md#repo_delete) | **DELETE** /repos/{owner}/{repo} | Delete a repository
[**repo_delete_collaborator**](RepositoryApi.md#repo_delete_collaborator) | **DELETE** /repos/{owner}/{repo}/collaborators/{collaborator} | Delete a collaborator from a repository
[**repo_delete_file**](RepositoryApi.md#repo_delete_file) | **DELETE** /repos/{owner}/{repo}/contents/{filepath} | Delete a file in a repository
[**repo_delete_git_hook**](RepositoryApi.md#repo_delete_git_hook) | **DELETE** /repos/{owner}/{repo}/hooks/git/{id} | Delete a Git hook in a repository
[**repo_delete_hook**](RepositoryApi.md#repo_delete_hook) | **DELETE** /repos/{owner}/{repo}/hooks/{id} | Delete a hook in a repository
[**repo_delete_key**](RepositoryApi.md#repo_delete_key) | **DELETE** /repos/{owner}/{repo}/keys/{id} | Delete a key from a repository
[**repo_delete_release**](RepositoryApi.md#repo_delete_release) | **DELETE** /repos/{owner}/{repo}/releases/{id} | Delete a release
[**repo_delete_release_attachment**](RepositoryApi.md#repo_delete_release_attachment) | **DELETE** /repos/{owner}/{repo}/releases/{id}/assets/{attachment_id} | Delete a release attachment
[**repo_delete_topic**](RepositoryApi.md#repo_delete_topic) | **DELETE** /repos/{owner}/{repo}/topics/{topic} | Delete a topic from a repository
[**repo_edit**](RepositoryApi.md#repo_edit) | **PATCH** /repos/{owner}/{repo} | Edit a repository&#39;s properties. Only fields that are set will be changed.
[**repo_edit_git_hook**](RepositoryApi.md#repo_edit_git_hook) | **PATCH** /repos/{owner}/{repo}/hooks/git/{id} | Edit a Git hook in a repository
[**repo_edit_hook**](RepositoryApi.md#repo_edit_hook) | **PATCH** /repos/{owner}/{repo}/hooks/{id} | Edit a hook in a repository
[**repo_edit_pull_request**](RepositoryApi.md#repo_edit_pull_request) | **PATCH** /repos/{owner}/{repo}/pulls/{index} | Update a pull request
[**repo_edit_release**](RepositoryApi.md#repo_edit_release) | **PATCH** /repos/{owner}/{repo}/releases/{id} | Update a release
[**repo_edit_release_attachment**](RepositoryApi.md#repo_edit_release_attachment) | **PATCH** /repos/{owner}/{repo}/releases/{id}/assets/{attachment_id} | Edit a release attachment
[**repo_get**](RepositoryApi.md#repo_get) | **GET** /repos/{owner}/{repo} | Get a repository
[**repo_get_all_commits**](RepositoryApi.md#repo_get_all_commits) | **GET** /repos/{owner}/{repo}/commits | Get a list of all commits from a repository
[**repo_get_archive**](RepositoryApi.md#repo_get_archive) | **GET** /repos/{owner}/{repo}/archive/{archive} | Get an archive of a repository
[**repo_get_branch**](RepositoryApi.md#repo_get_branch) | **GET** /repos/{owner}/{repo}/branches/{branch} | Retrieve a specific branch from a repository
[**repo_get_by_id**](RepositoryApi.md#repo_get_by_id) | **GET** /repositories/{id} | Get a repository by id
[**repo_get_combined_status_by_ref**](RepositoryApi.md#repo_get_combined_status_by_ref) | **GET** /repos/{owner}/{repo}/commits/{ref}/statuses | Get a commit&#39;s combined status, by branch/tag/commit reference
[**repo_get_contents**](RepositoryApi.md#repo_get_contents) | **GET** /repos/{owner}/{repo}/contents/{filepath} | Gets the metadata and contents (if a file) of an entry in a repository, or a list of entries if a dir
[**repo_get_contents_list**](RepositoryApi.md#repo_get_contents_list) | **GET** /repos/{owner}/{repo}/contents | Gets the metadata of all the entries of the root dir
[**repo_get_editor_config**](RepositoryApi.md#repo_get_editor_config) | **GET** /repos/{owner}/{repo}/editorconfig/{filepath} | Get the EditorConfig definitions of a file in a repository
[**repo_get_git_hook**](RepositoryApi.md#repo_get_git_hook) | **GET** /repos/{owner}/{repo}/hooks/git/{id} | Get a Git hook
[**repo_get_hook**](RepositoryApi.md#repo_get_hook) | **GET** /repos/{owner}/{repo}/hooks/{id} | Get a hook
[**repo_get_key**](RepositoryApi.md#repo_get_key) | **GET** /repos/{owner}/{repo}/keys/{id} | Get a repository&#39;s key by id
[**repo_get_pull_request**](RepositoryApi.md#repo_get_pull_request) | **GET** /repos/{owner}/{repo}/pulls/{index} | Get a pull request
[**repo_get_raw_file**](RepositoryApi.md#repo_get_raw_file) | **GET** /repos/{owner}/{repo}/raw/{filepath} | Get a file from a repository
[**repo_get_release**](RepositoryApi.md#repo_get_release) | **GET** /repos/{owner}/{repo}/releases/{id} | Get a release
[**repo_get_release_attachment**](RepositoryApi.md#repo_get_release_attachment) | **GET** /repos/{owner}/{repo}/releases/{id}/assets/{attachment_id} | Get a release attachment
[**repo_get_single_commit**](RepositoryApi.md#repo_get_single_commit) | **GET** /repos/{owner}/{repo}/git/commits/{sha} | Get a single commit from a repository
[**repo_list_all_git_refs**](RepositoryApi.md#repo_list_all_git_refs) | **GET** /repos/{owner}/{repo}/git/refs | Get specified ref or filtered repository&#39;s refs
[**repo_list_branches**](RepositoryApi.md#repo_list_branches) | **GET** /repos/{owner}/{repo}/branches | List a repository&#39;s branches
[**repo_list_collaborators**](RepositoryApi.md#repo_list_collaborators) | **GET** /repos/{owner}/{repo}/collaborators | List a repository&#39;s collaborators
[**repo_list_git_hooks**](RepositoryApi.md#repo_list_git_hooks) | **GET** /repos/{owner}/{repo}/hooks/git | List the Git hooks in a repository
[**repo_list_git_refs**](RepositoryApi.md#repo_list_git_refs) | **GET** /repos/{owner}/{repo}/git/refs/{ref} | Get specified ref or filtered repository&#39;s refs
[**repo_list_hooks**](RepositoryApi.md#repo_list_hooks) | **GET** /repos/{owner}/{repo}/hooks | List the hooks in a repository
[**repo_list_keys**](RepositoryApi.md#repo_list_keys) | **GET** /repos/{owner}/{repo}/keys | List a repository&#39;s keys
[**repo_list_pull_requests**](RepositoryApi.md#repo_list_pull_requests) | **GET** /repos/{owner}/{repo}/pulls | List a repo&#39;s pull requests
[**repo_list_release_attachments**](RepositoryApi.md#repo_list_release_attachments) | **GET** /repos/{owner}/{repo}/releases/{id}/assets | List release&#39;s attachments
[**repo_list_releases**](RepositoryApi.md#repo_list_releases) | **GET** /repos/{owner}/{repo}/releases | List a repo&#39;s releases
[**repo_list_stargazers**](RepositoryApi.md#repo_list_stargazers) | **GET** /repos/{owner}/{repo}/stargazers | List a repo&#39;s stargazers
[**repo_list_statuses**](RepositoryApi.md#repo_list_statuses) | **GET** /repos/{owner}/{repo}/statuses/{sha} | Get a commit&#39;s statuses
[**repo_list_subscribers**](RepositoryApi.md#repo_list_subscribers) | **GET** /repos/{owner}/{repo}/subscribers | List a repo&#39;s watchers
[**repo_list_tags**](RepositoryApi.md#repo_list_tags) | **GET** /repos/{owner}/{repo}/tags | List a repository&#39;s tags
[**repo_list_topics**](RepositoryApi.md#repo_list_topics) | **GET** /repos/{owner}/{repo}/topics | Get list of topics that a repository has
[**repo_merge_pull_request**](RepositoryApi.md#repo_merge_pull_request) | **POST** /repos/{owner}/{repo}/pulls/{index}/merge | Merge a pull request
[**repo_migrate**](RepositoryApi.md#repo_migrate) | **POST** /repos/migrate | Migrate a remote git repository
[**repo_mirror_sync**](RepositoryApi.md#repo_mirror_sync) | **POST** /repos/{owner}/{repo}/mirror-sync | Sync a mirrored repository
[**repo_pull_request_is_merged**](RepositoryApi.md#repo_pull_request_is_merged) | **GET** /repos/{owner}/{repo}/pulls/{index}/merge | Check if a pull request has been merged
[**repo_search**](RepositoryApi.md#repo_search) | **GET** /repos/search | Search for repositories
[**repo_signing_key**](RepositoryApi.md#repo_signing_key) | **GET** /repos/{owner}/{repo}/signing-key.gpg | Get signing-key.gpg for given repository
[**repo_test_hook**](RepositoryApi.md#repo_test_hook) | **POST** /repos/{owner}/{repo}/hooks/{id}/tests | Test a push webhook
[**repo_tracked_times**](RepositoryApi.md#repo_tracked_times) | **GET** /repos/{owner}/{repo}/times | List a repo&#39;s tracked times
[**repo_update_file**](RepositoryApi.md#repo_update_file) | **PUT** /repos/{owner}/{repo}/contents/{filepath} | Update a file in a repository
[**repo_update_topics**](RepositoryApi.md#repo_update_topics) | **PUT** /repos/{owner}/{repo}/topics | Replace list of topics for a repository
[**topic_search**](RepositoryApi.md#topic_search) | **GET** /topics/search | search topics via keyword
[**user_current_check_subscription**](RepositoryApi.md#user_current_check_subscription) | **GET** /repos/{owner}/{repo}/subscription | Check if the current user is watching a repo
[**user_current_delete_subscription**](RepositoryApi.md#user_current_delete_subscription) | **DELETE** /repos/{owner}/{repo}/subscription | Unwatch a repo
[**user_current_put_subscription**](RepositoryApi.md#user_current_put_subscription) | **PUT** /repos/{owner}/{repo}/subscription | Watch a repo


# **create_current_user_repo**
> Repository create_current_user_repo(body=body)

Create a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
body = giteapy.CreateRepoOption() # CreateRepoOption |  (optional)

try:
    # Create a repository
    api_response = api_instance.create_current_user_repo(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->create_current_user_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRepoOption**](CreateRepoOption.md)|  | [optional] 

### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fork**
> Repository create_fork(owner, repo, body=body)

Fork a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo to fork
repo = 'repo_example' # str | name of the repo to fork
body = giteapy.CreateForkOption() # CreateForkOption |  (optional)

try:
    # Fork a repository
    api_response = api_instance.create_fork(owner, repo, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->create_fork: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo to fork | 
 **repo** | **str**| name of the repo to fork | 
 **body** | [**CreateForkOption**](CreateForkOption.md)|  | [optional] 

### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blob**
> GitBlobResponse get_blob(owner, repo, sha)

Gets the blob of a repository.

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
sha = 'sha_example' # str | sha of the commit

try:
    # Gets the blob of a repository.
    api_response = api_instance.get_blob(owner, repo, sha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->get_blob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **sha** | **str**| sha of the commit | 

### Return type

[**GitBlobResponse**](GitBlobResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag**
> AnnotatedTag get_tag(owner, repo, sha)

Gets the tag object of an annotated tag (not lightweight tags)

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
sha = 'sha_example' # str | sha of the tag. The Git tags API only supports annotated tag objects, not lightweight tags.

try:
    # Gets the tag object of an annotated tag (not lightweight tags)
    api_response = api_instance.get_tag(owner, repo, sha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->get_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **sha** | **str**| sha of the tag. The Git tags API only supports annotated tag objects, not lightweight tags. | 

### Return type

[**AnnotatedTag**](AnnotatedTag.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tree**
> GitTreeResponse get_tree(owner, repo, sha, recursive=recursive, page=page, per_page=per_page)

Gets the tree of a repository.

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
sha = 'sha_example' # str | sha of the commit
recursive = true # bool | show all directories and files (optional)
page = 56 # int | page number; the 'truncated' field in the response will be true if there are still more items after this page, false if the last page (optional)
per_page = 56 # int | number of items per page; default is 1000 or what is set in app.ini as DEFAULT_GIT_TREES_PER_PAGE (optional)

try:
    # Gets the tree of a repository.
    api_response = api_instance.get_tree(owner, repo, sha, recursive=recursive, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->get_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **sha** | **str**| sha of the commit | 
 **recursive** | **bool**| show all directories and files | [optional] 
 **page** | **int**| page number; the &#39;truncated&#39; field in the response will be true if there are still more items after this page, false if the last page | [optional] 
 **per_page** | **int**| number of items per page; default is 1000 or what is set in app.ini as DEFAULT_GIT_TREES_PER_PAGE | [optional] 

### Return type

[**GitTreeResponse**](GitTreeResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_forks**
> list[Repository] list_forks(owner, repo)

List a repository's forks

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo

try:
    # List a repository's forks
    api_response = api_instance.list_forks(owner, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->list_forks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**list[Repository]**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_add_collaborator**
> repo_add_collaborator(owner, repo, collaborator, body=body)

Add a collaborator to a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
collaborator = 'collaborator_example' # str | username of the collaborator to add
body = giteapy.AddCollaboratorOption() # AddCollaboratorOption |  (optional)

try:
    # Add a collaborator to a repository
    api_instance.repo_add_collaborator(owner, repo, collaborator, body=body)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_add_collaborator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **collaborator** | **str**| username of the collaborator to add | 
 **body** | [**AddCollaboratorOption**](AddCollaboratorOption.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_add_topc**
> repo_add_topc(owner, repo, topic)

Add a topic to a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
topic = 'topic_example' # str | name of the topic to add

try:
    # Add a topic to a repository
    api_instance.repo_add_topc(owner, repo, topic)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_add_topc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **topic** | **str**| name of the topic to add | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_check_collaborator**
> repo_check_collaborator(owner, repo, collaborator)

Check if a user is a collaborator of a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
collaborator = 'collaborator_example' # str | username of the collaborator

try:
    # Check if a user is a collaborator of a repository
    api_instance.repo_check_collaborator(owner, repo, collaborator)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_check_collaborator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **collaborator** | **str**| username of the collaborator | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_file**
> FileResponse repo_create_file(owner, repo, filepath, body)

Create a file in a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
filepath = 'filepath_example' # str | path of the file to create
body = giteapy.CreateFileOptions() # CreateFileOptions | 

try:
    # Create a file in a repository
    api_response = api_instance.repo_create_file(owner, repo, filepath, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_create_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **filepath** | **str**| path of the file to create | 
 **body** | [**CreateFileOptions**](CreateFileOptions.md)|  | 

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_hook**
> Hook repo_create_hook(owner, repo, body=body)

Create a hook

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
body = giteapy.CreateHookOption() # CreateHookOption |  (optional)

try:
    # Create a hook
    api_response = api_instance.repo_create_hook(owner, repo, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_create_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**CreateHookOption**](CreateHookOption.md)|  | [optional] 

### Return type

[**Hook**](Hook.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_key**
> DeployKey repo_create_key(owner, repo, body=body)

Add a key to a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
body = giteapy.CreateKeyOption() # CreateKeyOption |  (optional)

try:
    # Add a key to a repository
    api_response = api_instance.repo_create_key(owner, repo, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_create_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**CreateKeyOption**](CreateKeyOption.md)|  | [optional] 

### Return type

[**DeployKey**](DeployKey.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_pull_request**
> PullRequest repo_create_pull_request(owner, repo, body=body)

Create a pull request

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
body = giteapy.CreatePullRequestOption() # CreatePullRequestOption |  (optional)

try:
    # Create a pull request
    api_response = api_instance.repo_create_pull_request(owner, repo, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_create_pull_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**CreatePullRequestOption**](CreatePullRequestOption.md)|  | [optional] 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_release**
> Release repo_create_release(owner, repo, body=body)

Create a release

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
body = giteapy.CreateReleaseOption() # CreateReleaseOption |  (optional)

try:
    # Create a release
    api_response = api_instance.repo_create_release(owner, repo, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_create_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**CreateReleaseOption**](CreateReleaseOption.md)|  | [optional] 

### Return type

[**Release**](Release.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_release_attachment**
> Attachment repo_create_release_attachment(owner, repo, id, attachment, name=name)

Create a release attachment

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | id of the release
attachment = '/path/to/file.txt' # file | attachment to upload
name = 'name_example' # str | name of the attachment (optional)

try:
    # Create a release attachment
    api_response = api_instance.repo_create_release_attachment(owner, repo, id, attachment, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_create_release_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the release | 
 **attachment** | **file**| attachment to upload | 
 **name** | **str**| name of the attachment | [optional] 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_status**
> list[Status] repo_create_status(owner, repo, sha, body=body)

Create a commit status

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
sha = 'sha_example' # str | sha of the commit
body = giteapy.CreateStatusOption() # CreateStatusOption |  (optional)

try:
    # Create a commit status
    api_response = api_instance.repo_create_status(owner, repo, sha, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_create_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **sha** | **str**| sha of the commit | 
 **body** | [**CreateStatusOption**](CreateStatusOption.md)|  | [optional] 

### Return type

[**list[Status]**](Status.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete**
> repo_delete(owner, repo)

Delete a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo to delete
repo = 'repo_example' # str | name of the repo to delete

try:
    # Delete a repository
    api_instance.repo_delete(owner, repo)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo to delete | 
 **repo** | **str**| name of the repo to delete | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_collaborator**
> repo_delete_collaborator(owner, repo, collaborator)

Delete a collaborator from a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
collaborator = 'collaborator_example' # str | username of the collaborator to delete

try:
    # Delete a collaborator from a repository
    api_instance.repo_delete_collaborator(owner, repo, collaborator)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_delete_collaborator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **collaborator** | **str**| username of the collaborator to delete | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_file**
> FileDeleteResponse repo_delete_file(owner, repo, filepath, body)

Delete a file in a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
filepath = 'filepath_example' # str | path of the file to delete
body = giteapy.DeleteFileOptions() # DeleteFileOptions | 

try:
    # Delete a file in a repository
    api_response = api_instance.repo_delete_file(owner, repo, filepath, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **filepath** | **str**| path of the file to delete | 
 **body** | [**DeleteFileOptions**](DeleteFileOptions.md)|  | 

### Return type

[**FileDeleteResponse**](FileDeleteResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_git_hook**
> repo_delete_git_hook(owner, repo, id)

Delete a Git hook in a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 'id_example' # str | id of the hook to get

try:
    # Delete a Git hook in a repository
    api_instance.repo_delete_git_hook(owner, repo, id)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_delete_git_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **str**| id of the hook to get | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_hook**
> repo_delete_hook(owner, repo, id)

Delete a hook in a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | id of the hook to delete

try:
    # Delete a hook in a repository
    api_instance.repo_delete_hook(owner, repo, id)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_delete_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the hook to delete | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_key**
> repo_delete_key(owner, repo, id)

Delete a key from a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | id of the key to delete

try:
    # Delete a key from a repository
    api_instance.repo_delete_key(owner, repo, id)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_delete_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the key to delete | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_release**
> repo_delete_release(owner, repo, id)

Delete a release

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | id of the release to delete

try:
    # Delete a release
    api_instance.repo_delete_release(owner, repo, id)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_delete_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the release to delete | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_release_attachment**
> repo_delete_release_attachment(owner, repo, id, attachment_id)

Delete a release attachment

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | id of the release
attachment_id = 789 # int | id of the attachment to delete

try:
    # Delete a release attachment
    api_instance.repo_delete_release_attachment(owner, repo, id, attachment_id)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_delete_release_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the release | 
 **attachment_id** | **int**| id of the attachment to delete | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_topic**
> repo_delete_topic(owner, repo, topic)

Delete a topic from a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
topic = 'topic_example' # str | name of the topic to delete

try:
    # Delete a topic from a repository
    api_instance.repo_delete_topic(owner, repo, topic)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_delete_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **topic** | **str**| name of the topic to delete | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit**
> Repository repo_edit(owner, repo, body=body)

Edit a repository's properties. Only fields that are set will be changed.

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo to edit
repo = 'repo_example' # str | name of the repo to edit
body = giteapy.EditRepoOption() # EditRepoOption | Properties of a repo that you can edit (optional)

try:
    # Edit a repository's properties. Only fields that are set will be changed.
    api_response = api_instance.repo_edit(owner, repo, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo to edit | 
 **repo** | **str**| name of the repo to edit | 
 **body** | [**EditRepoOption**](EditRepoOption.md)| Properties of a repo that you can edit | [optional] 

### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit_git_hook**
> GitHook repo_edit_git_hook(owner, repo, id, body=body)

Edit a Git hook in a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 'id_example' # str | id of the hook to get
body = giteapy.EditGitHookOption() # EditGitHookOption |  (optional)

try:
    # Edit a Git hook in a repository
    api_response = api_instance.repo_edit_git_hook(owner, repo, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_edit_git_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **str**| id of the hook to get | 
 **body** | [**EditGitHookOption**](EditGitHookOption.md)|  | [optional] 

### Return type

[**GitHook**](GitHook.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit_hook**
> Hook repo_edit_hook(owner, repo, id, body=body)

Edit a hook in a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | index of the hook
body = giteapy.EditHookOption() # EditHookOption |  (optional)

try:
    # Edit a hook in a repository
    api_response = api_instance.repo_edit_hook(owner, repo, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_edit_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| index of the hook | 
 **body** | [**EditHookOption**](EditHookOption.md)|  | [optional] 

### Return type

[**Hook**](Hook.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit_pull_request**
> PullRequest repo_edit_pull_request(owner, repo, index, body=body)

Update a pull request

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
index = 789 # int | index of the pull request to edit
body = giteapy.EditPullRequestOption() # EditPullRequestOption |  (optional)

try:
    # Update a pull request
    api_response = api_instance.repo_edit_pull_request(owner, repo, index, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_edit_pull_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request to edit | 
 **body** | [**EditPullRequestOption**](EditPullRequestOption.md)|  | [optional] 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit_release**
> Release repo_edit_release(owner, repo, id, body=body)

Update a release

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | id of the release to edit
body = giteapy.EditReleaseOption() # EditReleaseOption |  (optional)

try:
    # Update a release
    api_response = api_instance.repo_edit_release(owner, repo, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_edit_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the release to edit | 
 **body** | [**EditReleaseOption**](EditReleaseOption.md)|  | [optional] 

### Return type

[**Release**](Release.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit_release_attachment**
> Attachment repo_edit_release_attachment(owner, repo, id, attachment_id, body=body)

Edit a release attachment

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | id of the release
attachment_id = 789 # int | id of the attachment to edit
body = giteapy.EditAttachmentOptions() # EditAttachmentOptions |  (optional)

try:
    # Edit a release attachment
    api_response = api_instance.repo_edit_release_attachment(owner, repo, id, attachment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_edit_release_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the release | 
 **attachment_id** | **int**| id of the attachment to edit | 
 **body** | [**EditAttachmentOptions**](EditAttachmentOptions.md)|  | [optional] 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get**
> Repository repo_get(owner, repo)

Get a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo

try:
    # Get a repository
    api_response = api_instance.repo_get(owner, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_all_commits**
> list[Commit] repo_get_all_commits(owner, repo, sha=sha, page=page)

Get a list of all commits from a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
sha = 'sha_example' # str | SHA or branch to start listing commits from (usually 'master') (optional)
page = 56 # int | page number of requested commits (optional)

try:
    # Get a list of all commits from a repository
    api_response = api_instance.repo_get_all_commits(owner, repo, sha=sha, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_get_all_commits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **sha** | **str**| SHA or branch to start listing commits from (usually &#39;master&#39;) | [optional] 
 **page** | **int**| page number of requested commits | [optional] 

### Return type

[**list[Commit]**](Commit.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_archive**
> repo_get_archive(owner, repo, archive)

Get an archive of a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
archive = 'archive_example' # str | archive to download, consisting of a git reference and archive

try:
    # Get an archive of a repository
    api_instance.repo_get_archive(owner, repo, archive)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_get_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **archive** | **str**| archive to download, consisting of a git reference and archive | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_branch**
> Branch repo_get_branch(owner, repo, branch)

Retrieve a specific branch from a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
branch = 'branch_example' # str | branch to get

try:
    # Retrieve a specific branch from a repository
    api_response = api_instance.repo_get_branch(owner, repo, branch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_get_branch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **branch** | **str**| branch to get | 

### Return type

[**Branch**](Branch.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_by_id**
> Repository repo_get_by_id(id)

Get a repository by id

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
id = 789 # int | id of the repo to get

try:
    # Get a repository by id
    api_response = api_instance.repo_get_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the repo to get | 

### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_combined_status_by_ref**
> Status repo_get_combined_status_by_ref(owner, repo, ref, page=page)

Get a commit's combined status, by branch/tag/commit reference

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
ref = 'ref_example' # str | name of branch/tag/commit
page = 56 # int | page number of results (optional)

try:
    # Get a commit's combined status, by branch/tag/commit reference
    api_response = api_instance.repo_get_combined_status_by_ref(owner, repo, ref, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_get_combined_status_by_ref: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **ref** | **str**| name of branch/tag/commit | 
 **page** | **int**| page number of results | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_contents**
> ContentsResponse repo_get_contents(owner, repo, filepath, ref=ref)

Gets the metadata and contents (if a file) of an entry in a repository, or a list of entries if a dir

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
filepath = 'filepath_example' # str | path of the dir, file, symlink or submodule in the repo
ref = 'ref_example' # str | The name of the commit/branch/tag. Default the repository’s default branch (usually master) (optional)

try:
    # Gets the metadata and contents (if a file) of an entry in a repository, or a list of entries if a dir
    api_response = api_instance.repo_get_contents(owner, repo, filepath, ref=ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_get_contents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **filepath** | **str**| path of the dir, file, symlink or submodule in the repo | 
 **ref** | **str**| The name of the commit/branch/tag. Default the repository’s default branch (usually master) | [optional] 

### Return type

[**ContentsResponse**](ContentsResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_contents_list**
> list[ContentsResponse] repo_get_contents_list(owner, repo, ref=ref)

Gets the metadata of all the entries of the root dir

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
ref = 'ref_example' # str | The name of the commit/branch/tag. Default the repository’s default branch (usually master) (optional)

try:
    # Gets the metadata of all the entries of the root dir
    api_response = api_instance.repo_get_contents_list(owner, repo, ref=ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_get_contents_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **ref** | **str**| The name of the commit/branch/tag. Default the repository’s default branch (usually master) | [optional] 

### Return type

[**list[ContentsResponse]**](ContentsResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_editor_config**
> repo_get_editor_config(owner, repo, filepath)

Get the EditorConfig definitions of a file in a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
filepath = 'filepath_example' # str | filepath of file to get

try:
    # Get the EditorConfig definitions of a file in a repository
    api_instance.repo_get_editor_config(owner, repo, filepath)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_get_editor_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **filepath** | **str**| filepath of file to get | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_git_hook**
> GitHook repo_get_git_hook(owner, repo, id)

Get a Git hook

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 'id_example' # str | id of the hook to get

try:
    # Get a Git hook
    api_response = api_instance.repo_get_git_hook(owner, repo, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_get_git_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **str**| id of the hook to get | 

### Return type

[**GitHook**](GitHook.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_hook**
> Hook repo_get_hook(owner, repo, id)

Get a hook

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | id of the hook to get

try:
    # Get a hook
    api_response = api_instance.repo_get_hook(owner, repo, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_get_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the hook to get | 

### Return type

[**Hook**](Hook.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_key**
> DeployKey repo_get_key(owner, repo, id)

Get a repository's key by id

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | id of the key to get

try:
    # Get a repository's key by id
    api_response = api_instance.repo_get_key(owner, repo, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_get_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the key to get | 

### Return type

[**DeployKey**](DeployKey.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_pull_request**
> PullRequest repo_get_pull_request(owner, repo, index)

Get a pull request

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
index = 789 # int | index of the pull request to get

try:
    # Get a pull request
    api_response = api_instance.repo_get_pull_request(owner, repo, index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_get_pull_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request to get | 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_raw_file**
> repo_get_raw_file(owner, repo, filepath)

Get a file from a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
filepath = 'filepath_example' # str | filepath of the file to get

try:
    # Get a file from a repository
    api_instance.repo_get_raw_file(owner, repo, filepath)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_get_raw_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **filepath** | **str**| filepath of the file to get | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_release**
> Release repo_get_release(owner, repo, id)

Get a release

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | id of the release to get

try:
    # Get a release
    api_response = api_instance.repo_get_release(owner, repo, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_get_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the release to get | 

### Return type

[**Release**](Release.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_release_attachment**
> Attachment repo_get_release_attachment(owner, repo, id, attachment_id)

Get a release attachment

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | id of the release
attachment_id = 789 # int | id of the attachment to get

try:
    # Get a release attachment
    api_response = api_instance.repo_get_release_attachment(owner, repo, id, attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_get_release_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the release | 
 **attachment_id** | **int**| id of the attachment to get | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_single_commit**
> Commit repo_get_single_commit(owner, repo, sha)

Get a single commit from a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
sha = 'sha_example' # str | the commit hash

try:
    # Get a single commit from a repository
    api_response = api_instance.repo_get_single_commit(owner, repo, sha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_get_single_commit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **sha** | **str**| the commit hash | 

### Return type

[**Commit**](Commit.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_all_git_refs**
> list[Reference] repo_list_all_git_refs(owner, repo)

Get specified ref or filtered repository's refs

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo

try:
    # Get specified ref or filtered repository's refs
    api_response = api_instance.repo_list_all_git_refs(owner, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_list_all_git_refs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**list[Reference]**](Reference.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_branches**
> list[Branch] repo_list_branches(owner, repo)

List a repository's branches

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo

try:
    # List a repository's branches
    api_response = api_instance.repo_list_branches(owner, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_list_branches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**list[Branch]**](Branch.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_collaborators**
> list[User] repo_list_collaborators(owner, repo)

List a repository's collaborators

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo

try:
    # List a repository's collaborators
    api_response = api_instance.repo_list_collaborators(owner, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_list_collaborators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**list[User]**](User.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_git_hooks**
> list[GitHook] repo_list_git_hooks(owner, repo)

List the Git hooks in a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo

try:
    # List the Git hooks in a repository
    api_response = api_instance.repo_list_git_hooks(owner, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_list_git_hooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**list[GitHook]**](GitHook.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_git_refs**
> list[Reference] repo_list_git_refs(owner, repo, ref)

Get specified ref or filtered repository's refs

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
ref = 'ref_example' # str | part or full name of the ref

try:
    # Get specified ref or filtered repository's refs
    api_response = api_instance.repo_list_git_refs(owner, repo, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_list_git_refs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **ref** | **str**| part or full name of the ref | 

### Return type

[**list[Reference]**](Reference.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_hooks**
> list[Hook] repo_list_hooks(owner, repo)

List the hooks in a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo

try:
    # List the hooks in a repository
    api_response = api_instance.repo_list_hooks(owner, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_list_hooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**list[Hook]**](Hook.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_keys**
> list[DeployKey] repo_list_keys(owner, repo, key_id=key_id, fingerprint=fingerprint)

List a repository's keys

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
key_id = 56 # int | the key_id to search for (optional)
fingerprint = 'fingerprint_example' # str | fingerprint of the key (optional)

try:
    # List a repository's keys
    api_response = api_instance.repo_list_keys(owner, repo, key_id=key_id, fingerprint=fingerprint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_list_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **key_id** | **int**| the key_id to search for | [optional] 
 **fingerprint** | **str**| fingerprint of the key | [optional] 

### Return type

[**list[DeployKey]**](DeployKey.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_pull_requests**
> list[PullRequest] repo_list_pull_requests(owner, repo, page=page, state=state, sort=sort, milestone=milestone, labels=labels)

List a repo's pull requests

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
page = 56 # int | Page number (optional)
state = 'state_example' # str | State of pull request: open or closed (optional) (optional)
sort = 'sort_example' # str | Type of sort (optional)
milestone = 789 # int | ID of the milestone (optional)
labels = [56] # list[int] | Label IDs (optional)

try:
    # List a repo's pull requests
    api_response = api_instance.repo_list_pull_requests(owner, repo, page=page, state=state, sort=sort, milestone=milestone, labels=labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_list_pull_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **page** | **int**| Page number | [optional] 
 **state** | **str**| State of pull request: open or closed (optional) | [optional] 
 **sort** | **str**| Type of sort | [optional] 
 **milestone** | **int**| ID of the milestone | [optional] 
 **labels** | [**list[int]**](int.md)| Label IDs | [optional] 

### Return type

[**list[PullRequest]**](PullRequest.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_release_attachments**
> list[Attachment] repo_list_release_attachments(owner, repo, id)

List release's attachments

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | id of the release

try:
    # List release's attachments
    api_response = api_instance.repo_list_release_attachments(owner, repo, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_list_release_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the release | 

### Return type

[**list[Attachment]**](Attachment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_releases**
> list[Release] repo_list_releases(owner, repo, page=page, per_page=per_page)

List a repo's releases

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
page = 56 # int | page wants to load (optional)
per_page = 56 # int | items count every page wants to load (optional)

try:
    # List a repo's releases
    api_response = api_instance.repo_list_releases(owner, repo, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_list_releases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **page** | **int**| page wants to load | [optional] 
 **per_page** | **int**| items count every page wants to load | [optional] 

### Return type

[**list[Release]**](Release.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_stargazers**
> list[User] repo_list_stargazers(owner, repo)

List a repo's stargazers

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo

try:
    # List a repo's stargazers
    api_response = api_instance.repo_list_stargazers(owner, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_list_stargazers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**list[User]**](User.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_statuses**
> list[Status] repo_list_statuses(owner, repo, sha, page=page, sort=sort, state=state)

Get a commit's statuses

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
sha = 'sha_example' # str | sha of the commit
page = 56 # int | page number of results (optional)
sort = 'sort_example' # str | type of sort (optional)
state = 'state_example' # str | type of state (optional)

try:
    # Get a commit's statuses
    api_response = api_instance.repo_list_statuses(owner, repo, sha, page=page, sort=sort, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_list_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **sha** | **str**| sha of the commit | 
 **page** | **int**| page number of results | [optional] 
 **sort** | **str**| type of sort | [optional] 
 **state** | **str**| type of state | [optional] 

### Return type

[**list[Status]**](Status.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_subscribers**
> list[User] repo_list_subscribers(owner, repo)

List a repo's watchers

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo

try:
    # List a repo's watchers
    api_response = api_instance.repo_list_subscribers(owner, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_list_subscribers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**list[User]**](User.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_tags**
> list[Tag] repo_list_tags(owner, repo)

List a repository's tags

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo

try:
    # List a repository's tags
    api_response = api_instance.repo_list_tags(owner, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_list_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**list[Tag]**](Tag.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_topics**
> TopicName repo_list_topics(owner, repo)

Get list of topics that a repository has

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo

try:
    # Get list of topics that a repository has
    api_response = api_instance.repo_list_topics(owner, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_list_topics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**TopicName**](TopicName.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_merge_pull_request**
> repo_merge_pull_request(owner, repo, index, body=body)

Merge a pull request

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
index = 789 # int | index of the pull request to merge
body = giteapy.MergePullRequestOption() # MergePullRequestOption |  (optional)

try:
    # Merge a pull request
    api_instance.repo_merge_pull_request(owner, repo, index, body=body)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_merge_pull_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request to merge | 
 **body** | [**MergePullRequestOption**](MergePullRequestOption.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_migrate**
> Repository repo_migrate(body=body)

Migrate a remote git repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
body = giteapy.MigrateRepoForm() # MigrateRepoForm |  (optional)

try:
    # Migrate a remote git repository
    api_response = api_instance.repo_migrate(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_migrate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MigrateRepoForm**](MigrateRepoForm.md)|  | [optional] 

### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_mirror_sync**
> repo_mirror_sync(owner, repo)

Sync a mirrored repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo to sync
repo = 'repo_example' # str | name of the repo to sync

try:
    # Sync a mirrored repository
    api_instance.repo_mirror_sync(owner, repo)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_mirror_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo to sync | 
 **repo** | **str**| name of the repo to sync | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_pull_request_is_merged**
> repo_pull_request_is_merged(owner, repo, index)

Check if a pull request has been merged

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
index = 789 # int | index of the pull request

try:
    # Check if a pull request has been merged
    api_instance.repo_pull_request_is_merged(owner, repo, index)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_pull_request_is_merged: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_search**
> SearchResults repo_search(q=q, topic=topic, include_desc=include_desc, uid=uid, starred_by=starred_by, private=private, page=page, limit=limit, mode=mode, exclusive=exclusive, sort=sort, order=order)

Search for repositories

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
q = 'q_example' # str | keyword (optional)
topic = true # bool | Limit search to repositories with keyword as topic (optional)
include_desc = true # bool | include search of keyword within repository description (optional)
uid = 789 # int | search only for repos that the user with the given id owns or contributes to (optional)
starred_by = 789 # int | search only for repos that the user with the given id has starred (optional)
private = true # bool | include private repositories this user has access to (defaults to true) (optional)
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results, maximum page size is 50 (optional)
mode = 'mode_example' # str | type of repository to search for. Supported values are \"fork\", \"source\", \"mirror\" and \"collaborative\" (optional)
exclusive = true # bool | if `uid` is given, search only for repos that the user owns (optional)
sort = 'sort_example' # str | sort repos by attribute. Supported values are \"alpha\", \"created\", \"updated\", \"size\", and \"id\". Default is \"alpha\" (optional)
order = 'order_example' # str | sort order, either \"asc\" (ascending) or \"desc\" (descending). Default is \"asc\", ignored if \"sort\" is not specified. (optional)

try:
    # Search for repositories
    api_response = api_instance.repo_search(q=q, topic=topic, include_desc=include_desc, uid=uid, starred_by=starred_by, private=private, page=page, limit=limit, mode=mode, exclusive=exclusive, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| keyword | [optional] 
 **topic** | **bool**| Limit search to repositories with keyword as topic | [optional] 
 **include_desc** | **bool**| include search of keyword within repository description | [optional] 
 **uid** | **int**| search only for repos that the user with the given id owns or contributes to | [optional] 
 **starred_by** | **int**| search only for repos that the user with the given id has starred | [optional] 
 **private** | **bool**| include private repositories this user has access to (defaults to true) | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results, maximum page size is 50 | [optional] 
 **mode** | **str**| type of repository to search for. Supported values are \&quot;fork\&quot;, \&quot;source\&quot;, \&quot;mirror\&quot; and \&quot;collaborative\&quot; | [optional] 
 **exclusive** | **bool**| if &#x60;uid&#x60; is given, search only for repos that the user owns | [optional] 
 **sort** | **str**| sort repos by attribute. Supported values are \&quot;alpha\&quot;, \&quot;created\&quot;, \&quot;updated\&quot;, \&quot;size\&quot;, and \&quot;id\&quot;. Default is \&quot;alpha\&quot; | [optional] 
 **order** | **str**| sort order, either \&quot;asc\&quot; (ascending) or \&quot;desc\&quot; (descending). Default is \&quot;asc\&quot;, ignored if \&quot;sort\&quot; is not specified. | [optional] 

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_signing_key**
> str repo_signing_key(owner, repo)

Get signing-key.gpg for given repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo

try:
    # Get signing-key.gpg for given repository
    api_response = api_instance.repo_signing_key(owner, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_signing_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

**str**

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_test_hook**
> repo_test_hook(owner, repo, id)

Test a push webhook

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
id = 789 # int | id of the hook to test

try:
    # Test a push webhook
    api_instance.repo_test_hook(owner, repo, id)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_test_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the hook to test | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_tracked_times**
> list[TrackedTime] repo_tracked_times(owner, repo)

List a repo's tracked times

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo

try:
    # List a repo's tracked times
    api_response = api_instance.repo_tracked_times(owner, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_tracked_times: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**list[TrackedTime]**](TrackedTime.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_update_file**
> FileResponse repo_update_file(owner, repo, filepath, body)

Update a file in a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
filepath = 'filepath_example' # str | path of the file to update
body = giteapy.UpdateFileOptions() # UpdateFileOptions | 

try:
    # Update a file in a repository
    api_response = api_instance.repo_update_file(owner, repo, filepath, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_update_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **filepath** | **str**| path of the file to update | 
 **body** | [**UpdateFileOptions**](UpdateFileOptions.md)|  | 

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_update_topics**
> repo_update_topics(owner, repo, body=body)

Replace list of topics for a repository

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
body = giteapy.RepoTopicOptions() # RepoTopicOptions |  (optional)

try:
    # Replace list of topics for a repository
    api_instance.repo_update_topics(owner, repo, body=body)
except ApiException as e:
    print("Exception when calling RepositoryApi->repo_update_topics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**RepoTopicOptions**](RepoTopicOptions.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topic_search**
> list[TopicResponse] topic_search(q)

search topics via keyword

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
q = 'q_example' # str | keywords to search

try:
    # search topics via keyword
    api_response = api_instance.topic_search(q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->topic_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| keywords to search | 

### Return type

[**list[TopicResponse]**](TopicResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_current_check_subscription**
> WatchInfo user_current_check_subscription(owner, repo)

Check if the current user is watching a repo

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo

try:
    # Check if the current user is watching a repo
    api_response = api_instance.user_current_check_subscription(owner, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->user_current_check_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**WatchInfo**](WatchInfo.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_current_delete_subscription**
> user_current_delete_subscription(owner, repo)

Unwatch a repo

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo

try:
    # Unwatch a repo
    api_instance.user_current_delete_subscription(owner, repo)
except ApiException as e:
    print("Exception when calling RepositoryApi->user_current_delete_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_current_put_subscription**
> WatchInfo user_current_put_subscription(owner, repo)

Watch a repo

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
api_instance = giteapy.RepositoryApi(giteapy.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo

try:
    # Watch a repo
    api_response = api_instance.user_current_put_subscription(owner, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->user_current_put_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**WatchInfo**](WatchInfo.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

