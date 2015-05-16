import sys
import urllib.request
import json
#import request                                                    #I really liked request, but I generally prefer solutions that don't require non-standard libraries if possible.

if len(sys.argv) != 2:
    print("Program is envoked with the streamers name as a command line argument.")
    print(len(sys.argv))
    sys.exit()
streamer = sys.argv[1]
viewerendpoint = "https://api.twitch.tv/kraken/streams/" + streamer

try:
    resp = urllib.request.urlopen(viewerendpoint).read()           #resp = requests.get(viewerendpoint)
except urllib.error.URLError:                                      #except request.exceptions.ConnectionError:
    print("API access failed.")
    print("Make sure the Twitch account actually exists.")
    print("If you're sure it is, check your Internet connection and the API itself.")   
    sys.exit();
  
json = json.loads(resp.decode())                                   #json = resp.json()
    
try:
    numbviewers = json["stream"]["viewers"]
    streamer = json["stream"]["channel"]["display_name"]
    gameplaying = json["stream"]["channel"]["game"]
    status = json["stream"]["channel"]["status"]
    print(streamer + " is streaming " + gameplaying + " with " + str(numbviewers) + " viewers.")
    print(status)
except TypeError:
    print(streamer + " is not streaming right now.")
    


