# To do: 
# - set up as repo
# - try to set it up with something like js `this`, so I can just do something like `var Robin = new bird(Robin)`, with the other necessary stuff. Or maybe there's a more pythonic? way to do this, with a list of birds, and a for loop.
# - put the calls in a list, so that I can iterate through them even if I don't know the size. 
# - figure out a way to close the image; might involve opening it in a better way. (Call through web browser, using import webbrowser//webbrowser.open('pathToFile')) - (nope; have to use Selenium, probably, which might add more complexity than it's worth.)

from playsound import playsound
from PIL import Image

yellow_warbler={}
yellow_warbler.pic="./yellowWarbler.jpg"
yellow_warbler.call1="./yellowWarbler1.mp3"

playsound(yellow_warbler['call1'])

image = Image.open(yellow_warbler['pic'])
image.show()
# Testing stuff, above

# Libraries

# def createBird(name):
#     name = {
#         "image" : "./{name}.jpg", 
#         "call" : "./{name}.mp3"
#     }

# TRY NEXT: 
birdList = ["robin", "catbird", "titmouse"]
for x in birdList:
    {x}Bird = {
        "image" : "./{x}.jpg"
        "call" : "./{x}.mp3"
    }
print(robinBird)
print(catbirdBird)
# (Didn't work. :( )

# Works 

chippingSparrow = {
    "image" : "chippingSparrow.jpg", 
    "call": "chipping1.mp3"
}


print("Practice?")
input = input()



# From Josh: 

Or, you could put all of those in a larger outer dictionary, like this:

bigBirdDict = {}
birds = ["robin", "catbird", "yellowWarbler", ...]

for bird in birds:
  birdDict = {}
  birdDict["pic"] = bird + ".jpg"
  birdDict["call"] = bird + "Call.mp3"
  birdDict["song"] = bird + "Song.mp3"
  bigBirdDict[bird] = birdDict