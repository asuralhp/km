# path_csv_out = "./report/find_name.csv"
# word_pattern = r'!\[([^]]*)\]\((?!http)([^)]+)\)'

import os


km_execute = False
km_execute = bool(int(os.environ.get('km_execute')))

create_folder_name = 'static'
path_csv_out = "./report/find.csv"
word_pattern = r'!(?:(?!a)[^]]*)]\((?!http)([^)\s]+\.[^)\s]+)\)'