import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from func.find_report_re import find_word_in_files_re
from func.csv_report import read_csv_to_listOfDict, write_dicts_to_csv
from config import *
import walk_image 


# find single word
# result = find_word_in_files("![", "../static/", '.md')
# print(result)
# write_dicts_to_csv(result,"./report/output.csv")




# find words with regex
result_re = find_word_in_files_re(word_pattern, "../static/", '.md')
write_dicts_to_csv(result_re,path_csv_out)




execFunc=walk_image.check_image_syntax
if km_walk_image:
    execFunc=walk_image.move_rename_static

listOfMatch = read_csv_to_listOfDict(path_csv_out)
walk_image.execute(listOfMatch,execFunc=execFunc)