##size=14
##for i in range (size):
  ##  for j in range(size):
    ##    if j < size - i or j >= size + i:
      ##    print(" ",end="")
        ##else:
          ## print("x ",end="")
##print()


size = 11

for i in range(size):
    for j in range(size + i):
        if j <= size - i or j >= size + i:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
    

    
