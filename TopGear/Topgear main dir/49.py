myfile = open("output.txt", "r")
print(myfile.read())
myfile.close()

myfile = open("sample.txt", "w")
myfile.write(" Ankit")
myfile.write("working on python")
myfile.write("Hello  ")
myfile.write("How are you ?")
myfile.write("Wipro topgear")
myfile.close()

myfile = open("output.txt", "a")
myfile.write(" Ankit")
myfile.write("working on python")
myfile.write("Hello  ")
myfile.write("How are you ?")
myfile.write("Wipro topgear")
myfile.close()


