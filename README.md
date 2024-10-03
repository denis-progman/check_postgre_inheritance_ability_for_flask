## Main API

#### To launch:
> - `$cp .env.example .env`
> - `$make up`

---
###### type `$make help` to see all the commands.

### sending data from front to back:
> request type - POST
> url - http://10.0.2.2:8888/user_auth
> JSON:
```
{
"serverAuthCode": "13216596816513854168"
}
```
### request's header:
```
'X-Requested-With': 387b562fefe45de2b573114a868a64a2335062f784bc1cfccae4da1fee85ea80,
```
### sending response from back to front:
> As the response the object will be send.
Response object includes user's data:
```
{
 "user": {
  "avatar": null,
  "created_at": "Thu, 27 Jun 2024 01:01:33 GMT",
  "google_id": "106474395490511024966",
  "id": 7,
  "login": null,
  "middle_name": null,
  "type": "users",
  "updated_at": "Thu, 27 Jun 2024 01:01:33 GMT",
  "user_name": "Anton Potapov"
 }
}
```
Response headers include:
```
 X-Requested-With: 387b562fefe45de2b573114a868a64a2335062f784bc1cfccae4da1fee85ea80,
 Content-Type: application/json,
 Session_Status: 1fecd8a930804ca98a819a824d59ecd3fed2a7801deac8fbc4d828de04deb0c6
```
