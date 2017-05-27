# xblock-mediasite-credentials
The [edX XBlock for a mediasite server](../../../xblock-mediasite/blob/master/README.md) needs credentials to access the mediasite API. Install this software on a separate server and allow access through a whitelist in /etc/mediasite.conf.

### Example /etc/mediasite.conf
[mediasite_url_1]<br/>
username: API_username_for_this_server<br/>
password: password_for_this_server<br/>
apikey: api_key_for_this_server<br/>
token_life_time: when using a token, this is the lifetime in minutes<br/>
origin_whitelist: ip numbers and/or ip ranges for getting credentials, separated by comma<br/>

##### Optional: more servers
[mediasite_url_2]<br/>
username: API_username_for_this_server<br/>
password: password_for_this_server<br/>
apikey: api_key_for_this_server<br/>
token_life_time: when using a token, this is the lifetime in minutes<br/>

The most obvious place to get a key for the API is https://<mediasite_server>/mediasite/api/Docs/ApiKeyRegistration.aspx but ask your local mediasite-administrator for the right procedure, including getting a username and password.
