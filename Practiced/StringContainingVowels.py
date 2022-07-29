str = input("Ente a string :")
#ctr=0
l1  = list(str.split(" "))
print(l1)
l2 = list("aeiou")
#i=0

for i in l1:
    for j in i:
        if j not in l2:
            print(i,"is not accepted ")
            break
    else:
        print(i," accepted")
        
        
#print(l2)   