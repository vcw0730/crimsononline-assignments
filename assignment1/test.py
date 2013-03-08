from pprint import pprint # pretty print output formatting
from question1 import (common_words, common_words_min, common_words_tuple,
    common_words_safe)
from question2 import parse_links_regex, parse_links_xpath
from question4 import GITHUB_URL
# fill in the rest!

print "==testing question 1=="
print "common_words... ",
pprint(common_words("words.txt"))

print "common_words_min 2... ",
pprint(common_words_min("words.txt", 2))

print "common_words_min 5... ",
pprint(common_words_min("words.txt", 5))

print "common_words_min 9... ",
pprint(common_words_min("words.txt", 9))

print "common_words_tuple w/ min 5... ",
pprint(common_words_tuple("words.txt", 5))

print "common_words_safe... ",
pprint(common_words_safe("words_fail.txt", 5))
print


print "==testing question 2=="
print "regex... ",
pprint(parse_links_regex("crimson.html"))
pprint(parse_links_xpath("crimson.html"))
print


print "==testing question 3=="
# ???
print


print "==testing question 4=="
print "github url: {}".format(GITHUB_URL)
print


print "==testing question 5=="
# ???
print