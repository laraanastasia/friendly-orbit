import tabulate
def AND (a,b):
    if a == True and b == True:
        return True
    elif a == True and b != True:
        return False
    elif a == False and b == False:
        return False
    elif a == False and b == True: 
        return False
table = [[1,1,1], [1,0,0], [0,1,0],[0,0,0]]
print(tabulate.tabulate(table))
    
print(AND(True,True))
