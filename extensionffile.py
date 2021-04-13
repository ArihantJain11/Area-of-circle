filename = input("Input the Filename: ")
ext = filename.split(".")
if ext[1]=="py":
    print ("The extension of the file is : 'python'" )
else:
    print("Invalid Extension")
