from collections import defaultdict
import re

def common_words(filename):
    #opens file, reads it, changes chars to lowercase, closes original file
    in_file = open(filename, "r")
    text = in_file.read().lower()
    in_file.close()
    #finds all words in text, puts them in list
    text = re.findall("[\w]+", text)
    #creates dict, stores words in text in dict, then returns sorted items in dict
    wordCount = defaultdict(int)
    for word in text:
      wordCount[word] += 1
    #returns a list of words in text in sorted order
    return [pair[0] for pair in sorted(wordCount.items(), key=lambda item: item[1], reverse=True)]
    
    """question 1a

    Write a function that takes a path to a text file as input. The function
    should open the file, count the number of occurrences of each word, and
    return a sorted list of the most common words.
    """
    pass

def common_words_min(filename, min_chars):
    in_file = open(filename, "r")
    text = in_file.read().lower()
    in_file.close()
    text = re.findall("[\w]+", text)
    wordCount = defaultdict(int)
    for word in text:
      if len(word) >= min_chars:
        wordCount[word] += 1
    return [pair[0] for pair in sorted(wordCount.items(), key=lambda item: item[1], reverse=True)]
    """question 1b

    Modify this function to take a second argument that specifies the
    minimum number of characters long a word can be to be counted.
    """
    pass

def common_words_tuple(filename, min_chars):
    in_file = open(filename, "r")
    text = in_file.read().lower()
    in_file.close()
    text = re.findall("[\w]+", text)
    wordCount = defaultdict(int)
    for word in text:
        if len(word) >= min_chars:
            wordCount[word] += 1
    return sorted(wordCount.items(), key=lambda item: item[1], reverse=True)
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)
    Of course, the list of tuples should still be sorted as in part a.
    """
    pass

def common_words_safe(filename, min_chars):
    try:
        in_file = open(filename, "r")
        text = in_file.read().lower()
        in_file.close()
        text = re.findall("[\w]+", text)
        wordCount = defaultdict(int)
        for word in text:
            if len(word) >= min_chars:
                wordCount[word] += 1
        return sorted(wordCount.items(), key=lambda item: item[1], reverse=True)
    except IOError:
        return "This is not the file you're looking for..."
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """
    pass
