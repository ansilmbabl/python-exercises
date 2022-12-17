n=5

#square
for i in range(n):
  for j in range(n):
    print("*", end=" ")
   print()
  
#increasing triangle
for i in range(n):
  for j in range(i+1):
    print("*", end=" ")
   print()
  
#decreasing triangle
for i in range(n):
  for j in range(i,n):
    print("*", end=" ")
   print()
  
#right sided triangle
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
    
#right sided inverted triangle
for i in range(n):
  for j in range(i):
    print(" ",end=" ")
  for j in range(n-i):
    print("*",end=" ")
  print()
  
#hill pattern
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
    
#eeverse hill pattern
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i-1):
        print("*",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()

#diamond pattern
for i in range(n-1):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
    
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i-1):
        print("*",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()
