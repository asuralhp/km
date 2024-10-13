import os
import sys
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))


current_dir_path = os.path.dirname(os.path.abspath(__file__))
report_path = os.path.join(current_dir_path,'report')

km_execute = False
km_execute = bool(int(os.environ.get('km_execute',0)))
km_walk_image = bool(int(os.environ.get('km_walk_image',0)))
create_folder_name = 'static'

report_pattern='include_alt_name'
if km_walk_image:
    report_pattern='image_path'

    
    
# ![alt_name](image_path)
match report_pattern:
    case 'image_path':
        path_csv_out = os.path.join(report_path,"find.csv")
        word_pattern = r'!(?:(?!a)[^]]*)]\((?!http)([^)\s]+\.[^)\s]+)\)'
    case 'include_alt_name':
        path_csv_out = os.path.join(report_path,"find_name.csv")
        word_pattern = r'!\[([^]]*)\]\((?!http)([^)]+)\)'
    case _:
        pass
    
if __name__ == '__main__':
    print(current_dir_path)
