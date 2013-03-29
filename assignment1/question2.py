from collections import defaultdict
import re

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
    return d
        
    # there are \n and random spaces in my dict...how to fix / why?
    

"""question 2b

    Do the same using xpath and the lxml library from http://lxml.de rather
    than regular expressions.
    
    Which approach is better? (Hint: http://goo.gl/mzl9t)
    """

# wondering what pos is?

import lxml.html

def parse_links_xpath(filename):
    d = defaultdict(list)
    html = lxml.html.parse(filename)
    # converts parsed lxml tree object into HTML string so that iterlinks can use
    htmlstr = lxml.html.tostring(html)
    # iterates over each, inserting text as keys and links as values of corresponding keys
    for elt, atr, link, pos in lxml.html.iterlinks(htmlstr):
        d[elt.text].append(link)
    return d
    
