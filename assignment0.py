def fizzbuzz():
    i = 1
    while i < 101:
        if i % 3 == 0 and i % 5 == 0:
            print 'FizzBuzz'
        elif i % 3 == 0:
            print 'Fizz'
        elif i % 5 == 0:
            print 'Buzz'
        else: print i
        i = i + 1
        
from collections import Counter

# helper function that returns the most common char
def max_counter(str):
    return Counter(str).most_common(1)[0][0]
 
# returns the least common char, i.e. last char in the most_common list 
def min_counter(str):
    return Counter(str).most_common()[-1][0]
  
def swapchar(str):
    most = max_counter(str)
    least = min_counter(str)
    # define a temporary char to assist with swapping
    # one issue is that function fails if temp has a char that is in str...how do you account for that corner case?
    temp = '~'
    print str.replace(most, temp).replace(least, most).replace(temp, least)

def sortlist(num, *args):
    sorted_list = sorted(args, key=lambda x:len(x), reverse=True)
    # accounts for -1 case
    if num == -1:
        num = len(sorted_list)
    # concatenates the strings longest to shortest up till num 
    print ''.join(sorted_list[:num])
    
import random

def look_away(trials):
    i = 0
    wins = 0
    while i < trials:
        # represents direction as a random int
        luigi = random.randint(1,5)
        mario = random.randint(1,5)
        wario = random.randint(1,5)
        peach = random.randint(1,5)
        # if same direction as luigi, then luigi wins the trial
        if mario == luigi or wario == luigi or peach == luigi:
            wins += 1
        i += 1
    print 'Fraction of trials Luigi won:' + ' ' + str(wins) + '/' + str(trials)
    
import json, urllib, datetime

def shuttle_time():
    data = urllib.urlopen('http://shuttleboy.cs50.net/api/1.2/trips?a=Quad&b=Mass+Ave+Garden+St&output=json')
    json_data = json.load(data)
    current_time = datetime.datetime.now()
    #retrieves data, cleans it up into proper datetime format
    train1 = datetime.datetime.strptime(json_data[0]["departs"].replace("T", " "),'%Y-%m-%d %H:%M:%S')
    train2 = datetime.datetime.strptime(json_data[1]["departs"].replace("T", " "),'%Y-%m-%d %H:%M:%S')
    train3 = datetime.datetime.strptime(json_data[2]["departs"].replace("T", " "),'%Y-%m-%d %H:%M:%S')

    #finds difference between current time and departure time then converts to minutes
    train1time = (train1 - current_time).seconds/60
    train2time = (train2 - current_time).seconds/60
    train3time = (train3 - current_time).seconds/60

    #displays info
    print "The next train leaves at ", train1, " which is in ", train1time, " minutes"
    print "The next train leaves at ", train2, " which is in ", train2time, " minutes"
    print "The next train leaves at ", train3, " which is in ", train3time, " minutes"
