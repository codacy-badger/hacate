import urllib.request
import urllib.parse

key = 0 # The api key
action = 0 # action that you performing most of the time feeds
type = "json"

url = "http://api.broadcastify.com/audio/?"+ action +"=feeds&type="+ type +"&key=" + key

