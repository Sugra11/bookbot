def main():
    # Path to the file relative to the root of the project
    file_path = 'books/frankenstein.txt'
    
    try:
        # Open the file using a with block
        with open(file_path, 'r') as f:
            # Read the contents of the file into a string
            file_contents = f.read()
            
            # Count the number of words in the file content
            word_count = count_words(file_contents)
            
            # Count the occurrences of each character in the file content
            char_count = count_characters(file_contents)
            
            # Print the report
            print_report(file_path, word_count, char_count)
    
    except FileNotFoundError:
        print("The file {} was not found.".format(file_path))
    
    except IOError:
        print("An error occurred while reading the file {}.".format(file_path))

def count_words(text):
    """
    Count the number of words in a given text.
    """
    words = text.split()
    return len(words)

def count_characters(text):
    """
    Count the number of occurrences of each character in the given text.
    """
    text = text.lower()
    char_count = {}
    
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

def print_report(file_path, word_count, char_count):
    """
    Print a formatted report of word and character counts.
    """
    # Start the report
    print(f"\n--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    
    # Convert character count dictionary to a list of tuples and sort it
    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    
    # Print each character and its frequency
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")
    
    # End the report
    print("--- End report ---")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
