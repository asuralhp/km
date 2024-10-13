import csv
import ast

def write_dicts_to_csv(data, csv_file):
    """
    Write a list of dictionaries to a CSV file.

    Parameters:
    data (list): A list of dictionaries to write.
    csv_file (str): The name of the CSV file to write to.
    """
    if not data:
        raise ValueError("The data list is empty.")

    with open(csv_file, mode='w', newline='') as file:
        # Create a DictWriter object
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        
        # Write the header
        writer.writeheader()
        
        # Write the rows
        writer.writerows(data)

    print(f'report written to {csv_file}')

# Example usage
def read_csv_to_listOfDict(csv_file):
    """Reads a CSV file and returns a list of dictionaries, converting specific string fields to lists."""
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        result = []
        for row in reader:
            # Convert 'found_words' from string to list if it exists in the row
            if 'found_words' in row:
                try:
                    row['found_words'] = ast.literal_eval(row['found_words'])
                except (ValueError, SyntaxError):
                    print(f"Error converting 'found_words' for row: {row}")
                    row['found_words'] = []  # Default to empty list if conversion fails
            result.append(row)
    return result


if __name__ == "__main__":
    path_out_csv = './example/example.csv'
    sample_data = [
        {'name': 'Alice', 'age': 30, 'city': 'New York'},
        {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
        {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
    ]
    
    write_dicts_to_csv(sample_data, path_out_csv)


    data = read_csv_to_listOfDict(path_out_csv)
    print(data)