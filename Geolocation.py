import httplib2
import json
import sys



def getGeocodeLocation(inputString):
    google_api_key = "AIzaSyDF9zCSziOR1fMeEouclQvWC_pf2U9iLVU"
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%(locationString,google_api_key))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    if sys.version_info > (3,0):
        true_content = content.decode('utf-8')
    else:
        true_content = content
    result = json.loads(true_content)
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude,longitude)


response = getGeocodeLocation("Chicago, IL")
print (response)
