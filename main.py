import urllib.request
import urllib.parse

key = 0 # The api key
action = 0 # action that you performing
 type = "json"

url = "http://api.broadcastify.com/audio/?a=feeds&type="+ type +"&key=" + key