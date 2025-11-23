def wordcount(input_string: str) -> int:
    """Count number of words in input string"""
    wordlist = input_string.split() # use standard 'smart' sep
    return len(wordlist) 

def char_count(input_string:str) -> dict:
    """Convert characters to lower case and count occurrence of each character"""
    # Preparation:
    lc_string = input_string.lower() # convert to lower case
    output_dict = {}
    # Find all unique characters
    unique_char = set(lc_string) 
    # Fill dictionary
    for ch in unique_char:
        output_dict[ch] = lc_string.count(ch) # start with 1 for debugging 

    return output_dict