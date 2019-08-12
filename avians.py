from playsound import playsound
from PIL import Image

bigBirdDict = {}
birds = ["robin", "tuftedTitmouse"]

for bird in birds:
  birdDict = {}
  birdDict["pic"] = bird + ".jpg"
  birdDict["call"] = bird + "Call.mp3"
  birdDict["song"] = bird + "Song.mp3"
  bigBirdDict[bird] = birdDict

print("Learn or practice?")
choice = input().lower()
if choice == 'learn':
    print("Not ready yet")
else:
    playsound(bigBirdDict['tuftedTitmouse']['song'])
    print("Which bird? (1 or 2)")
    print("1. Tufted Titmouse")
    print("2. Robin")
    choice = input().lower()
    if choice == "1":
        print("Right!")
    else: 
        print("Wrong!")

