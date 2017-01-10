import httplib2
import json

def getGeocodeLocation(inputString):
    google_api_key = "AIzaSyDF9zCSziOR1fMeEouclQvWC_pf2U9iLVU"
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%(locationString,google_api_key))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = ['results'][0]['geometry']['location']['lng']
    return (latitude,longitude)
