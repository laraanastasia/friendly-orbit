import json
class Jokes:
    def __init__(self, Joke, JID):
        self.Joke=Joke
        self.JID=JID

#f= open('jokes.json')
#entries = json.load(f)

#for i in entries:
  #  print(i)

#f.close()    

##with open("jokes.json","r") as file:
   # data=json.load(file)
##date=data["data"]["date"]
##jokes_data= data["data"]["jokes_data"]
##print(f"{date}:{jokes_data}")
jokesList = []
with open('jokes.json')as f:
    for jsonObj in f:
        jokeDict = json.loads(jsonObj)
        jokesList.append(jokeDict)
print(jokesList)




##import tabulate
##import random
##table = [ ["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"]]
##print(tabulate.tabulate(table,tablefmt='fancy_grid'))
##Ausdrücke = [[["So könnte auch eine Frage in der Klausur aussehen"],["Gifs werden verschickt"],["Alex bricht sich den Nacken"],["Nico lacht"]],[["Herr und Frau Lammarsch verbessern sich passiv agressiv gegenseitig"],["Lara fragt alle sich zu wiederholen"],["Pascal programmiert in jeder Vorlesung außer in Programmieren 1"],["Jannik und Alex spielen Schach"]],[["Javacode wird für mind. 20 min erklärt"],["Sitzplatzkrieg"],[""],["1"]],[["1"],["1"],["1"],["1"]],[["1"],["1"],["1"],["1"]],[["1"],["1"],["1"],["1"]]]
##list=[]
##for i in range(5):
 ##   numer = random.choice(Ausdrücke)
 ##   list.append(numer)
##print(tabulate.tabulate(list,tablefmt="grid"))


