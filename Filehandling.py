#Opening the file

fp=open("Example.txt",'r')

#Reading all the text from the files

print(fp.read())



#Reading the first 4 letter or bytes

print(fp.read(4))



#Reading one line

print(fp.readline())