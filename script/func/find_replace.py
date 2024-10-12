def replace_words_in_file(file_path, words_to_replace):
    """
    Replaces specified words in a file with new words.

    Parameters:
    - file_path: str, path to the file to be modified
    - words_to_replace: dict, a dictionary where keys are words to find and values are the replacements
    """
    # Step 1: Read the file
    with open(file_path, 'r') as file:
        content = file.read()

    # print("Original content:")
    # print(content)

    # Step 2: Replace the words
    for old_word, new_word in words_to_replace.items():
        content = content.replace(old_word, new_word)

    # Step 3: Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

    # print("Words replaced successfully!")

if __name__ == "__main__":
    # Example usage
    file_path = 'example.md'
    words_to_replace = {
        'new_word1': 'new_word11',
        'new_word2': 'new_word22'
    }

    replace_words_in_file(file_path, words_to_replace)