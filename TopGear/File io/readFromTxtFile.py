f1 = open("E:\python programs\data.txt","r")
#file1 = open("E:\python programs\data_file.txt","w+")

user_input = "Enter something to data_file.txt :\n"






#for writing into file
with open("E:\python programs\data_file.txt","w+") as f :
    f.write(user_input)
    print(f.read())


for i in f1:
    print(i,end="")
print("\n\n")

#for reading
with open("E:\python programs\data_file.txt","r") as f :
    print(f.read())


print("\n\n")

#for append mode
with open("E:\python programs\data_file.txt","a") as f :
    f.write("Hello i am ankit ! Please dont disturb . <3")

with open("E:\python programs\data_file.txt", "r") as file2:
    for line in file2:
        print(line,end="")