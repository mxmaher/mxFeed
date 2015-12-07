#mxFeed
=====

Display your Facebook Newsfeed in the Terminal

Notes:
  * You will need to get an AppID and AppSecret from Facebook
    and store them in a json file 'app.json' for authenticating with the graphAPI

  * I haven't included my _app.json_ file in this repository
    for security issues
    but it looks like this

  ```{
      "appsecret": "put your AppSecret here",
      "appid": "put your AppID here",
      "access_token": ""
  }```

#Usage example:

  * `mxfeed -sf`
     prints the full retrived Newsfeed and saves it for future viewing

  * `mxfeed -lf`
    prints the previously saved Newsfeed

  * `mxfeed -lp 1`
   prints the first post in the saved Newsfeed

  * `mxfeed -lo 1`
   opens the first post link in the browser

  * `mxfeed -t`
   get an access_token from Facebook

#screenshot:

![screenshot](/screenshots/UsageExample.png)
