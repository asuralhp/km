import os

def walk_directory(directory, extension):
    """Walk through the directory and yield absolute paths of files with the specified extension."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                # Yield the absolute path of the file
                yield os.path.abspath(os.path.join(root, file))

def find_word_in_files(word, directory, extension):
    """Find a specified word in all files with the given extension within the directory."""
    results = []

    
    for file_path in walk_directory(directory, extension):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                contents = f.read()
                occurrences = contents.count(word)
                if occurrences > 0:
                    results.append({"time": occurrences, "path": file_path})
        except Exception as e:
            print(f'Could not read file {file_path}: {e}')
    
    return results



# Example usage
if __name__ == "__main__":
    results = find_word_in_files("new_word", ".", '.md')
    print(results)
