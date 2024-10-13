import os
import shutil

def move_file_to_folder(file_path, tar_path):

    try:
        # Ensure the target directory exists
        os.makedirs(tar_path, exist_ok=True)
        
        # Move the file
        shutil.move(file_path, tar_path)
        # print(f'File moved to: tar_path')
    except FileNotFoundError:
        print(f'Error: The file {file_path} does not exist.')
    except PermissionError:
        print(f'Error: Permission denied when trying to move {file_path}.')
    except Exception as e:
        print(f'Error moving file: {e}')

if __name__ == '__main__':
    # Example usage
    # You can replace these paths with actual paths for testing
    file_to_move = '/Users/leolau/Documents/CODE/km copy/script/func/XaaS.png'
    target_folder = '/Users/leolau/Documents/CODE/km copy/script/func/test'
    
    move_file_to_folder(file_to_move, target_folder)