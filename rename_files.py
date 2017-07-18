import os

def rename_files():
    #get file names from the OS
    file_list = os.listdir("/Users/mituljindal/Desktop/Python-Files/Udacity-Python-Course/prank") #save the names of files in a list
    print(file_list)
    cwd = os.getcwd() #save the current directory
    os.chdir("/Users/mituljindal/Desktop/Python-Files/Udacity-Python-Course/prank") #move to the directory containing files

    #for loop, rename each file
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789")) #rename the file
        print(file_name.translate(None, "1234567890")) #print the new names

    os.chdir(cwd) #change the directory back to the original

rename_files()
