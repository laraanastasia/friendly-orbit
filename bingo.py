import tabulate
table = [["1", "2","3","4","5"], ["1"],["1"],["1"],["1"],]
print(tabulate.tabulate(table,tablefmt="grid"))