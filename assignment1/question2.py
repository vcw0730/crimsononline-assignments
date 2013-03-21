from collections import defaultdict
import re

# don't quite understand how reg expressions work

def parse_links_regex(filename):
    file = open(filename, "r")
    html_list = file.read()
    file.close()
    # find all links matching form <a href="link">text</a>, capture link and text
    urls = re.findall(r"<a href=\"([^\"]*)[^>]*>([^<]*)", html_list)
    d = defaultdict(list)
    # create key-val dict with txt as key and links as vals
    # (I think) if two links use same txt, then they just both get added on as vals of that key
    for link, txt in urls:
        d[txt].append(link)
    return d.items()
        
    # there are \n and random spaces in my dict...how to fix / why?
    
    """question 2a

    Using the re module, write a function that takes a path to an HTML file
    (assuming the HTML is well-formed) as input and returns a dictionary
    whose keys are the text of the links in the file and whose values are
    the URLs to which those links correspond. Be careful about how you handle
    the case in which the same text is used to link to different urls.
    
    For example:

        You can get file 1 <a href="1.file">here</a>.
        You can get file 2 <a href="2.file">here</a>.

    What does it make the most sense to do here? 
    """
    pass

from lxml import etree

# I was unable to install lxml for some reason, getting errors when I try to run "sudo pip install lxml"
def parse_links_xpath(filename):

    """question 2b

    Do the same using xpath and the lxml library from http://lxml.de rather
    than regular expressions.
    
    Which approach is better? (Hint: http://goo.gl/mzl9t)
    """
    pass
