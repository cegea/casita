def get_oauth_token():
    http_obj = Http()
    
    
    url = "https://api.idealista.com/oauth/token"
    apikey= urllib.parse.quote_plus('Provided_API_key')
    secret= urllib.parse.quote_plus('Provided_API_secret')
    auth = base64.encode(apikey + ':' + secret)
    body = {'grant_type':'client_credentials'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8','Authorization' : 'Basic ' + auth}
    resp, content = http_obj.request(url,method='POST',headers=headers, body=urllib.parse.urlencode(body))
    return content
