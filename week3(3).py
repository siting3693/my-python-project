#FILE HANDLING
#File Open

'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
'''

'''
"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
'''

f = open("filehandling.txt","at")
f.close()

f = open("filehandling.txt","rt")      #open(filename, modes)
#same as f = open("filehandling.txt")
f.close()

f = open(r"C:\Users\HP\Documents\Siting\physics engine\Folder A\file_a.txt", "rt")   #specify the file path if it is located in a different location   (need add r before " because \ is an escape character)
print(f.read())     #print content in file
f.close()

#or
with open("filehandling.txt") as f:        #using with to open file no need to write close to close file
  print(f.read())

with open("filehandling.txt") as f:
  print(f.read(5))

with open("filehandling.txt") as f:
  print(f.readline())
  print(f.readline())   #read first two lines

with open("filehandling.txt") as f:
  for x in f:           #read the whole file line by line
    print(x)



#Write
with open("filehandling.txt", "a") as f:
  f.write("Now the file has more content!")   #append

with open("filehandling.txt") as f:
  print(f.read())

with open("demofile.txt", "w") as f:          #overwrite
  f.write("Woops! I have deleted the content!")

with open("demofile.txt") as f:
  print(f.read())



import os
os.remove("filehandling.txt")    #delete file

if os.path.exists("filehandling.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#os.rmdir("myfolder")     #remove folder (can only remove empty folders)
