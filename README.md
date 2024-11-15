## Main API

#### To launch:
> - `$cp .env.example .env`
> - `$make up`

---
###### type `$make help` to see all the commands.

## Authorisation via Google service:
### Sending data from front to back:
> request type - POST
> url - http://10.0.2.2:8888/user_auth
> JSON:
```
{
"serverAuthCode": "13216596816513854168"
}
```
### Request's header:
```
'X-Requested-With': 387b562fefe45de2b573114a868a64a2335062f784bc1cfccae4da1fee85ea80,
```
### sending response from back to front:
Response headers contain:
```
 X-Requested-With: 387b562fefe45de2b573114a868a64a2335062f784bc1cfccae4da1fee85ea80,
 Content-Type: application/json
```
> The response contains message and status code:
```
"message: The user just has been created. Login is required"
```
```
status_code - 401
```
> Trying register again without a login, the response will contain:
```
"message: The required field Login is empty"
```
```
status_code - 401
```

## Registration via Google service:
### Sending data from front to back:
> request type - POST
> url - http://10.0.2.2:8888/register_user
> JSON:
```
{
"login": "Username"
"serverAuthCode": "13216596816513854168"
}
```
### Request's header:
```
'X-Requested-With': 387b562fefe45de2b573114a868a64a2335062f784bc1cfccae4da1fee85ea80,
```
### sending response from back to front:
Response headers contain:
```
 X-Requested-With: 387b562fefe45de2b573114a868a64a2335062f784bc1cfccae4da1fee85ea80,
 Content-Type: application/json
```
> The response contains User's data and status code:
```
Response Body: {
   "session_token": "04146e93ecd2cd831c3a73049e09c4e906d59527d4b21b9523e722368fc73b66",
   "user": {
     "avatar": null,
     "created_at": "Thu, 14 Nov 2024 00:43:19 GMT",
     "google_id": "106474395490511024966",
     "id": 12,
     "login": "Username",
     "middle_name": null,
     "type": "users",
     "updated_at": "Thu, 14 Nov 2024 00:43:36 GMT",
     "user_name": "Anton Potapov"
   }
 }
```
```
status_code - 200
```
> In case when the user try input the login shorter than 3 symbols the response will contain:
```
"message: It must be at least 3 characters long."
```
```
status_code - 400
```
