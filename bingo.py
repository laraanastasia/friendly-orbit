import tabulate
import random
table = [ ["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"]]
print(tabulate.tabulate(table,tablefmt="grid"))
Ausdrücke = [["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["2"],["3"],["4"],]
list=[]
for i in range(5):
    numer = random.choice(Ausdrücke)
    list.append(numer)
print(tabulate.tabulate(list,tablefmt="grid"))

