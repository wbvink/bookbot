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

def dict_char_count_sort_helper(items: dict) -> int:
    """Helper function to sort_char_count: takes a dictionary and returns the value of the "num" key
    """
    return items["num"]

def sort_char_count(input_dict:dict) -> list:
    """Convert input-dictionary of character counts to list of dictionaries sorted in descending order of occurrence
    Input: dictionary with character:occurrences format, e.g. {'p': 6121, 'r': 20818, 'o': 25225, ...
    Output: list of dictionaries where each dict has this format: {"char": "b", "num": 4868}
    """
    output_list = [] # initiate empty list
    # Translate to new format
    for ch in input_dict:
        output_list.append({"char":ch, "num":input_dict.get(ch)})
    # Sort to descending occurrence order
    output_list.sort(reverse=True, key=dict_char_count_sort_helper)
    return output_list
