import os
from config import *
from func.csv_report import read_csv_to_listOfDict
from func.create_folder import create_folder
from func.file_move import move_file_to_folder
from func.find_replace import replace_words_in_file
print("Execute : ", km_execute)
listOfMatch = read_csv_to_listOfDict(path_csv_out)

listOfFile = []
listOfPath = []
def execute(listOfMatch, listOfFile):
    for m in listOfMatch:
        parent_path = os.path.dirname(m['path'])
    # listOfPath.append(path)
        words = m['found_words']
        print('\n')
        print('Parent : ',parent_path)
        
        path_md = m['path']
        print(" For : ", path_md)
        
        for w in words:
            file_path = os.path.join(parent_path,w)
            file_move_path = os.path.join(parent_path,'static')
            new_w = os.path.join(create_folder_name,w)
            print('   Move From : ',file_path)
            print('     Move To Folder : ',file_move_path)
            print('   Word From :', w, 'To :',new_w)
            if km_execute:
                move_file_to_folder(file_path,file_move_path)
                replace_words_in_file(path_md,{w:new_w})
                print("execute!!")
                pass
            listOfFile.append(os.path.join(os.path.dirname(parent_path),w))


if __name__ == '__main__':
    execute(listOfMatch, listOfFile)
    


# print(listOfPath)

# for path in paths:
#     parent_dir = os.path.dirname(path)  # Get the parent directory
#     static_dir = os.path.join(parent_dir, 'static')  # Define the static folder path
    
#     # Create the "static" folder if it doesn't exist
#     os.makedirs(static_dir, exist_ok=True)
#     print(f'Created: {static_dir}')