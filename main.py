import urllib.request
import urllib.parse

key = 0 # The api key
action = 0 # action that you performing most of the time feeds


def urlgetter(action,key):
    url = "http://api.broadcastify.com/audio/?"+ action +"=feeds&type=type&key=" + key

    contents = urllib.request.urlopen(url).read()
    return contents

urlgetter(action,key)

