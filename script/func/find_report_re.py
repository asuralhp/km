import os
import re
from .find_report import walk_directory



def find_word_in_files_re(pattern, directory, extension):
    """Find a specified word using regex in all files with the given extension within the directory."""
    results = []
    
    for file_path in walk_directory(directory, extension):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                contents = f.read()
                found_words = re.findall(pattern, contents)
                occurrences = len(found_words)
                if occurrences > 0:
                    results.append({
                        "time": occurrences,
                        "path": file_path,
                        "found_words": found_words
                    })
        except Exception as e:
            print(f'Could not read file {file_path}: {e}')
    
    return results

# Example usage
if __name__ == "__main__":
    # Define a regex pattern for the word you want to find
    word_pattern = r"\bnew_word\b"  # Example pattern, matches "new_word" as a whole word
    results = find_word_in_files_re(word_pattern, ".", '.md')
    print(results)