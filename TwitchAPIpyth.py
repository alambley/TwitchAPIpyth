#!/usr/bin/python3

import sys
import urllib.request
import json
import os

def main():

  os.chdir(os.path.dirname(os.path.realpath(__file__)))

  clientID = ""

  if os.path.isfile("clientkey.txt"):
    clientID = fileToString("clientkey.txt").replace("\n","").strip()
  else:
    print("Twitch API now requires you to register your app to access the API")
    print("https://dev.twitch.tv/docs/api")
    print("Add your Client-ID to a text file called 'clientkey.txt' in the same dir as this script")

  if len(sys.argv) != 2:
    print("Program is envoked with the streamers name as a command line argument.")
    sys.exit()
  streamer = sys.argv[1]
  viewerendpoint = "https://api.twitch.tv/kraken/streams/" + streamer

  try:
    request = urllib.request.Request(viewerendpoint,data=None,headers={"Client-ID" : clientID})
    resp = urllib.request.urlopen(request).read()
  except urllib.error.URLError as e:
    print("API access failed ({0})".format(e))

    sys.exit();

  jsonResp = json.loads(resp.decode())

  try:
    numbviewers = jsonResp["stream"]["viewers"]
    streamer = jsonResp["stream"]["channel"]["display_name"]
    gameplaying = jsonResp["stream"]["channel"]["game"]
    status = jsonResp["stream"]["channel"]["status"]
    print(streamer + " is streaming " + gameplaying + " with " + str(numbviewers) + " viewers.")
    print(status)
  except TypeError:
    print(streamer + " is not streaming right now or doesn't exist.")

def fileToString(path):
  with open(path,"r") as f:
    return f.read()

if __name__ == "__main__":
  main()


