def search_api(token):
    http_obj = Http()
    url = "http://api.idealista.com/3.5/es/search?center=40.42938099999995,-3.7097526269835726&country=es&maxItems=50&numPage=1&distance=452&propertyType=bedrooms&operation=rent"
    headers = {'Authorization' : 'Bearer ' + token}
    resp, content = http_obj.request(url,method='POST',headers=headers)
    return content
