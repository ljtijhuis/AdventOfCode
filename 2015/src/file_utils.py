import os.path

def read_file(relative_path):
    #open text file in read mode
    text_file = open(os.path.dirname(__file__) + relative_path, "r")
 
    #read whole file to a string
    data = text_file.read()
    
    #close file
    text_file.close()

    return data