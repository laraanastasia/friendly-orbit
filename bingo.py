import tabulate
import random
table = [ ["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"]]
print(tabulate.tabulate(table,tablefmt='fancy_grid'))
Ausdrücke = [[["So könnte auch eine Frage in der Klausur aussehen"],["Gifs werden verschickt"],["Alex bricht sich den Nacken"],["Nico lacht"]],[["Herr und Frau Lammarsch verbessern sich passiv agressiv gegenseitig"],["Lara fragt alle sich zu wiederholen"],["Pascal programmiert in jeder Vorlesung außer in Programmieren 1"],["Jannik und Alex spielen Schach"]],[["Javacode wird für mind. 20 min erklärt"],["Sitzplatzkrieg"],[""],["1"]],[["1"],["1"],["1"],["1"]],[["1"],["1"],["1"],["1"]],[["1"],["1"],["1"],["1"]]]
list=[]
for i in range(5):
    numer = random.choice(Ausdrücke)
    list.append(numer)
print(tabulate.tabulate(list,tablefmt="grid"))

