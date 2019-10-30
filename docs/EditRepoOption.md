# EditRepoOption

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_merge_commits** | **bool** | either &#x60;true&#x60; to allow merging pull requests with a merge commit, or &#x60;false&#x60; to prevent merging pull requests with merge commits. &#x60;has_pull_requests&#x60; must be &#x60;true&#x60;. | [optional] 
**allow_rebase** | **bool** | either &#x60;true&#x60; to allow rebase-merging pull requests, or &#x60;false&#x60; to prevent rebase-merging. &#x60;has_pull_requests&#x60; must be &#x60;true&#x60;. | [optional] 
**allow_rebase_explicit** | **bool** | either &#x60;true&#x60; to allow rebase with explicit merge commits (--no-ff), or &#x60;false&#x60; to prevent rebase with explicit merge commits. &#x60;has_pull_requests&#x60; must be &#x60;true&#x60;. | [optional] 
**allow_squash_merge** | **bool** | either &#x60;true&#x60; to allow squash-merging pull requests, or &#x60;false&#x60; to prevent squash-merging. &#x60;has_pull_requests&#x60; must be &#x60;true&#x60;. | [optional] 
**archived** | **bool** | set to &#x60;true&#x60; to archive this repository. | [optional] 
**default_branch** | **str** | sets the default branch for this repository. | [optional] 
**description** | **str** | a short description of the repository. | [optional] 
**external_tracker** | [**ExternalTracker**](ExternalTracker.md) |  | [optional] 
**external_wiki** | [**ExternalWiki**](ExternalWiki.md) |  | [optional] 
**has_issues** | **bool** | either &#x60;true&#x60; to enable issues for this repository or &#x60;false&#x60; to disable them. | [optional] 
**has_pull_requests** | **bool** | either &#x60;true&#x60; to allow pull requests, or &#x60;false&#x60; to prevent pull request. | [optional] 
**has_wiki** | **bool** | either &#x60;true&#x60; to enable the wiki for this repository or &#x60;false&#x60; to disable it. | [optional] 
**ignore_whitespace_conflicts** | **bool** | either &#x60;true&#x60; to ignore whitespace for conflicts, or &#x60;false&#x60; to not ignore whitespace. &#x60;has_pull_requests&#x60; must be &#x60;true&#x60;. | [optional] 
**internal_tracker** | [**InternalTracker**](InternalTracker.md) |  | [optional] 
**name** | **str** | name of the repository | [optional] 
**private** | **bool** | either &#x60;true&#x60; to make the repository private or &#x60;false&#x60; to make it public. Note: you will get a 422 error if the organization restricts changing repository visibility to organization owners and a non-owner tries to change the value of private. | [optional] 
**website** | **str** | a URL with more information about the repository. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


