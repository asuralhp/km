from func.find_report import find_word_in_files
from func.find_report_re import find_word_in_files_re
from func.csv_report import write_dicts_to_csv
from config import *


# result = find_word_in_files("![", "../static/", '.md')
# print(result)
# write_dicts_to_csv(result,"./report/output.csv")






result_re = find_word_in_files_re(word_pattern, "../static/", '.md')
# print(result_re)
write_dicts_to_csv(result_re,path_csv_out)


