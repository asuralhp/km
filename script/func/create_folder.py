import os

def create_folder(name,path):
    try:
        final_path = os.path.join(path,name)
        os.makedirs(final_path, exist_ok=True)  # Create the directory and parents if needed
        print(f'Folder created at: {path}')
    except OSError as e:
        print(f'Error creating folder: {e}')
    return final_path

if __name__ == "__main__":
    name = 'static'
    path = '/Users/leolau/Documents/CODE/km/script/func'
    create_folder(name,path)