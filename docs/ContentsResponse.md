# ContentsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**FileLinksResponse**](FileLinksResponse.md) |  | [optional]
**content** | **str** | &#x60;content&#x60; is populated when &#x60;type&#x60; is &#x60;file&#x60;, otherwise null | [optional]
**download_url** | **str** |  | [optional]
**encoding** | **str** | &#x60;encoding&#x60; is populated when &#x60;type&#x60; is &#x60;file&#x60;, otherwise null | [optional]
**git_url** | **str** |  | [optional]
**html_url** | **str** |  | [optional]
**name** | **str** |  | [optional]
**path** | **str** |  | [optional]
**sha** | **str** |  | [optional]
**size** | **int** |  | [optional]
**submodule_git_url** | **str** | &#x60;submodule_git_url&#x60; is populated when &#x60;type&#x60; is &#x60;submodule&#x60;, otherwise null | [optional]
**target** | **str** | &#x60;target&#x60; is populated when &#x60;type&#x60; is &#x60;symlink&#x60;, otherwise null | [optional]
**type** | **str** | &#x60;type&#x60; will be &#x60;file&#x60;, &#x60;dir&#x60;, &#x60;symlink&#x60;, or &#x60;submodule&#x60; | [optional]
**url** | **str** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


