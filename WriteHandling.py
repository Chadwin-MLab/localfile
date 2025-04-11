# Open a file for write and read w+

fp=open("Example.txt",'w+')

# OverWriting the "I Love Python" text to the file

fp.write("I Love Python")


# To append means adding to already existing text

fp=open("Example.txt",'a')

fp.write("Adding new text")

fp.close()



