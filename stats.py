def wordcount(input_string: str) -> int:
    """Count number of words in input string"""
    wordlist = input_string.split() # use standard 'smart' sep
    return len(wordlist) 