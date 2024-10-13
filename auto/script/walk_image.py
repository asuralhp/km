import os

from config import *
from func.csv_report import read_csv_to_listOfDict
from func.create_folder import create_folder
from func.file_move import move_file_to_folder
from func.find_replace import replace_words_in_file






def execute(listOfMatch,execFunc):
    found_count = 0
    for m in listOfMatch:
        parent_path = os.path.dirname(m['path'])

        

        words = m['found_words']
        
        path_md = m['path']
        isFound = False
        for w in words:
            # resolve for alt_name pattern
            res = execFunc(parent_path, path_md, w)
            if res:
                isFound =True
                found_count += 1
        if isFound:
            print(" In File : ", path_md)
            print('In Dir : ',parent_path)
            print('\n')
    print("Found Count : ", found_count)


def move_rename_static(parent_path, path_md, w):
    print('!!!!!',w)
    if type(w) == tuple:
        w = str(w[1])
    file_path = os.path.join(parent_path,w)
    file_move_path = os.path.join(parent_path,'static')
    new_w = os.path.join(create_folder_name,w)
    
    print('   Move From : ',file_path)
    print('     Move To Folder : ',file_move_path)
    print('   Word From :', w, 'To :',new_w)
    if km_execute:
        move_file_to_folder(file_path,file_move_path)
        replace_words_in_file(path_md,{w:new_w})
        print("Execute!!")
    return True

def check_image_syntax(parent_path, path_md, w):
    if len(w) != 2:
        print('word is not a pair')
        raise TypeError
    alt_w = w[0]
    path_w = os.path.splitext(os.path.basename(w[1]))[0]
    if alt_w != path_w:
        print('     Alt Name: ',alt_w, ', Base Path : ', path_w)
        return True
    else:
        return False

if __name__ == '__main__':
    listOfMatch = read_csv_to_listOfDict(path_csv_out)
    execute(listOfMatch,execFunc=check_image_syntax)
    
