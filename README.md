# Getting started

# Introduction


# Getting started
## Get an account
To use the API, you need an API account at Idfy You can get a free test account by going to our onboarding site and filling out the form there: [https://onboard.idfy.io](https://onboard.idfy.io) 
## Support
We’re here to help. Get in touch and we’ll get back to you as soon as we can. [Contact us](support@idfy.io).




# Statuspage
If you want to know the status of our services or subscribe to notifications go to our Statuspage: [http://signere.statuspage.io/](http://signere.statuspage.io/)

# REST API

## Statuscodes
* 200 OK: Everything worked as expected.
* 201 Created: New resource is created for example a new document for signing.
* 204 No content: The response code when a resource is deleted.
* 400 Bad request: The request was unacceptable, often due to missing a required parameter, or parameter not following given restrictions.
* 401 Unauthorized: Not authorized for this API
* 402 Payment Required: When trying to access an endpoint that are not in your current subscription. Contact sales@idfy.io.
* 403 Forbidden: Not correct scope/access to this resource
* 422 Unprocessable Entity: The request syntax is correct, but there is a business or logical error. For example sign xml signature with Swedish BankID that is not supported.
* 404 Not found: The route is not found or the entity is not found. Look at the reason phrase in the response to find detailed error.
* 429 Too Many Requests: The API have built in throttling to prevent any singel customer taking the API down.
* 503 Service Unavailable: A 3rd party services that this endpoint uses had an error or is unavailable.
* 50x Server errors: Something is wrong on the Idfy servers or the hosting environment.

## Http verbs
* Get: Get a resource
* Post: Create a new resource or exceute a command on the resource that is only can be exceuted once.
* Put: Replace a resource or exceute a command on the resource that is only can be exceuted mulitple times.
* Patch: Partially update a resoruce.
* Delete: Delete a resoure.

## Formats
The Idfy API only support json format at the time beeing. All request must use the Content-type header set top application/json. The json will use camelCasing. All request must use the UTF-8 encoding. All responsens will be in UTF-8.
All file download will be a standard http download result.

## Idempotent Requests
The APIs supports idempotency for safely retrying requests without accidentally performing the same operation twice. For example, if a request to create a new document fails due to a network connection error, you can retry the request with the same ExternalId  to guarantee that only a single document/identification is created.

## Compatibility
The Idfy API do change from time to time, but all changes will follow strict rules in order to keep the API's backward compatible. All new fields will be optional never required and if large changes are required a new endpoint will be created or a new API.
If an API are to be deprecated all customers will be given notice well in advance and not shutdown until all customers have converted to the new API's.

## Pagination (linked lists)
When using paging the list will be wrapped in a linked list object. The data contains the list-data in the result. There will also be navigation links for next, first, last and previous. The total amount of results (size) will also be inlcuded.
Example:
```json
{
   "offset": 0,
   "limit": 2,
   "size": 45,
   "links": {
     "next": "https://api.idfy.io/signature/documents/summary?limit=2&offset=2",
     "first": "https://api.idfy.io/signature/documents/summary?limit=2",
     "last": "",
     "previous": ""
   },
   "data": [
      "id": "2519011552909132317BrJ6VqOrcBYfwmgQ2eypM5XP7DEbCm8",
      "name": "Bruce Wayne",
      "status": "SUCCESS",
      "clientIp": "192.168.1.1",
      "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
      "identityProviderType": "NO_BANKID_WEB",
      "language": "NO",
      "externalid": "gtWEH8euBHeSWPTcjwB0Bg5o1mjsH106wmjTDMxoFnadzvNSsnSSY0zbJTpy",
      "timestamp": "2017-07-19T18:29:53.7550972Z",
      "iframe": false,
      "socialSecurityNumber": false
    },
    {
      "id": "2519011552909132317BrJ6VqOrcBYfwmgQ2eypM5XP7DEbCm8",
      "name": "Joker",
      "status": "ERROR",
      "clientIp": "192.168.1.1",
      "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
      "identityProviderType": "FI_TUPAS",
      "language": "NO",
      "externalid": "gtWEH8euBHeSWPTcjwB0Bg5o1mjsH106wmjTDMxoFnadzvNSsnSSY0zbJTpy",
      "errorcode": "TIMEOUT",
      "timestamp": "2017-07-19T18:29:53.7550972Z",
      "iframe": false,
      "socialSecurityNumber": false
    }
  ]
}
```

## Http Response headers
All API request have some standard http headers theese are:
* X-Idfy-Environment: (test or prod) this header tells you if you are talking to the test or the production environment.
* X-Idfy-AccountId: The Idfy accountID for the request.
* RequestId: Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You will also be able to use this to search in the logs in the Idfy dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.

# API Authentication
This API uses OAuth2 for authentication the requests. OAuth2 - an open protocol to allow secure authorization in a simple and standard method from web, mobile and desktop applications. Be sure to use client_credentials as grant type when connecting to this API. 

<b>Simple step by step guide to receive required access token </b><br/><br/>
1) Get access token <br/><br/>
http POST to https://oauth2test.signere.com/connect/token for test or https://oauth.signere.no/connect/token for prod <br/><br/>
&bull; Request Headers: <br/>
&nbsp;&nbsp;Content-Type: application/x-www-form-urlencoded <br/>
&nbsp;&nbsp;Authorization: Basic auth with ClientId as username, and ClientSecret as password<br/>
&nbsp;&nbsp;<i>Pseudo code: Authorization: "[ClientId]:[Secret]".ToBase64String() (utf-8) </i> <br/>
<br>
&bull; Request Body:<br/>
&nbsp;&nbsp;grant_type: client_credentials<br/>
&nbsp;&nbsp;scope: [insert scope(s) here] (Contact us if you dont have access to this scope) <br/>
<br>
2) Use access token to access our API<br/><br/>
In the response you will receive an item containing the id token you should use to connect to our API's named access_token.<br/>
&bull; This token can then be added to the header in the requests to this API:<br/> 
&nbsp;&nbsp; Authorization: Bearer [access_token]
<br><br>
We have created a guide to create Oauth2 tokens for different languages here: [https://sdk.signere.com/oauthtoken.html](https://sdk.signere.com/oauthtoken.html)
<br><br><i>Hint: The access token has a limited lifetime, check how long it will live in the response. Then you can save it to cache and reuse it (our .NET nuget client does this for you)</i><br><br>
Read more aboute OAuth2 here: 
[https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2](https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2)
<!-- ReDoc-Inject: <security-definitions> -->



## How to Build


You must have Python ```2 >=2.7.9``` or Python ```3 >=3.4``` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=IdfyRestClient-Python)


## How to Use

The following section explains how to use the IdfyRestClient SDK package in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=openProject0&workspaceFolder=IdfyRestClient-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=IdfyRestClient-Python&projectName=idfy_rest_client)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=IdfyRestClient-Python&projectName=idfy_rest_client)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=IdfyRestClient-Python&projectName=idfy_rest_client)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from idfy_rest_client.idfy_rest_client_client import IdfyRestClientClient
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=IdfyRestClient-Python&libraryName=idfy_rest_client.idfy_rest_client_client&projectName=idfy_rest_client&className=IdfyRestClientClient)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=IdfyRestClient-Python&libraryName=idfy_rest_client.idfy_rest_client_client&projectName=idfy_rest_client&className=IdfyRestClientClient)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke ```pip install -r test-requirements.txt```
  3. Invoke ```nosetests```

## Initialization

### Authentication
In order to setup authentication and initialization of the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| o_auth_client_id | OAuth 2 Client ID |
| o_auth_client_secret | OAuth 2 Client Secret |



API client can be initialized as following.

```python
# Configuration parameters and credentials
o_auth_client_id = 't50406ae2701149be8d72063a4ac005d0' # OAuth 2 Client ID
o_auth_client_secret = 'b3bf4003f34acc146a8270cb991fa2afc3be4a72df2aae0b5db3067120ec23a6' # OAuth 2 Client Secret

client = IdfyRestClientClient(o_auth_client_id, o_auth_client_secret)
```


You must now authorize the client.

### Authorizing your client

This SDK uses *OAuth 2.0 authorization* to authorize the client.

The `authorize()` method will exchange the OAuth client credentials for an *access token*.
The access token is an object containing information for authorizing client requests.

 You must pass the *[scopes](#scopes)* for which you need permission to access.
```python
try:
    client.auth.authorize([OAuthScope.ADDONS, OAuthScope.ACCOUNT_READ])
except OAuthProviderException as ex:
    # handle exception
```

The client can now make authorized endpoint calls.


### Scopes

Scopes enable your application to only request access to the resources it needs while enabling users to control the amount of access they grant to your application. Available scopes are defined in the `idfy_rest_client.models.o_auth_scope.OAuthScope` enumeration.

| Scope Name | Description |
| --- | --- |
| `ADDONS` |  |
| `ACCOUNT_READ` |  |
| `ACCOUNT_WRITE` |  |
| `OAUTH_TOKEN` |  |
| `OPENID_CLIENT` |  |
| `ROOT` |  |
| `ACCOUNT_CREATE` |  |
| `IDENTIFY` |  |
| `DOCUMENT_READ` |  |
| `DOCUMENT_WRITE` |  |
| `DOCUMENT_FILE` |  |
| `FORM_WRITE` |  |
| `FORM_READ` |  |
| `FORM_FILE` |  |
| `EVENT` |  |
| `INVOICE` |  |
| `ANALYTICS` |  |
| `AUDIT_ROOT` |  |
| `AUDIT_READ` |  |
| `AUDIT_WRITE` |  |
| `MERCHANTSIGN` |  |
| `VALIDATION` |  |
| `VALIDATION_SSN` |  |
| `TEXT_READ` |  |
| `TEXT_WRITE` |  |
| `OAUTH_WRITE` |  |
| `OPENID_WRITE` |  |

### Storing an access token for reuse

It is recommended that you store the access token for reuse.

You can store the access token in a file or a database.

```python
# store token
save_token_to_database(client.config.o_auth_token)
```

### Creating a client from a stored token

To authorize a client from a stored access token, just set the access token after creating the client:

```python
client = IdfyRestClientClient()
client.config.o_auth_token = load_token_from_database()
```

### Complete example

```python
from idfy_rest_client.idfy_rest_client_client import IdfyRestClientClient
from idfy_rest_client.models.o_auth_scope import OAuthScope
from idfy_rest_client.exceptions.o_auth_provider_exception import OAuthProviderException

# function for storing token to database
def save_token_to_database(token):
    # code to save the token to database

# function for loading token from database
def load_token_from_database():
    # load token from database and return it (return None if no token exists)

# Configuration parameters and credentials
o_auth_client_id = 't50406ae2701149be8d72063a4ac005d0' # OAuth 2 Client ID
o_auth_client_secret = 'b3bf4003f34acc146a8270cb991fa2afc3be4a72df2aae0b5db3067120ec23a6' # OAuth 2 Client Secret

#  create a new client
client = IdfyRestClientClient(o_auth_client_id, o_auth_client_secret)

# obtain access token, needed for client to be authorized
previous_token = load_token_from_database()
if previous_token:
    # restore previous access token
    client.config.o_auth_token = previous_token
else:
    # obtain new access token
    try:
        token = client.auth.authorize([OAuthScope.ADDONS, OAuthScope.ACCOUNT_READ])
        save_token_to_database(token)
    except OAuthProviderException as ex:
        # handle exception

# the client is now authorized and you can use controllers to make endpoint calls
```


# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [BusinessRegistryController](#business_registry_controller)
* [ThemesController](#themes_controller)
* [LanguageSetsController](#language_sets_controller)
* [LanguagesController](#languages_controller)
* [AccountController](#account_controller)
* [EventsController](#events_controller)
* [SignatureRolesCheckController](#signature_roles_check_controller)
* [ReportController](#report_controller)
* [PersonController](#person_controller)
* [LeiController](#lei_controller)
* [GeoDataController](#geo_data_controller)
* [BusinessController](#business_controller)
* [SignersController](#signers_controller)
* [NotificationsController](#notifications_controller)
* [JwtController](#jwt_controller)
* [FilesController](#files_controller)
* [DocumentsController](#documents_controller)
* [AttachmentsController](#attachments_controller)
* [SignatureController](#signature_controller)
* [TranslationsController](#translations_controller)
* [TemplateController](#template_controller)
* [OpenIDController](#open_id_controller)
* [OAuthAPIClientController](#o_auth_api_client_controller)
* [DealerController](#dealer_controller)
* [MobileInfoController](#mobile_info_controller)
* [NorwegianBankIDController](#norwegian_bank_id_controller)
* [NorwgianBankIDController](#norwgian_bank_id_controller)
* [LogController](#log_controller)
* [IdentificationSessionController](#identification_session_controller)
* [WebhooksController](#webhooks_controller)
* [AmlController](#aml_controller)
* [InvoiceController](#invoice_controller)

## <a name="business_registry_controller"></a>![Class: ](https://apidocs.io/img/class.png ".BusinessRegistryController") BusinessRegistryController

### Get controller instance

An instance of the ``` BusinessRegistryController ``` class can be accessed from the API Client.

```python
 business_registry_controller = client.business_registry
```

### <a name="list_registration_authorities"></a>![Method: ](https://apidocs.io/img/method.png ".BusinessRegistryController.list_registration_authorities") list_registration_authorities

> Retrieves a list of business registration authorities globally

```python
def list_registration_authorities(self)
```

#### Example Usage

```python

result = business_registry_controller.list_registration_authorities()

```


### <a name="retrieve_registration_authority"></a>![Method: ](https://apidocs.io/img/method.png ".BusinessRegistryController.retrieve_registration_authority") retrieve_registration_authority

> Retrieves detailed information about a specific registration authority

```python
def retrieve_registration_authority(self,
                                        authority_code)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| authorityCode |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
authority_code = 'authorityCode'

result = business_registry_controller.retrieve_registration_authority(authority_code)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="themes_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ThemesController") ThemesController

### Get controller instance

An instance of the ``` ThemesController ``` class can be accessed from the API Client.

```python
 themes_controller = client.themes
```

### <a name="themes_list_spinners"></a>![Method: ](https://apidocs.io/img/method.png ".ThemesController.themes_list_spinners") themes_list_spinners

> *Tags:*  ``` Skips Authentication ``` 

> This endpoint lists all the spinners you can use in our sign application

```python
def themes_list_spinners(self)
```

#### Example Usage

```python

result = themes_controller.themes_list_spinners()

```


### <a name="themes_list_themes"></a>![Method: ](https://apidocs.io/img/method.png ".ThemesController.themes_list_themes") themes_list_themes

> *Tags:*  ``` Skips Authentication ``` 

> This endpoint lists all the color themes you can use in our sign application

```python
def themes_list_themes(self)
```

#### Example Usage

```python

result = themes_controller.themes_list_themes()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="language_sets_controller"></a>![Class: ](https://apidocs.io/img/class.png ".LanguageSetsController") LanguageSetsController

### Get controller instance

An instance of the ``` LanguageSetsController ``` class can be accessed from the API Client.

```python
 language_sets_controller = client.language_sets
```

### <a name="create_language_set"></a>![Method: ](https://apidocs.io/img/method.png ".LanguageSetsController.create_language_set") create_language_set

> *Tags:*  ``` Skips Authentication ``` 

> Creates a new language set.

```python
def create_language_set(self,
                            new_language_set=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| newLanguageSet |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
new_language_set = LanguageSetCreateDTO()

result = language_sets_controller.create_language_set(new_language_set)

```


### <a name="list_language_sets"></a>![Method: ](https://apidocs.io/img/method.png ".LanguageSetsController.list_language_sets") list_language_sets

> *Tags:*  ``` Skips Authentication ``` 

> Returns a list of all your language sets.

```python
def list_language_sets(self)
```

#### Example Usage

```python

result = language_sets_controller.list_language_sets()

```


### <a name="update_language_set"></a>![Method: ](https://apidocs.io/img/method.png ".LanguageSetsController.update_language_set") update_language_set

> *Tags:*  ``` Skips Authentication ``` 

> Updates the specified language set with the parameters passed.

```python
def update_language_set(self,
                            id,
                            language_set_update=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |
| languageSetUpdate |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
id = 238
language_set_update = LanguageSetUpdateDTO()

result = language_sets_controller.update_language_set(id, language_set_update)

```


### <a name="delete_language_set"></a>![Method: ](https://apidocs.io/img/method.png ".LanguageSetsController.delete_language_set") delete_language_set

> *Tags:*  ``` Skips Authentication ``` 

> Deletes the specified language set.

```python
def delete_language_set(self,
                            id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
id = 238

language_sets_controller.delete_language_set(id)

```


### <a name="retrieve_language_set"></a>![Method: ](https://apidocs.io/img/method.png ".LanguageSetsController.retrieve_language_set") retrieve_language_set

> *Tags:*  ``` Skips Authentication ``` 

> Retrieves the details of a single language set.

```python
def retrieve_language_set(self,
                              id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
id = 238

result = language_sets_controller.retrieve_language_set(id)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="languages_controller"></a>![Class: ](https://apidocs.io/img/class.png ".LanguagesController") LanguagesController

### Get controller instance

An instance of the ``` LanguagesController ``` class can be accessed from the API Client.

```python
 languages_controller = client.languages
```

### <a name="list_all_languages"></a>![Method: ](https://apidocs.io/img/method.png ".LanguagesController.list_all_languages") list_all_languages

> *Tags:*  ``` Skips Authentication ``` 

> Returns a list of all supported languages.

```python
def list_all_languages(self)
```

#### Example Usage

```python

result = languages_controller.list_all_languages()

```


### <a name="retrieve_language"></a>![Method: ](https://apidocs.io/img/method.png ".LanguagesController.retrieve_language") retrieve_language

> *Tags:*  ``` Skips Authentication ``` 

> Retrieve language

```python
def retrieve_language(self,
                          id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
id = 238

result = languages_controller.retrieve_language(id)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="account_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AccountController") AccountController

### Get controller instance

An instance of the ``` AccountController ``` class can be accessed from the API Client.

```python
 account_controller = client.account
```

### <a name="list_account_names"></a>![Method: ](https://apidocs.io/img/method.png ".AccountController.list_account_names") list_account_names

> *Tags:*  ``` Skips Authentication ``` 

> List names of accounts you have access to

```python
def list_account_names(self)
```

#### Example Usage

```python

result = account_controller.list_account_names()

```


### <a name="disable_account"></a>![Method: ](https://apidocs.io/img/method.png ".AccountController.disable_account") disable_account

> Set the account as incative / disabled. Requires one of the following scopes: [root, account-write, dealer]

```python
def disable_account(self)
```

#### Example Usage

```python

result = account_controller.disable_account()

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="update_account_styling"></a>![Method: ](https://apidocs.io/img/method.png ".AccountController.update_account_styling") update_account_styling

> Upload / Update custom account css. Returns a url with your uploaded css. Requires one of the following scopes: [root, account-write, dealer]

```python
def update_account_styling(self,
                               styling)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| styling |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
styling = Styling()

result = account_controller.update_account_styling(styling)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="update_account_logo"></a>![Method: ](https://apidocs.io/img/method.png ".AccountController.update_account_logo") update_account_logo

> Upload / Update and resize account logo. Returns a url with your uploaded / resized logo. Requires one of the following scopes: [root, account-write, dealer]

```python
def update_account_logo(self,
                            account_logo)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| accountLogo |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
account_logo = AccountLogo()

result = account_controller.update_account_logo(account_logo)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="create_account"></a>![Method: ](https://apidocs.io/img/method.png ".AccountController.create_account") create_account

> *Tags:*  ``` Skips Authentication ``` 

> Requires one of the following scopes: [dealer]

```python
def create_account(self,
                       account_details)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| accountDetails |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
account_details = CreateAccountRequest()

result = account_controller.create_account(account_details)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="update_account"></a>![Method: ](https://apidocs.io/img/method.png ".AccountController.update_account") update_account

> Requires one of the following scopes: [root, account-write, dealer]

```python
def update_account(self,
                       account_details)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| accountDetails |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
account_details = UpdateAccountRequest()

result = account_controller.update_account(account_details)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="retrieve_account"></a>![Method: ](https://apidocs.io/img/method.png ".AccountController.retrieve_account") retrieve_account

> Requires one of the following scopes: [root, account-read, dealer]

```python
def retrieve_account(self)
```

#### Example Usage

```python

result = account_controller.retrieve_account()

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="list_accounts"></a>![Method: ](https://apidocs.io/img/method.png ".AccountController.list_accounts") list_accounts

> *Tags:*  ``` Skips Authentication ``` 

> List accounts you have access to

```python
def list_accounts(self,
                      filter_name=None,
                      filter_org_no=None,
                      filter_uni_customer_no=None,
                      filter_created_before=None,
                      filter_created_after=None,
                      filter_last_modified_before=None,
                      filter_last_modified_after=None,
                      filter_dealer_name=None,
                      filter_dealer_reference=None,
                      filter_enabled=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| filterName |  ``` Optional ```  | TODO: Add a parameter description |
| filterOrgNo |  ``` Optional ```  | TODO: Add a parameter description |
| filterUniCustomerNo |  ``` Optional ```  | TODO: Add a parameter description |
| filterCreatedBefore |  ``` Optional ```  | TODO: Add a parameter description |
| filterCreatedAfter |  ``` Optional ```  | TODO: Add a parameter description |
| filterLastModifiedBefore |  ``` Optional ```  | TODO: Add a parameter description |
| filterLastModifiedAfter |  ``` Optional ```  | TODO: Add a parameter description |
| filterDealerName |  ``` Optional ```  | TODO: Add a parameter description |
| filterDealerReference |  ``` Optional ```  | TODO: Add a parameter description |
| filterEnabled |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
filter_name = 'filter.name'
filter_org_no = 'filter.orgNo'
filter_uni_customer_no = 'filter.uniCustomerNo'
filter_created_before = datetime.now()
filter_created_after = datetime.now()
filter_last_modified_before = datetime.now()
filter_last_modified_after = datetime.now()
filter_dealer_name = 'filter.dealerName'
filter_dealer_reference = 'filter.dealerReference'
filter_enabled = False

result = account_controller.list_accounts(filter_name, filter_org_no, filter_uni_customer_no, filter_created_before, filter_created_after, filter_last_modified_before, filter_last_modified_after, filter_dealer_name, filter_dealer_reference, filter_enabled)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="events_controller"></a>![Class: ](https://apidocs.io/img/class.png ".EventsController") EventsController

### Get controller instance

An instance of the ``` EventsController ``` class can be accessed from the API Client.

```python
 events_controller = client.events
```

### <a name="events_get_event_types"></a>![Method: ](https://apidocs.io/img/method.png ".EventsController.events_get_event_types") events_get_event_types

> Returns a list of all available event types.

```python
def events_get_event_types(self)
```

#### Example Usage

```python

result = events_controller.events_get_event_types()

```


### <a name="events_clear"></a>![Method: ](https://apidocs.io/img/method.png ".EventsController.events_clear") events_clear

> Clear all events for your account

```python
def events_clear(self)
```

#### Example Usage

```python

events_controller.events_clear()

```


### <a name="events_peek"></a>![Method: ](https://apidocs.io/img/method.png ".EventsController.events_peek") events_peek

> Peek top 100 unhandled events regardless if they are locked or not. Dont use this endpoint to handle events.

```python
def events_peek(self,
                    event_type=None,
                    tags=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| eventType |  ``` Optional ```  | Filter by event type |
| tags |  ``` Optional ```  | Filter the events with your own tags that you added to the document when you created it (Separate tags with ,) |



#### Example Usage

```python
event_type = EventType.DOCUMENT_BEFORE_DELETED
tags = 'tags'

result = events_controller.events_peek(event_type, tags)

```


### <a name="events_handle"></a>![Method: ](https://apidocs.io/img/method.png ".EventsController.events_handle") events_handle

> Mark the status of an event as handled to make sure you dont retrieve this event again

```python
def events_handle(self,
                      event_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| eventId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
event_id = uuid.uuid4()

events_controller.events_handle(event_id)

```


### <a name="events_handle_many"></a>![Method: ](https://apidocs.io/img/method.png ".EventsController.events_handle_many") events_handle_many

> Mark the status of a batch of events as handled to make sure you dont retrieve these events again

```python
def events_handle_many(self,
                           event_ids)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| eventIds |  ``` Required ```  ``` Collection ```  | TODO: Add a parameter description |



#### Example Usage

```python
event_ids = [uuid.uuid4()]

events_controller.events_handle_many(event_ids)

```


### <a name="events_get"></a>![Method: ](https://apidocs.io/img/method.png ".EventsController.events_get") events_get

> Retrieve up to 100 unhandled events for your account. After you retrieve this list the
> 
>              events will be "locked" for 10 minutes to give you time to handle them. Please handle the events using one of the endpoints in this API to avoid retrieving the same events multiple times.

```python
def events_get(self,
                   event_type=None,
                   tags=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| eventType |  ``` Optional ```  | Filter by event type |
| tags |  ``` Optional ```  | Filter the events with your own tags that you added to the document when you created it (Separate tags with ,) |



#### Example Usage

```python
event_type = EventType.DOCUMENT_BEFORE_DELETED
tags = 'tags'

result = events_controller.events_get(event_type, tags)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="signature_roles_check_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SignatureRolesCheckController") SignatureRolesCheckController

### Get controller instance

An instance of the ``` SignatureRolesCheckController ``` class can be accessed from the API Client.

```python
 signature_roles_check_controller = client.signature_roles_check
```

### <a name="get_rights"></a>![Method: ](https://apidocs.io/img/method.png ".SignatureRolesCheckController.get_rights") get_rights

> Check which person(s) that has the right to sign documents in an organization. You will receive lists with names and date of birth for the persons allowed for signing / prokura.

```python
def get_rights(self,
                   orgnumber,
                   countrycode=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| orgnumber |  ``` Required ```  | TODO: Add a parameter description |
| countrycode |  ``` Optional ```  | Default value is "NO" |



#### Example Usage

```python
orgnumber = 'orgnumber'
countrycode = 'countrycode'

result = signature_roles_check_controller.get_rights(orgnumber, countrycode)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 401 | Not authorized |
| 404 | Organization data not found |
| 500 | Internal server error (Miscellaneous) |




### <a name="check_signatures_prokura"></a>![Method: ](https://apidocs.io/img/method.png ".SignatureRolesCheckController.check_signatures_prokura") check_signatures_prokura

> Check if received signatures and/or prokura are valid. This call allows you to do this check for multiple organizations simulataneously.
> 
> A valid date of birth in this format [ddMMyy] is required. The persons last name plus minimum one other part of the signees name (first, (middle) and last name has to be separated by whitespace, comma or ;). 
> 
> A report that explains the validity of the signatures can be included.

```python
def check_signatures_prokura(self,
                                 data,
                                 includereport=None,
                                 countrycode=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| data |  ``` Required ```  | An array including all the organizations you want to check |
| includereport |  ``` Optional ```  | Returns a pdf report explaining the validity of the checked signatures, default value is true |
| countrycode |  ``` Optional ```  | Default value is "NO" |



#### Example Usage

```python
data = SignatureCheckRequest()
includereport = False
countrycode = 'countrycode'

result = signature_roles_check_controller.check_signatures_prokura(data, includereport, countrycode)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 401 | Not authorized |
| 404 | Organization data not found |
| 500 | Internal server error (Miscellaneous) |




[Back to List of Controllers](#list_of_controllers)

## <a name="report_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ReportController") ReportController

### Get controller instance

An instance of the ``` ReportController ``` class can be accessed from the API Client.

```python
 report_controller = client.report
```

### <a name="retrive_signature_roles_report"></a>![Method: ](https://apidocs.io/img/method.png ".ReportController.retrive_signature_roles_report") retrive_signature_roles_report

> The pdf report will be awailable to download the first 48 hours.

```python
def retrive_signature_roles_report(self,
                                       report_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| reportId |  ``` Required ```  | The reportId returned from the Get |



#### Example Usage

```python
report_id = 'reportId'

report_controller.retrive_signature_roles_report(report_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 401 | Not authorized |
| 404 | Organization data not found |
| 500 | Internal server error (Miscellaneous) |




[Back to List of Controllers](#list_of_controllers)

## <a name="person_controller"></a>![Class: ](https://apidocs.io/img/class.png ".PersonController") PersonController

### Get controller instance

An instance of the ``` PersonController ``` class can be accessed from the API Client.

```python
 person_controller = client.person
```

### <a name="list_person_info_through_matchit_by_query"></a>![Method: ](https://apidocs.io/img/method.png ".PersonController.list_person_info_through_matchit_by_query") list_person_info_through_matchit_by_query

> Returns (unofficial) person information, this method returns the 5 best matches from the query parameters served (freetext). The information is delievered by Matchit.

```python
def list_person_info_through_matchit_by_query(self,
                                                  query_string)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| queryString |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
query_string = 'queryString'

result = person_controller.list_person_info_through_matchit_by_query(query_string)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 401 | Not authorized |
| 500 | Internal server error (Miscellaneous) |




### <a name="retrieve_person_info_through_matchit"></a>![Method: ](https://apidocs.io/img/method.png ".PersonController.retrieve_person_info_through_matchit") retrieve_person_info_through_matchit

> Returns (unofficial) person information, this method returns the best match from the query parameters served. The information is delievered by Matchit. 
> 
> Valid query parameter combinations: name + dateOfBirth, name + socialSec, name + address, phonenumber

```python
def retrieve_person_info_through_matchit(self,
                                             name=None,
                                             social_sec=None,
                                             date_of_birth=None,
                                             phonenumber=None,
                                             address=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| name |  ``` Optional ```  | TODO: Add a parameter description |
| socialSec |  ``` Optional ```  | TODO: Add a parameter description |
| dateOfBirth |  ``` Optional ```  | TODO: Add a parameter description |
| phonenumber |  ``` Optional ```  | TODO: Add a parameter description |
| address |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
name = 'name'
social_sec = 'socialSec'
date_of_birth = 'dateOfBirth'
phonenumber = 'phonenumber'
address = 'address'

result = person_controller.retrieve_person_info_through_matchit(name, social_sec, date_of_birth, phonenumber, address)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 401 | Not authorized |
| 500 | Internal server error (Miscellaneous) |




### <a name="run_credit_check"></a>![Method: ](https://apidocs.io/img/method.png ".PersonController.run_credit_check") run_credit_check

> Credit check of a single person. The use of this will produce a duplicate letter to the person that is checked.
> 
>              A pdf report will be awailable to download the first 48 hours.

```python
def run_credit_check(self,
                         social_security_number,
                         user_id=None,
                         password=None,
                         phonenumber=None,
                         email=None,
                         include_report=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| socialSecurityNumber |  ``` Required ```  | TODO: Add a parameter description |
| userId |  ``` Optional ```  | Override bisnode user Id |
| password |  ``` Optional ```  | Override bisnode password |
| phonenumber |  ``` Optional ```  | Specify this to use electronic duplicate letters |
| email |  ``` Optional ```  | Specify this to use electronic duplicate letters |
| includeReport |  ``` Optional ```  | Specify if you want a pdf report (defaults to false) |



#### Example Usage

```python
social_security_number = 74
user_id = 'userId'
password = 'password'
phonenumber = 74
email = 'email'
include_report = False

result = person_controller.run_credit_check(social_security_number, user_id, password, phonenumber, email, include_report)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 401 | Not authorized |
| 500 | Internal server error (Miscellaneous) |




### <a name="retrieve_person_info_through_infotorget"></a>![Method: ](https://apidocs.io/img/method.png ".PersonController.retrieve_person_info_through_infotorget") retrieve_person_info_through_infotorget

> Run a query using social security number as parameter. The use of this requires username and password for Infortorget with the required permissions.
> 
> Valid query parameter combinations: 
> 
> socialSecurityNumber, 
> 
> socialSecurityNumber + firstName + lastName, 
> 
> dateOfBirth + firstName + lastName, 
> 
> firstName + lastName + address + postalCode

```python
def retrieve_person_info_through_infotorget(self,
                                                username,
                                                password,
                                                reason,
                                                system,
                                                social_security_number=None,
                                                firstname=None,
                                                lastname=None,
                                                dateofbirth=None,
                                                address=None,
                                                postalcode=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| username |  ``` Required ```  | Infotorget username |
| password |  ``` Required ```  | Infotorget password |
| reason |  ``` Required ```  | Reason for request |
| system |  ``` Required ```  | Your system name (Cannot contain any special characters or numbers) |
| socialSecurityNumber |  ``` Optional ```  | TODO: Add a parameter description |
| firstname |  ``` Optional ```  | TODO: Add a parameter description |
| lastname |  ``` Optional ```  | TODO: Add a parameter description |
| dateofbirth |  ``` Optional ```  | TODO: Add a parameter description |
| address |  ``` Optional ```  | TODO: Add a parameter description |
| postalcode |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
username = 'username'
password = 'password'
reason = 'reason'
system = 'system'
social_security_number = 'socialSecurityNumber'
firstname = 'firstname'
lastname = 'lastname'
dateofbirth = 74
address = 'address'
postalcode = 'postalcode'

result = person_controller.retrieve_person_info_through_infotorget(username, password, reason, system, social_security_number, firstname, lastname, dateofbirth, address, postalcode)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 401 | Not authorized |
| 500 | Internal server error (Miscellaneous) |




[Back to List of Controllers](#list_of_controllers)

## <a name="lei_controller"></a>![Class: ](https://apidocs.io/img/class.png ".LeiController") LeiController

### Get controller instance

An instance of the ``` LeiController ``` class can be accessed from the API Client.

```python
 lei_controller = client.lei
```

### <a name="retrieve_lei_record"></a>![Method: ](https://apidocs.io/img/method.png ".LeiController.retrieve_lei_record") retrieve_lei_record

> Retrieve the entity record for a given LEI

```python
def retrieve_lei_record(self,
                            lei)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| lei |  ``` Required ```  | LEI to retrieve |



#### Example Usage

```python
lei = 'lei'

result = lei_controller.retrieve_lei_record(lei)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Not authorized |
| 404 | Not found |




### <a name="query_lei_records"></a>![Method: ](https://apidocs.io/img/method.png ".LeiController.query_lei_records") query_lei_records

> QueryLeiRecords for LEI-registered entities with filters

```python
def query_lei_records(self,
                          country_code=None,
                          lei=None,
                          legal_name_contains=None,
                          legal_name_equals=None,
                          registration_authority_entity_id=None,
                          page_size=None,
                          page=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| countryCode |  ``` Optional ```  | ISO 3166-1 alpha-2 country code for country entity is registered in |
| lei |  ``` Optional ```  | LEI of entity |
| legalNameContains |  ``` Optional ```  | Words included in entity's legal name |
| legalNameEquals |  ``` Optional ```  | Exact phrase included in entity's legal name |
| registrationAuthorityEntityId |  ``` Optional ```  | Entity Id provided by local business registry authority. For Norway this is the 'organisasjonsnummer' or tax identification number of the business |
| pageSize |  ``` Optional ```  | Size of result set per request. Defaults to 25 |
| page |  ``` Optional ```  | Current page number for result set. Defaults to 0 |



#### Example Usage

```python
country_code = 'countryCode'
lei = 'lei'
legal_name_contains = 'legalNameContains'
legal_name_equals = 'legalNameEquals'
registration_authority_entity_id = 'registrationAuthorityEntityId'
page_size = 74
page = 74

result = lei_controller.query_lei_records(country_code, lei, legal_name_contains, legal_name_equals, registration_authority_entity_id, page_size, page)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Not authorized |




[Back to List of Controllers](#list_of_controllers)

## <a name="geo_data_controller"></a>![Class: ](https://apidocs.io/img/class.png ".GeoDataController") GeoDataController

### Get controller instance

An instance of the ``` GeoDataController ``` class can be accessed from the API Client.

```python
 geo_data_controller = client.geo_data
```

### <a name="list_country_subdivisions"></a>![Method: ](https://apidocs.io/img/method.png ".GeoDataController.list_country_subdivisions") list_country_subdivisions

> Retrieves a list over top level administrative subdivisions for a country with name and ISO 3166-2 region code

```python
def list_country_subdivisions(self,
                                  country_code,
                                  lang=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| countryCode |  ``` Required ```  | ISO 3166-1 country code to look up |
| lang |  ``` Optional ```  | Language for result. Defaults to English |



#### Example Usage

```python
country_code = 'countryCode'
lang = 'lang'

result = geo_data_controller.list_country_subdivisions(country_code, lang)

```


### <a name="retrieve_country_info"></a>![Method: ](https://apidocs.io/img/method.png ".GeoDataController.retrieve_country_info") retrieve_country_info

> Retrieves basic geographical information about a country

```python
def retrieve_country_info(self,
                              country_code,
                              lang=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| countryCode |  ``` Required ```  | ISO 3166-1 country code to look up |
| lang |  ``` Optional ```  | Language for result. Defaults to English |



#### Example Usage

```python
country_code = 'countryCode'
lang = 'lang'

result = geo_data_controller.retrieve_country_info(country_code, lang)

```


### <a name="list_countries"></a>![Method: ](https://apidocs.io/img/method.png ".GeoDataController.list_countries") list_countries

> Lists all countries in the world with English name and ISO 3166-1 country code

```python
def list_countries(self,
                       lang=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| lang |  ``` Optional ```  | Language for result. Defaults to English |



#### Example Usage

```python
lang = 'lang'

result = geo_data_controller.list_countries(lang)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="business_controller"></a>![Class: ](https://apidocs.io/img/class.png ".BusinessController") BusinessController

### Get controller instance

An instance of the ``` BusinessController ``` class can be accessed from the API Client.

```python
 business_controller = client.business
```

### <a name="retrieve_information_from_matchit"></a>![Method: ](https://apidocs.io/img/method.png ".BusinessController.retrieve_information_from_matchit") retrieve_information_from_matchit

> Query company information from Matchit, Matchit uses existing information to build up their database. Supports query by name and/or orgnumber

```python
def retrieve_information_from_matchit(self,
                                          companyname=None,
                                          orgnumber=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| companyname |  ``` Optional ```  | query param |
| orgnumber |  ``` Optional ```  | query param |



#### Example Usage

```python
companyname = 'companyname'
orgnumber = 'orgnumber'

result = business_controller.retrieve_information_from_matchit(companyname, orgnumber)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 401 | Not authorized |
| 404 | Not found |
| 500 | Internal Server Error (Miscellaneous) |




### <a name="retrieve_information_from_difi"></a>![Method: ](https://apidocs.io/img/method.png ".BusinessController.retrieve_information_from_difi") retrieve_information_from_difi

> Query company information from difi datahotell (official data from bronnoysund), supports query by name and/or orgnumber

```python
def retrieve_information_from_difi(self,
                                       orgnumber=None,
                                       companyname=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| orgnumber |  ``` Optional ```  | TODO: Add a parameter description |
| companyname |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
orgnumber = 'orgnumber'
companyname = 'companyname'

result = business_controller.retrieve_information_from_difi(orgnumber, companyname)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 404 | Not found |
| 500 | Internal Server Error (Miscellaneous) |




### <a name="perform_credit_check"></a>![Method: ](https://apidocs.io/img/method.png ".BusinessController.perform_credit_check") perform_credit_check

> Run a credit check on a specified company, this check will not produce any duplicate letters.
> 
>              A pdf report will be awailable to download the first 48 hours.

```python
def perform_credit_check(self,
                             orgnumber,
                             user_id=None,
                             password=None,
                             country_code=None,
                             include_report=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| orgnumber |  ``` Required ```  | TODO: Add a parameter description |
| userId |  ``` Optional ```  | Override bisnode user Id |
| password |  ``` Optional ```  | Override bisnode password |
| countryCode |  ``` Optional ```  | Default = "NO" |
| includeReport |  ``` Optional ```  | Specify if you want a pdf report (defaults to false) |



#### Example Usage

```python
orgnumber = 33
user_id = 'userId'
password = 'password'
country_code = 'countryCode'
include_report = False

result = business_controller.perform_credit_check(orgnumber, user_id, password, country_code, include_report)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 401 | Not authorized |
| 500 | Internal server error (Miscellaneous) |




[Back to List of Controllers](#list_of_controllers)

## <a name="signers_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SignersController") SignersController

### Get controller instance

An instance of the ``` SignersController ``` class can be accessed from the API Client.

```python
 signers_controller = client.signers
```

### <a name="signers_add"></a>![Method: ](https://apidocs.io/img/method.png ".SignersController.signers_add") signers_add

> Create signer

```python
def signers_add(self,
                    document_id,
                    signer)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| documentId |  ``` Required ```  | TODO: Add a parameter description |
| signer |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
document_id = uuid.uuid4()
signer = SignerWrapper()

result = signers_controller.signers_add(document_id, signer)

```


### <a name="signers_list"></a>![Method: ](https://apidocs.io/img/method.png ".SignersController.signers_list") signers_list

> List signers

```python
def signers_list(self,
                     document_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| documentId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
document_id = uuid.uuid4()

result = signers_controller.signers_list(document_id)

```


### <a name="signers_update"></a>![Method: ](https://apidocs.io/img/method.png ".SignersController.signers_update") signers_update

> Update signer

```python
def signers_update(self,
                       document_id,
                       signer_id,
                       request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| documentId |  ``` Required ```  | TODO: Add a parameter description |
| signerId |  ``` Required ```  | TODO: Add a parameter description |
| request |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
document_id = uuid.uuid4()
signer_id = uuid.uuid4()
request = UpdateSignerRequestWrapper()

result = signers_controller.signers_update(document_id, signer_id, request)

```


### <a name="signers_delete"></a>![Method: ](https://apidocs.io/img/method.png ".SignersController.signers_delete") signers_delete

> Delete signer

```python
def signers_delete(self,
                       document_id,
                       signer_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| documentId |  ``` Required ```  | TODO: Add a parameter description |
| signerId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
document_id = uuid.uuid4()
signer_id = uuid.uuid4()

result = signers_controller.signers_delete(document_id, signer_id)

```


### <a name="signers_get"></a>![Method: ](https://apidocs.io/img/method.png ".SignersController.signers_get") signers_get

> Retrieves the details of a single signer.

```python
def signers_get(self,
                    document_id,
                    signer_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| documentId |  ``` Required ```  | TODO: Add a parameter description |
| signerId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
document_id = uuid.uuid4()
signer_id = uuid.uuid4()

result = signers_controller.signers_get(document_id, signer_id)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="notifications_controller"></a>![Class: ](https://apidocs.io/img/class.png ".NotificationsController") NotificationsController

### Get controller instance

An instance of the ``` NotificationsController ``` class can be accessed from the API Client.

```python
 notifications_controller = client.notifications
```

### <a name="notifications_list"></a>![Method: ](https://apidocs.io/img/method.png ".NotificationsController.notifications_list") notifications_list

> Returns a list of all notifications that has been sent / attempted sent for a document

```python
def notifications_list(self,
                           document_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| documentId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
document_id = uuid.uuid4()

result = notifications_controller.notifications_list(document_id)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="jwt_controller"></a>![Class: ](https://apidocs.io/img/class.png ".JwtController") JwtController

### Get controller instance

An instance of the ``` JwtController ``` class can be accessed from the API Client.

```python
 jwt_controller = client.jwt
```

### <a name="jwt_validate"></a>![Method: ](https://apidocs.io/img/method.png ".JwtController.jwt_validate") jwt_validate

> *Tags:*  ``` Skips Authentication ``` 

> Validate JWT

```python
def jwt_validate(self,
                     request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
request = JwtValidationRequest()

result = jwt_controller.jwt_validate(request)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="files_controller"></a>![Class: ](https://apidocs.io/img/class.png ".FilesController") FilesController

### Get controller instance

An instance of the ``` FilesController ``` class can be accessed from the API Client.

```python
 files_controller = client.files
```

### <a name="files_get_signer_attachment"></a>![Method: ](https://apidocs.io/img/method.png ".FilesController.files_get_signer_attachment") files_get_signer_attachment

> Retrieves the attachment file for the specified signer.

```python
def files_get_signer_attachment(self,
                                    document_id,
                                    attachment_id,
                                    signer_id,
                                    file_format)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| documentId |  ``` Required ```  | TODO: Add a parameter description |
| attachmentId |  ``` Required ```  | TODO: Add a parameter description |
| signerId |  ``` Required ```  | The signers Id |
| fileFormat |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
document_id = uuid.uuid4()
attachment_id = uuid.uuid4()
signer_id = uuid.uuid4()
file_format = FileFormat331.ENUM_NATIVE

result = files_controller.files_get_signer_attachment(document_id, attachment_id, signer_id, file_format)

```


### <a name="files_get_attachment"></a>![Method: ](https://apidocs.io/img/method.png ".FilesController.files_get_attachment") files_get_attachment

> Retrieves the attachment file.

```python
def files_get_attachment(self,
                             document_id,
                             attachment_id,
                             file_format)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| documentId |  ``` Required ```  | TODO: Add a parameter description |
| attachmentId |  ``` Required ```  | TODO: Add a parameter description |
| fileFormat |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
document_id = uuid.uuid4()
attachment_id = uuid.uuid4()
file_format = FileFormat.ENUM_UNSIGNED

result = files_controller.files_get_attachment(document_id, attachment_id, file_format)

```


### <a name="files_get_signer"></a>![Method: ](https://apidocs.io/img/method.png ".FilesController.files_get_signer") files_get_signer

> Retrieves the signed document file for the specified signer.

```python
def files_get_signer(self,
                         document_id,
                         signer_id,
                         file_format)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| documentId |  ``` Required ```  | TODO: Add a parameter description |
| signerId |  ``` Required ```  | The signers Id |
| fileFormat |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
document_id = uuid.uuid4()
signer_id = uuid.uuid4()
file_format = FileFormat331.ENUM_NATIVE

result = files_controller.files_get_signer(document_id, signer_id, file_format)

```


### <a name="files_get"></a>![Method: ](https://apidocs.io/img/method.png ".FilesController.files_get") files_get

> Retrieves the signed document file.

```python
def files_get(self,
                  document_id,
                  file_format)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| documentId |  ``` Required ```  | TODO: Add a parameter description |
| fileFormat |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
document_id = uuid.uuid4()
file_format = FileFormat.ENUM_UNSIGNED

result = files_controller.files_get(document_id, file_format)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="documents_controller"></a>![Class: ](https://apidocs.io/img/class.png ".DocumentsController") DocumentsController

### Get controller instance

An instance of the ``` DocumentsController ``` class can be accessed from the API Client.

```python
 documents_controller = client.documents
```

### <a name="documents_get_summary"></a>![Method: ](https://apidocs.io/img/method.png ".DocumentsController.documents_get_summary") documents_get_summary

> Get information about a document

```python
def documents_get_summary(self,
                              document_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| documentId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
document_id = uuid.uuid4()

result = documents_controller.documents_get_summary(document_id)

```


### <a name="documents_status"></a>![Method: ](https://apidocs.io/img/method.png ".DocumentsController.documents_status") documents_status

> Get the status of a document

```python
def documents_status(self,
                         document_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| documentId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
document_id = uuid.uuid4()

result = documents_controller.documents_status(document_id)

```


### <a name="documents_cancel"></a>![Method: ](https://apidocs.io/img/method.png ".DocumentsController.documents_cancel") documents_cancel

> Cancel document

```python
def documents_cancel(self,
                         document_id,
                         reason)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| documentId |  ``` Required ```  | TODO: Add a parameter description |
| reason |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
document_id = uuid.uuid4()
reason = 'reason'

result = documents_controller.documents_cancel(document_id, reason)

```


### <a name="documents_update"></a>![Method: ](https://apidocs.io/img/method.png ".DocumentsController.documents_update") documents_update

> Update document

```python
def documents_update(self,
                         document_id,
                         request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| documentId |  ``` Required ```  | TODO: Add a parameter description |
| request |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
document_id = uuid.uuid4()
request = UpdateDocumentRequestWrapper()

result = documents_controller.documents_update(document_id, request)

```


### <a name="documents_get"></a>![Method: ](https://apidocs.io/img/method.png ".DocumentsController.documents_get") documents_get

> Retrieves details of a single document.

```python
def documents_get(self,
                      document_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| documentId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
document_id = uuid.uuid4()

result = documents_controller.documents_get(document_id)

```


### <a name="documents_create"></a>![Method: ](https://apidocs.io/img/method.png ".DocumentsController.documents_create") documents_create

> Creates a new document. In the response you will receive a document ID to retrieve info about the document at a later time. 
> 
> You also receive a URL and unique identifier per signer.

```python
def documents_create(self,
                         request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
request = CreateDocumentRequestWrapper()

result = documents_controller.documents_create(request)

```


### <a name="documents_get_collection"></a>![Method: ](https://apidocs.io/img/method.png ".DocumentsController.documents_get_collection") documents_get_collection

> Queries your documents using the provided parameters.

```python
def documents_get_collection(self,
                                 external_id=None,
                                 signer_id=None,
                                 external_signer_id=None,
                                 from_date=None,
                                 to_date=None,
                                 last_updated=None,
                                 signed_date=None,
                                 name_of_signer=None,
                                 title=None,
                                 status=None,
                                 tags=None,
                                 offset=None,
                                 limit=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| externalId |  ``` Optional ```  | Documents external id |
| signerId |  ``` Optional ```  | Signer Id |
| externalSignerId |  ``` Optional ```  | External signer Id |
| fromDate |  ``` Optional ```  | Documents created from date (ticks) |
| toDate |  ``` Optional ```  | Documents created to date (ticks) |
| lastUpdated |  ``` Optional ```  | Documents updated after this date (ticks) |
| signedDate |  ``` Optional ```  | Documents signed after this date (ticks) |
| nameOfSigner |  ``` Optional ```  | Name of signer |
| title |  ``` Optional ```  | TODO: Add a parameter description |
| status |  ``` Optional ```  | Document status |
| tags |  ``` Optional ```  | Document tags |
| offset |  ``` Optional ```  | Used for paging (will be automatically set in response links) |
| limit |  ``` Optional ```  | Set how many results you want per page (max/default 100) |



#### Example Usage

```python
external_id = 'externalId'
signer_id = uuid.uuid4()
external_signer_id = 'externalSignerId'
from_date = datetime.now()
to_date = datetime.now()
last_updated = datetime.now()
signed_date = datetime.now()
name_of_signer = 'nameOfSigner'
title = 'title'
status = Status329.ENUM_UNSIGNED
tags = 'tags'
offset = 124
limit = 124

result = documents_controller.documents_get_collection(external_id, signer_id, external_signer_id, from_date, to_date, last_updated, signed_date, name_of_signer, title, status, tags, offset, limit)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="attachments_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AttachmentsController") AttachmentsController

### Get controller instance

An instance of the ``` AttachmentsController ``` class can be accessed from the API Client.

```python
 attachments_controller = client.attachments
```

### <a name="attachments_update"></a>![Method: ](https://apidocs.io/img/method.png ".AttachmentsController.attachments_update") attachments_update

> Updates the specified attachment (Will only take affect if no one has signed the document yet)

```python
def attachments_update(self,
                           document_id,
                           attachment_id,
                           request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| documentId |  ``` Required ```  | TODO: Add a parameter description |
| attachmentId |  ``` Required ```  | TODO: Add a parameter description |
| request |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
document_id = uuid.uuid4()
attachment_id = uuid.uuid4()
request = UpdateAttachmentRequestWrapper()

result = attachments_controller.attachments_update(document_id, attachment_id, request)

```


### <a name="attachments_delete"></a>![Method: ](https://apidocs.io/img/method.png ".AttachmentsController.attachments_delete") attachments_delete

> Deletes the specified attachment (Will only take affect if no one has signed the document yet)

```python
def attachments_delete(self,
                           document_id,
                           attachment_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| documentId |  ``` Required ```  | TODO: Add a parameter description |
| attachmentId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
document_id = uuid.uuid4()
attachment_id = uuid.uuid4()

result = attachments_controller.attachments_delete(document_id, attachment_id)

```


### <a name="attachments_get"></a>![Method: ](https://apidocs.io/img/method.png ".AttachmentsController.attachments_get") attachments_get

> Retrieves the details of a single attachment.

```python
def attachments_get(self,
                        document_id,
                        attachment_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| documentId |  ``` Required ```  | TODO: Add a parameter description |
| attachmentId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
document_id = uuid.uuid4()
attachment_id = uuid.uuid4()

result = attachments_controller.attachments_get(document_id, attachment_id)

```


### <a name="attachments_create"></a>![Method: ](https://apidocs.io/img/method.png ".AttachmentsController.attachments_create") attachments_create

> Adds an attachments to the specified document. You can choose between different ways to make the user accept the attachment.
> 
>              <span style="color:red;">The attachment will be deleted when the signature job is completed or has expired</span>

```python
def attachments_create(self,
                           document_id,
                           request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| documentId |  ``` Required ```  | TODO: Add a parameter description |
| request |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
document_id = uuid.uuid4()
request = AttachmentRequestWrapper()

result = attachments_controller.attachments_create(document_id, request)

```


### <a name="attachments_list"></a>![Method: ](https://apidocs.io/img/method.png ".AttachmentsController.attachments_list") attachments_list

> Returns a list of all attachments for the specified document.

```python
def attachments_list(self,
                         document_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| documentId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
document_id = uuid.uuid4()

result = attachments_controller.attachments_list(document_id)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="signature_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SignatureController") SignatureController

### Get controller instance

An instance of the ``` SignatureController ``` class can be accessed from the API Client.

```python
 signature_controller = client.signature
```

### <a name="signature_get"></a>![Method: ](https://apidocs.io/img/method.png ".SignatureController.signature_get") signature_get

> Get a single transaction

```python
def signature_get(self,
                      transaction_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| transactionId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
transaction_id = uuid.uuid4()

result = signature_controller.signature_get(transaction_id)

```


### <a name="signature_sign"></a>![Method: ](https://apidocs.io/img/method.png ".SignatureController.signature_sign") signature_sign

> Create a merchant signature

```python
def signature_sign(self,
                       request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
request = SignRequest()

result = signature_controller.signature_sign(request)

```


### <a name="signature_list"></a>![Method: ](https://apidocs.io/img/method.png ".SignatureController.signature_list") signature_list

> Get a selection of transactions

```python
def signature_list(self,
                       oauth_client_id,
                       from_date=None,
                       to_date=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| oauthClientId |  ``` Required ```  | TODO: Add a parameter description |
| fromDate |  ``` Optional ```  | Date in ticks |
| toDate |  ``` Optional ```  | Date in ticks |



#### Example Usage

```python
oauth_client_id = 'oauthClientId'
from_date = 124
to_date = 124

result = signature_controller.signature_list(oauth_client_id, from_date, to_date)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="translations_controller"></a>![Class: ](https://apidocs.io/img/class.png ".TranslationsController") TranslationsController

### Get controller instance

An instance of the ``` TranslationsController ``` class can be accessed from the API Client.

```python
 translations_controller = client.translations
```

### <a name="list_translations"></a>![Method: ](https://apidocs.io/img/method.png ".TranslationsController.list_translations") list_translations

> *Tags:*  ``` Skips Authentication ``` 

> Returns a list of all your translations for the given language set.

```python
def list_translations(self,
                          language_set_id,
                          language=None,
                          format=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| languageSetId |  ``` Required ```  | TODO: Add a parameter description |
| language |  ``` Optional ```  | TODO: Add a parameter description |
| format |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
language_set_id = 124
language = 'language'
format = Format.NORMAL

result = translations_controller.list_translations(language_set_id, language, format)

```


### <a name="update_translation"></a>![Method: ](https://apidocs.io/img/method.png ".TranslationsController.update_translation") update_translation

> *Tags:*  ``` Skips Authentication ``` 

> Updates the specified translation with the parameters passed.

```python
def update_translation(self,
                           language_set_id,
                           id,
                           translation_update=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| languageSetId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |
| translationUpdate |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
language_set_id = 124
id = 124
translation_update = TranslationUpdateDTO()

translations_controller.update_translation(language_set_id, id, translation_update)

```


### <a name="retrieve_translation"></a>![Method: ](https://apidocs.io/img/method.png ".TranslationsController.retrieve_translation") retrieve_translation

> *Tags:*  ``` Skips Authentication ``` 

> Retrieves the details of a single translation.

```python
def retrieve_translation(self,
                             language_set_id,
                             id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| languageSetId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
language_set_id = 124
id = 124

result = translations_controller.retrieve_translation(language_set_id, id)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="template_controller"></a>![Class: ](https://apidocs.io/img/class.png ".TemplateController") TemplateController

### Get controller instance

An instance of the ``` TemplateController ``` class can be accessed from the API Client.

```python
 template_controller = client.template
```

### <a name="retrieve_data_source"></a>![Method: ](https://apidocs.io/img/method.png ".TemplateController.retrieve_data_source") retrieve_data_source

> *Tags:*  ``` Skips Authentication ``` 

> Preview the underlaying template datasource

```python
def retrieve_data_source(self,
                             model,
                             xml_tempalte=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| model |  ``` Required ```  | Preview model |
| xmlTempalte |  ``` Optional ```  | Prefilled XmlSignature templates |



#### Example Usage

```python
model = TemplatePreview()
xml_tempalte = XmlTempalte.SINGEL_BANKID_NO

result = template_controller.retrieve_data_source(model, xml_tempalte)

```


### <a name="preview_template_from_model"></a>![Method: ](https://apidocs.io/img/method.png ".TemplateController.preview_template_from_model") preview_template_from_model

> *Tags:*  ``` Skips Authentication ``` 

> Preview your PAdES template use your own signature file or choose the xmlTemplate prefilled

```python
def preview_template_from_model(self,
                                    model,
                                    xml_template=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| model |  ``` Required ```  | Preview model |
| xmlTemplate |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
model = TemplatePreview()
xml_template = XmlTemplate.SINGEL_BANKID_NO

template_controller.preview_template_from_model(model, xml_template)

```


### <a name="preview_template_from_id"></a>![Method: ](https://apidocs.io/img/method.png ".TemplateController.preview_template_from_id") preview_template_from_id

> *Tags:*  ``` Skips Authentication ``` 

> Preview your PAdES template use your own signature file or choose the xmlTemplate prefilled

```python
def preview_template_from_id(self,
                                 model,
                                 id,
                                 xml_template=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| model |  ``` Required ```  | Preview model |
| id |  ``` Required ```  | Template Id |
| xmlTemplate |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
model = TemplateWithIdPreview()
id = uuid.uuid4()
xml_template = XmlTemplate.SINGEL_BANKID_NO

template_controller.preview_template_from_id(model, id, xml_template)

```


### <a name="retrieve_default_coverpage_template"></a>![Method: ](https://apidocs.io/img/method.png ".TemplateController.retrieve_default_coverpage_template") retrieve_default_coverpage_template

> *Tags:*  ``` Skips Authentication ``` 

> Gets the HTML used as a template for the details page if not overridden by user

```python
def retrieve_default_coverpage_template(self)
```

#### Example Usage

```python

result = template_controller.retrieve_default_coverpage_template()

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="retrieve_default_details_template"></a>![Method: ](https://apidocs.io/img/method.png ".TemplateController.retrieve_default_details_template") retrieve_default_details_template

> *Tags:*  ``` Skips Authentication ``` 

> Gets the HTML used as a template for the details page if not overridden by user

```python
def retrieve_default_details_template(self,
                                          language)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| language |  ``` Required ```  | Language of the details page |



#### Example Usage

```python
language = Language185.EN

result = template_controller.retrieve_default_details_template(language)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="delete_template"></a>![Method: ](https://apidocs.io/img/method.png ".TemplateController.delete_template") delete_template

> *Tags:*  ``` Skips Authentication ``` 

> Deletes the PDF template

```python
def delete_template(self,
                        id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | The template ID |



#### Example Usage

```python
id = uuid.uuid4()

result = template_controller.delete_template(id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="update_template"></a>![Method: ](https://apidocs.io/img/method.png ".TemplateController.update_template") update_template

> *Tags:*  ``` Skips Authentication ``` 

> Updates the given PDF template

```python
def update_template(self,
                        id,
                        model)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | The template ID |
| model |  ``` Required ```  | The template body |



#### Example Usage

```python
id = uuid.uuid4()
model = UpdatePdfTemplate()

result = template_controller.update_template(id, model)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="retrieve_template"></a>![Method: ](https://apidocs.io/img/method.png ".TemplateController.retrieve_template") retrieve_template

> *Tags:*  ``` Skips Authentication ``` 

> Gets a PDF template

```python
def retrieve_template(self,
                          id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | The template ID |



#### Example Usage

```python
id = uuid.uuid4()

result = template_controller.retrieve_template(id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="create_template"></a>![Method: ](https://apidocs.io/img/method.png ".TemplateController.create_template") create_template

> *Tags:*  ``` Skips Authentication ``` 

> Creates a new PDF template

```python
def create_template(self,
                        model)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| model |  ``` Required ```  | Create PDF template body |



#### Example Usage

```python
model = CreatePdfTemplate()

result = template_controller.create_template(model)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="list_templates_for_account"></a>![Method: ](https://apidocs.io/img/method.png ".TemplateController.list_templates_for_account") list_templates_for_account

> *Tags:*  ``` Skips Authentication ``` 

> Lists all the PDF template for the account

```python
def list_templates_for_account(self)
```

#### Example Usage

```python

result = template_controller.list_templates_for_account()

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




[Back to List of Controllers](#list_of_controllers)

## <a name="open_id_controller"></a>![Class: ](https://apidocs.io/img/class.png ".OpenIDController") OpenIDController

### Get controller instance

An instance of the ``` OpenIDController ``` class can be accessed from the API Client.

```python
 open_id_controller = client.open_id
```

### <a name="create_openid_client"></a>![Method: ](https://apidocs.io/img/method.png ".OpenIDController.create_openid_client") create_openid_client

> Create a new openId client for the requested account. Requires on of the following scopes: [root]

```python
def create_openid_client(self,
                             client)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| client |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
client = CreateOpenIdClientRequest()

result = open_id_controller.create_openid_client(client)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="update_openid_client"></a>![Method: ](https://apidocs.io/img/method.png ".OpenIDController.update_openid_client") update_openid_client

> Updates the requested openid client on the requested account. Requires on of the following scopes: [dealer,  openid-client, root]

```python
def update_openid_client(self,
                             client)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| client |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
client = UpdateOpenIdClientRequest()

result = open_id_controller.update_openid_client(client)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="disable_openid_client"></a>![Method: ](https://apidocs.io/img/method.png ".OpenIDController.disable_openid_client") disable_openid_client

> Deactivates the requested oauth client. Requires on of the following scopes: [dealer,  openid-client, root]

```python
def disable_openid_client(self,
                              request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
request = OauthClientId()

result = open_id_controller.disable_openid_client(request)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="enable_openid_client"></a>![Method: ](https://apidocs.io/img/method.png ".OpenIDController.enable_openid_client") enable_openid_client

> Requires on of the following scopes: [dealer,  openid-client, root]

```python
def enable_openid_client(self,
                             request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
request = OauthClientId()

result = open_id_controller.enable_openid_client(request)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="list_openid_clients_for_account"></a>![Method: ](https://apidocs.io/img/method.png ".OpenIDController.list_openid_clients_for_account") list_openid_clients_for_account

> Returns a list of all oauth clients registered on requested account. Requires on of the following scopes: [dealer,  openid-client, root]

```python
def list_openid_clients_for_account(self)
```

#### Example Usage

```python

result = open_id_controller.list_openid_clients_for_account()

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="delete_openid_client"></a>![Method: ](https://apidocs.io/img/method.png ".OpenIDController.delete_openid_client") delete_openid_client

> Requires on of the following scopes: [dealer,  openid-client, root]

```python
def delete_openid_client(self,
                             client_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| clientId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
client_id = 'clientId'

result = open_id_controller.delete_openid_client(client_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="retrieve_openid_client"></a>![Method: ](https://apidocs.io/img/method.png ".OpenIDController.retrieve_openid_client") retrieve_openid_client

> Returns the requested oauth client with settings. Requires on of the following scopes: [dealer,  openid-client, root]

```python
def retrieve_openid_client(self,
                               client_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| clientId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
client_id = 'clientId'

result = open_id_controller.retrieve_openid_client(client_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




[Back to List of Controllers](#list_of_controllers)

## <a name="o_auth_api_client_controller"></a>![Class: ](https://apidocs.io/img/class.png ".OAuthAPIClientController") OAuthAPIClientController

### Get controller instance

An instance of the ``` OAuthAPIClientController ``` class can be accessed from the API Client.

```python
 o_auth_api_client_controller = client.o_auth_api_client
```

### <a name="create_oauth_client"></a>![Method: ](https://apidocs.io/img/method.png ".OAuthAPIClientController.create_oauth_client") create_oauth_client

> Create a new oauth api client for the requested account. Requires on of the following scopes: [dealer,  oauth-token, root]

```python
def create_oauth_client(self,
                            api_client)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| apiClient |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
api_client = CreateOauthAPIClientRequest()

result = o_auth_api_client_controller.create_oauth_client(api_client)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="update_oauth_client"></a>![Method: ](https://apidocs.io/img/method.png ".OAuthAPIClientController.update_oauth_client") update_oauth_client

> Updates the requested oauth client on the requested account. Requires on of the following scopes: [dealer,  oauth-token, root]

```python
def update_oauth_client(self,
                            api_client)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| apiClient |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
api_client = UpdateOauthAPIClientRequest()

result = o_auth_api_client_controller.update_oauth_client(api_client)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="disable_oauth_client"></a>![Method: ](https://apidocs.io/img/method.png ".OAuthAPIClientController.disable_oauth_client") disable_oauth_client

> Deactivates the requested oauth client. Requires on of the following scopes: [dealer,  oauth-token, root]

```python
def disable_oauth_client(self,
                             request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
request = OauthClientId()

result = o_auth_api_client_controller.disable_oauth_client(request)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="enable_oauth_client"></a>![Method: ](https://apidocs.io/img/method.png ".OAuthAPIClientController.enable_oauth_client") enable_oauth_client

> Activates the requested oauth client. Requires on of the following scopes: [dealer,  oauth-token, root]

```python
def enable_oauth_client(self,
                            request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
request = OauthClientId()

result = o_auth_api_client_controller.enable_oauth_client(request)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="list_oauth_clients"></a>![Method: ](https://apidocs.io/img/method.png ".OAuthAPIClientController.list_oauth_clients") list_oauth_clients

> Returns a list of all oauth clients registered on requested account. Requires on of the following scopes: [dealer,  oauth-token, root]

```python
def list_oauth_clients(self)
```

#### Example Usage

```python

result = o_auth_api_client_controller.list_oauth_clients()

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="delete_oauth_client"></a>![Method: ](https://apidocs.io/img/method.png ".OAuthAPIClientController.delete_oauth_client") delete_oauth_client

> Delete oauth API client.  Requires on of the following scopes: [dealer,  oauth-token, root]

```python
def delete_oauth_client(self,
                            client_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| clientId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
client_id = 'clientId'

result = o_auth_api_client_controller.delete_oauth_client(client_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="retrieve_oauth_client"></a>![Method: ](https://apidocs.io/img/method.png ".OAuthAPIClientController.retrieve_oauth_client") retrieve_oauth_client

> Returns the requested oauth client with settings. Requires on of the following scopes: [dealer,  oauth-token, root]

```python
def retrieve_oauth_client(self,
                              client_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| clientId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
client_id = 'clientId'

result = o_auth_api_client_controller.retrieve_oauth_client(client_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




[Back to List of Controllers](#list_of_controllers)

## <a name="dealer_controller"></a>![Class: ](https://apidocs.io/img/class.png ".DealerController") DealerController

### Get controller instance

An instance of the ``` DealerController ``` class can be accessed from the API Client.

```python
 dealer_controller = client.dealer
```

### <a name="update_dealer_logo"></a>![Method: ](https://apidocs.io/img/method.png ".DealerController.update_dealer_logo") update_dealer_logo

> *Tags:*  ``` Skips Authentication ``` 

> Set dealer Logo. Requires the following scope: [dealer]

```python
def update_dealer_logo(self,
                           dealer_id,
                           dealer_logo)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| dealerId |  ``` Required ```  | Your Idfy dealer ID |
| dealerLogo |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
dealer_id = uuid.uuid4()
dealer_logo = DealerLogo()

result = dealer_controller.update_dealer_logo(dealer_id, dealer_logo)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="list_accounts_for_dealer"></a>![Method: ](https://apidocs.io/img/method.png ".DealerController.list_accounts_for_dealer") list_accounts_for_dealer

> *Tags:*  ``` Skips Authentication ``` 

> Requires the following scope: [dealer-read]

```python
def list_accounts_for_dealer(self,
                                 dealer_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| dealerId |  ``` Required ```  | Your Idfy dealer ID |



#### Example Usage

```python
dealer_id = uuid.uuid4()

result = dealer_controller.list_accounts_for_dealer(dealer_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="update_dealer"></a>![Method: ](https://apidocs.io/img/method.png ".DealerController.update_dealer") update_dealer

> *Tags:*  ``` Skips Authentication ``` 

> Update dealer credentials. Requires the following scope: [dealer]

```python
def update_dealer(self,
                      dealer_id,
                      dealer)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| dealerId |  ``` Required ```  | Your Idfy dealer ID |
| dealer |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
dealer_id = uuid.uuid4()
dealer = Dealer()

result = dealer_controller.update_dealer(dealer_id, dealer)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




### <a name="retrieve_dealer"></a>![Method: ](https://apidocs.io/img/method.png ".DealerController.retrieve_dealer") retrieve_dealer

> *Tags:*  ``` Skips Authentication ``` 

> Requires the following scope: [dealer]

```python
def retrieve_dealer(self,
                        dealer_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| dealerId |  ``` Required ```  | Your Idfy dealer ID |



#### Example Usage

```python
dealer_id = uuid.uuid4()

result = dealer_controller.retrieve_dealer(dealer_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




[Back to List of Controllers](#list_of_controllers)

## <a name="mobile_info_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MobileInfoController") MobileInfoController

### Get controller instance

An instance of the ``` MobileInfoController ``` class can be accessed from the API Client.

```python
 mobile_info_controller = client.mobile_info
```

### <a name="mobile_info"></a>![Method: ](https://apidocs.io/img/method.png ".MobileInfoController.mobile_info") mobile_info

> With this enpoints a user can fill out a form with one click. Per now the user have to be a telenor customer to retrieve information from this endpoint.
> 
>            The url received here can be used in an iframe or a popupwindow, we will then deliever the user information with webmessageing.
> 
>            <br /><br />
> 
>            Flow:<br />
> 
>            1) Get url from this endpoint<br />
> 
>            2) Open a popup window or an iframe with this url as src<br />
> 
>            3) User authenticates and gives you permission to retrieve user information<br />
> 
>            4) User is redirected to the callback endpoint, we connect to the serviceprovider API and retrieves the information about the user<br />
> 
>            5) We use webmessaging so you can collect the information

```python
def mobile_info(self,
                    response_mode)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseMode |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
response_mode = ResponseMode.POPUP

result = mobile_info_controller.mobile_info(response_mode)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="norwegian_bank_id_controller"></a>![Class: ](https://apidocs.io/img/class.png ".NorwegianBankIDController") NorwegianBankIDController

### Get controller instance

An instance of the ``` NorwegianBankIDController ``` class can be accessed from the API Client.

```python
 norwegian_bank_id_controller = client.norwegian_bank_id
```

### <a name="no_bank_id_validation_parse_sdo"></a>![Method: ](https://apidocs.io/img/method.png ".NorwegianBankIDController.no_bank_id_validation_parse_sdo") no_bank_id_validation_parse_sdo

> *Tags:*  ``` Skips Authentication ``` 

> This service validates and parses the signatures on the SDOdata, to validate/parse the SDO we use the validation component from bankID norway. 
> 
> This endpoint parses the SDO to readable data and provides you with information about the signatures and document.

```python
def no_bank_id_validation_parse_sdo(self,
                                        request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
request = ParseSDORequest()

result = norwegian_bank_id_controller.no_bank_id_validation_parse_sdo(request)

```


### <a name="no_bank_id_validation_validate_sdo"></a>![Method: ](https://apidocs.io/img/method.png ".NorwegianBankIDController.no_bank_id_validation_validate_sdo") no_bank_id_validation_validate_sdo

> *Tags:*  ``` Skips Authentication ``` 

> This service validates the signatures on the SDOdata, to validate the SDO we use the validation component from BankID Norway. 
> 
> In this endpoint you can also include the data from the original document to validate that they matches the SDO data, the same goes for the signatures. (Ssn is only available if you have an account and validate-ssn scope)

```python
def no_bank_id_validation_validate_sdo(self,
                                           request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
request = ValidateSDORequest()

result = norwegian_bank_id_controller.no_bank_id_validation_validate_sdo(request)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="norwgian_bank_id_controller"></a>![Class: ](https://apidocs.io/img/class.png ".NorwgianBankIDController") NorwgianBankIDController

### Get controller instance

An instance of the ``` NorwgianBankIDController ``` class can be accessed from the API Client.

```python
 norwgian_bank_id_controller = client.norwgian_bank_id
```

### <a name="create_mobile_session"></a>![Method: ](https://apidocs.io/img/method.png ".NorwgianBankIDController.create_mobile_session") create_mobile_session

> Create a new BankID mobile session to start the identification process. Returns requestID and a merchant ref.
> 
> If the user do not have BankID mobile of have inputed inncorrect values the InvalidMobileNumberOrDateOfBirth will be returned as true
> 
> If there is an error the error code will be returned also.

```python
def create_mobile_session(self,
                              model)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| model |  ``` Required ```  | A request object |



#### Example Usage

```python
model = CreateBankIDMobileRequest()

result = norwgian_bank_id_controller.create_mobile_session(model)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request (One or more of the request properties are missing or are on a wrong format) |
| 401 | Not authorized |
| 500 | Internal server error (Miscellaneous) |




[Back to List of Controllers](#list_of_controllers)

## <a name="log_controller"></a>![Class: ](https://apidocs.io/img/class.png ".LogController") LogController

### Get controller instance

An instance of the ``` LogController ``` class can be accessed from the API Client.

```python
 log_controller = client.log
```

### <a name="retrieve_a_log_entry"></a>![Method: ](https://apidocs.io/img/method.png ".LogController.retrieve_a_log_entry") retrieve_a_log_entry

> Gets an historic identification session (older than 14 days)

```python
def retrieve_a_log_entry(self,
                             request_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| requestId |  ``` Required ```  | A request object |



#### Example Usage

```python
request_id = 'requestId'

result = log_controller.retrieve_a_log_entry(request_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 401 | Not authorized |
| 500 | Internal server error (Miscellaneous) |




### <a name="list_log_entries"></a>![Method: ](https://apidocs.io/img/method.png ".LogController.list_log_entries") list_log_entries

> Gets an  list of historic identification sessions (older than 14 days) by the filter below fetched the last 1000 with a link to next page

```python
def list_log_entries(self,
                         year,
                         month=None,
                         day=None,
                         status=None,
                         identity_provider_type=None,
                         external_id=None,
                         name=None,
                         skip=None,
                         page_size=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| year |  ``` Required ```  | The year to fetch the sessions from |
| month |  ``` Optional ```  | Optional: Filter on month |
| day |  ``` Optional ```  | Optional: Filter on day |
| status |  ``` Optional ```  | Optional: Filter on status |
| identityProviderType |  ``` Optional ```  | Optional: Filter on identity provider |
| externalId |  ``` Optional ```  | The merchants reference to the identification process |
| name |  ``` Optional ```  | Optional: Filter on the name of the user |
| skip |  ``` Optional ```  | Number of pages to skip |
| pageSize |  ``` Optional ```  | Number of results in each page (max 1000) |



#### Example Usage

```python
year = 174
month = 174
day = 174
status = Status.UNKNOWN
identity_provider_type = IdentityProviderType.UNKNOWN
external_id = 'externalId'
name = 'name'
skip = 174
page_size = 174

result = log_controller.list_log_entries(year, month, day, status, identity_provider_type, external_id, name, skip, page_size)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="identification_session_controller"></a>![Class: ](https://apidocs.io/img/class.png ".IdentificationSessionController") IdentificationSessionController

### Get controller instance

An instance of the ``` IdentificationSessionController ``` class can be accessed from the API Client.

```python
 identification_session_controller = client.identification_session
```

### <a name="invalidate_session"></a>![Method: ](https://apidocs.io/img/method.png ".IdentificationSessionController.invalidate_session") invalidate_session

> Invalidate the identification session to avoid using the same request twice. (remark: if the session is in error the session will not be invalidated)

```python
def invalidate_session(self,
                           value)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| value |  ``` Required ```  | A request object |



#### Example Usage

```python
value = InvalidateIdentificationRequest()

result = identification_session_controller.invalidate_session(value)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 401 | Not authorized |
| 500 | Internal server error (Miscellaneous) |




### <a name="is_session_done"></a>![Method: ](https://apidocs.io/img/method.png ".IdentificationSessionController.is_session_done") is_session_done

> Checks the status of the identification session, returns OK if complete

```python
def is_session_done(self,
                        request_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| requestId |  ``` Required ```  | The requestId returned in the creation of the request |



#### Example Usage

```python
request_id = 'requestId'

result = identification_session_controller.is_session_done(request_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 401 | Not authorized |
| 500 | Internal server error (Miscellaneous) |




### <a name="create_session"></a>![Method: ](https://apidocs.io/img/method.png ".IdentificationSessionController.create_session") create_session

> Creates a new identification session

```python
def create_session(self,
                       request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | A request object |



#### Example Usage

```python
request = CreateIdentificationRequest()

result = identification_session_controller.create_session(request)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request (One or more of the request properties are missing or are on a wrong format) |
| 401 | Not authorized |
| 500 | Internal server error (Miscellaneous) |




### <a name="retrieve_session_response"></a>![Method: ](https://apidocs.io/img/method.png ".IdentificationSessionController.retrieve_session_response") retrieve_session_response

> Gets the response of the identifaction session (status, name, unique identifier from e-Id, ssn (if allowed) and other metadata about the user)
> 
> REMARK: Only authenticate users when the identitication status is equal to SUCCESS.

```python
def retrieve_session_response(self,
                                  request_id,
                                  meta_data=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| requestId |  ``` Required ```  | The requestId returned in the creation of the session |
| metaData |  ``` Optional ```  | Should metadata be included in the response, only set to true if need (addons and user ceritifcate) |



#### Example Usage

```python
request_id = 'requestId'
meta_data = True

result = identification_session_controller.retrieve_session_response(request_id, meta_data)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 401 | Not authorized |
| 500 | Internal server error (Miscellaneous) |




[Back to List of Controllers](#list_of_controllers)

## <a name="webhooks_controller"></a>![Class: ](https://apidocs.io/img/class.png ".WebhooksController") WebhooksController

### Get controller instance

An instance of the ``` WebhooksController ``` class can be accessed from the API Client.

```python
 webhooks_controller = client.webhooks
```

### <a name="webhooks_get_webhook_deliveries"></a>![Method: ](https://apidocs.io/img/method.png ".WebhooksController.webhooks_get_webhook_deliveries") webhooks_get_webhook_deliveries

> Returns the 10 most recent delivery attempts for a single webhook.

```python
def webhooks_get_webhook_deliveries(self,
                                        id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
id = 174

result = webhooks_controller.webhooks_get_webhook_deliveries(id)

```


### <a name="webhooks_ping_webhook"></a>![Method: ](https://apidocs.io/img/method.png ".WebhooksController.webhooks_ping_webhook") webhooks_ping_webhook

> Triggers a ping event to be sent to the webhook.

```python
def webhooks_ping_webhook(self,
                              id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
id = 174

webhooks_controller.webhooks_ping_webhook(id)

```


### <a name="webhooks_create_webhook"></a>![Method: ](https://apidocs.io/img/method.png ".WebhooksController.webhooks_create_webhook") webhooks_create_webhook

> Creates a new webhook

```python
def webhooks_create_webhook(self,
                                new_webhook)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| newWebhook |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
new_webhook = WebhookCreateDto()

result = webhooks_controller.webhooks_create_webhook(new_webhook)

```


### <a name="webhooks_list_webhooks"></a>![Method: ](https://apidocs.io/img/method.png ".WebhooksController.webhooks_list_webhooks") webhooks_list_webhooks

> Returns a list of all your webhooks.

```python
def webhooks_list_webhooks(self)
```

#### Example Usage

```python

result = webhooks_controller.webhooks_list_webhooks()

```


### <a name="webhooks_update_webhook"></a>![Method: ](https://apidocs.io/img/method.png ".WebhooksController.webhooks_update_webhook") webhooks_update_webhook

> Updates the specifiedlast webhook with the parameters passed.
> 
> Any parameters not provided will be left unchanged.

```python
def webhooks_update_webhook(self,
                                id,
                                updated_webhook)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |
| updatedWebhook |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
id = 174
updated_webhook = WebhookUpdateDto()

result = webhooks_controller.webhooks_update_webhook(id, updated_webhook)

```


### <a name="webhooks_delete_webhook"></a>![Method: ](https://apidocs.io/img/method.png ".WebhooksController.webhooks_delete_webhook") webhooks_delete_webhook

> Deletes the specified webhook.

```python
def webhooks_delete_webhook(self,
                                id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
id = 174

webhooks_controller.webhooks_delete_webhook(id)

```


### <a name="webhooks_get_single_webhook"></a>![Method: ](https://apidocs.io/img/method.png ".WebhooksController.webhooks_get_single_webhook") webhooks_get_single_webhook

> Retrieves the details of a single webhook.

```python
def webhooks_get_single_webhook(self,
                                    id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
id = 174

result = webhooks_controller.webhooks_get_single_webhook(id)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="aml_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AmlController") AmlController

### Get controller instance

An instance of the ``` AmlController ``` class can be accessed from the API Client.

```python
 aml_controller = client.aml
```

### <a name="b_2_b_identify_and_screening_request"></a>![Method: ](https://apidocs.io/img/method.png ".AmlController.b_2_b_identify_and_screening_request") b_2_b_identify_and_screening_request

> Person screening with data enhancement enabled for nationalities where data enhancement is provided. For other nationalities the data enhancement will be skipped 
> 
> 
> 
> **Required fields**: Name with either birthDate or ssn.

```python
def b_2_b_identify_and_screening_request(self,
                                             name,
                                             ssn=None,
                                             birth_date=None,
                                             nationality=None,
                                             language=None,
                                             include_report=None,
                                             mode=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| name |  ``` Required ```  | Complete name of person.  (Order of first and last names is not significant.) |
| ssn |  ``` Optional ```  | National Identification number. SSN or Birthdate are REQUIRED (Se NationalId format) |
| birthDate |  ``` Optional ```  | Date of birth. SSN or Birthdate are REQUIRED (format: yyyyMMdd) |
| nationality |  ``` Optional ```  | Nationality of person (two letters ISO 3166 ) |
| language |  ``` Optional ```  | Language to use in response where applicable, optional. (two letters ISO 3166 ) |
| includeReport |  ``` Optional ```  | Create a PDF report with the data timestamp and sealed as future proof for the process. |
| mode |  ``` Optional ```  | What mode to use. When using identify and screening data enhancement is enabled for nationalities where data enhancement is provided. |



#### Example Usage

```python
name = 'name'
ssn = 'ssn'
birth_date = 'birthDate'
nationality = 'nationality'
language = 'language'
include_report = False
mode = Mode.SCREEN

result = aml_controller.b_2_b_identify_and_screening_request(name, ssn, birth_date, nationality, language, include_report, mode)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 401 | Not authorized |
| 404 | Not found |
| 500 | Internal Server Error (Miscellaneous) |




### <a name="b_2_c_identify_and_screening_request"></a>![Method: ](https://apidocs.io/img/method.png ".AmlController.b_2_c_identify_and_screening_request") b_2_c_identify_and_screening_request

> Person screening with data enhancement enabled for nationalities where data enhancement is provided. For other nationalities the data enhancement will be skipped 
> 
> 
> 
> **Required fields**: Name with either birthDate or ssn.

```python
def b_2_c_identify_and_screening_request(self,
                                             name,
                                             ssn=None,
                                             birth_date=None,
                                             nationality=None,
                                             language=None,
                                             include_report=None,
                                             mode=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| name |  ``` Required ```  | Complete name of person.  (Order of first and last names is not significant.) |
| ssn |  ``` Optional ```  | National Identification number. SSN or Birthdate are REQUIRED (Se NationalId format) |
| birthDate |  ``` Optional ```  | Date of birth. SSN or Birthdate are REQUIRED (format: yyyyMMdd) |
| nationality |  ``` Optional ```  | Nationality of person (two letters ISO 3166 ) |
| language |  ``` Optional ```  | Language to use in response where applicable, optional. (two letters ISO 3166 ) |
| includeReport |  ``` Optional ```  | Create a PDF report with the data timestamp and sealed as future proof for the process. |
| mode |  ``` Optional ```  | What mode to use. When using identify and screening data enhancement is enabled for nationalities where data enhancement is provided. |



#### Example Usage

```python
name = 'name'
ssn = 'ssn'
birth_date = 'birthDate'
nationality = 'nationality'
language = 'language'
include_report = False
mode = Mode.SCREEN

result = aml_controller.b_2_c_identify_and_screening_request(name, ssn, birth_date, nationality, language, include_report, mode)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 401 | Not authorized |
| 404 | Not found |
| 500 | Internal Server Error (Miscellaneous) |




[Back to List of Controllers](#list_of_controllers)

## <a name="invoice_controller"></a>![Class: ](https://apidocs.io/img/class.png ".InvoiceController") InvoiceController

### Get controller instance

An instance of the ``` InvoiceController ``` class can be accessed from the API Client.

```python
 invoice_controller = client.invoice
```

### <a name="list_account_transactions"></a>![Method: ](https://apidocs.io/img/method.png ".InvoiceController.list_account_transactions") list_account_transactions

> Returns a list of transactions for the requested account. Requires on of the following scopes: [dealer, account-read, root]

```python
def list_account_transactions(self,
                                  year,
                                  month=None,
                                  get_as_csv=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| year |  ``` Required ```  | Define a year |
| month |  ``` Optional ```  | Define a month (0 - 12), not required |
| getAsCsv |  ``` Optional ```  | If this is set to true a csv file is returned insted of transactionlist |



#### Example Usage

```python
year = 10
month = 10
get_as_csv = False

result = invoice_controller.list_account_transactions(year, month, get_as_csv)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad request |
| 403 | Forbidden (Access denied) |
| 500 | Internal server error |




[Back to List of Controllers](#list_of_controllers)



