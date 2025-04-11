# File Handling 

- Sometime we need to store and retrieve data from somewhere else, rather than variables and available data structures.

- Named locations on disks.

- Can be any type such as txt, csv and more.

# *Steps when we work with files in python*

- Opening the file{

    We use a open() function to open a file.

    The syntax:

    file_object=open(file_name,access_mode)

    Access modes, define the operations that can be performed on this file

    Write mode:
    - w
    - wb
    - w+


    Read mode:
    - r-opens the file in read-only mode.
    - rb-opens the file for reading only in binary format.
    - r+-Opens the file for both reading and writing

    Append mode:
    -It means to add not overwrite what is existing as in the write mode.
    - a
    - ab
    - a+

}

- Performing the action(Writing or reading)

1.Once the file is opened for reading. We need to read the contents of the file.
2.These are the methods for reading the contents:

-read()-reads a string from an open file.

-read(size)-This accepts the parameter as the size.

-readline()-reads one single line of the file at a time.

-readlines()-reads all the lines

code example{
    fp=open("python.txt",'r')
    print(fp.read())
}


- Writing to a file

-Once we have opened the file the next step is to write to the file.
-We use the write() function.

code example{
    fp=open("textfile.txt".'w')
    fp.write("Add whatever to the file")
}

- Closing the file

-We use the close()method that flushes any unwritten information and closes the file object.

code example{
    fp.open("text.txt",'r')
    print(fp.read())
    fp.close()

}

