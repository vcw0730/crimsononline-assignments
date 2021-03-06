"""question 3

a)  Implement classes representing people and buildings. People should support
    name and gender, seamlessly verifying that gender is either M or F (if it
    isn't, what's the best way to inform the calling code that a mistake was
    made?) and enforcing capitalization of both first name and last name.

b)  Buildings should support a function enter that takes a person and a room
    number. The building should then keep track of anyone who enters/leaves the
    building and respond to some type of where_is(person) query with the room
    number that person is in. Ensure, naturally, that no one can be in more
    than one building at a time.

c)  Make the building class iterable over the people in it. That is, make it
    possible to write a for loop of the form:
        for person in building:
            ...

d)  Implement a class that represents an office building, an object that
    behaves the same as a building but only allows people to enter if they are
    on a list of employees passed in when the OfficeBuilding is instantiated.
    You may want to look up the super function in the Python documentation
    concerning classes.

e)  Implement a class that represents a house. The House class should implement
    enter to take only a Person object, and the House class should not support
    where_is at all. It should instead support at_home(Person), a function that
    returns a Boolean.

f)  Modify all buildings, houses included, to remember their location as an
    (x, y) tuple. Then make it possible to call some function that takes such
    a tuple and returns the building object at that tuple or None if no
    building exists at that location. You may choose whether any given location
    can only hold one building or multiple buildings, but you need to handle
    this corner case in some logical fashion.

g)  With a minimum of code duplication, modify the Building class so that
    bldg[roomnumber] = person accomplishes the same thing as
    bldg.enter(person, roomnumber). Be careful with how you do this if you
    chose to inherit any classes from Building (which you should have).
"""

"""

Was unsure about 3g): does it mean that each room/index of bldg corresponds to a particular 
person, i.e. bldg is now a list of Person objects of length num_rooms?  If so, then what I 
would do is change the inititialization of the self.b list so that it is initialized with 
some sort of default Person object placeholders instead of empty lists, or essentially tell
the computer that I was going to be putting Person objects into the list b.  However, I 
couldn't figure out how to do that - the way I tried to do it fails b/c I basically have to
insert actual Person objects into each index of the list to initialize it, which isn't what
I want.  The enter method also relies on this "default" Person object, since if the person
in question is already in the building, it just puts the default Person where the person
once was and puts the person into the new position. However, this way does successfully 
create a list of num_rooms long, though, so that there is a Person in every room number,
and b.enter(person, roomnumber) is equivalent to b.b[roomnumber] = person in this code.
So yea...not sure if this was the correct interpretation of 3g), but if it is, then this
describes the approach I would take to implement and the problems I ran into in doing so.

"""

class Person:
    def __init__(self, first_name, last_name, gender):
        self.firstname = first_name
        self.lastname = last_name
        self.gender = gender
        if self.firstname[0].isupper() == False or self.lastname[0].isupper() == False:
            raise Exception ("First letter not capitalized")  
        elif self.gender != 'M' and self.gender != 'F':
            raise Exception ("Not a gender")

from collections import defaultdict

class Building(object):
    locations = defaultdict(list)
    
    def __init__(self, num_rooms, location):
        self.b = []
        self.num_rooms = num_rooms
        self.location = location
        # keeps track of total people in building
        self.ppl = []
        # initializes building to list of Person objects
        for x in range(0, self.num_rooms):
            y = Person("Default", "Default","M")
            self.b.append(y)
        Building.locations[self.location].append(self)
    
    # allows iteration over people in building
    def __iter__(self):
        return iter(self.ppl)
    
    def enter(self, person, room_no):
        # the -1 adjusts user input to list input
        self.room_no = room_no - 1
        # tracks person was already in building
        found = False
        # iterate through each room
        for room in range(0,self.num_rooms):
            if person == self.b[room]:
                self.b[room] = Person("Default","Default","M")
                found = True
        self.b[self.room_no] = person
        # if person newly entered building, then add to master list of people
        if found == False:
            self.ppl.append(person)

    def where_is(self, person):
        for room in range(0,self.num_rooms):
            if person == self.b[room]:
                #adjusts list input to user input
                return room + 1
        # returns this if person not found in any room
        return "Not in building"
        
class Office(Building):
    # how do you ensure that the emplist parameter passed in by user is actually a list of Person instances?)
    def __init__(self, num_rooms, location, emplist):
        self.emplist = emplist
        super(Office, self).__init__(num_rooms, location)
        
    def enter(self, person, room_no):
        if person in self.emplist:
            super(Office, self).enter(person, room_no)
        else:
            return "Cannot enter"
            
    def where_is(self, person):
        return super(Office, self).where_is(person)
            
class House(Building):
    def __init__(self, location):
        # num of rooms is not important, so just defaulted to 1
        super(House, self).__init__(1, location)
        self.list = []
        
    def enter(self, person):
        self.list.append(person)
    
    def at_home(self, person):
        if person in self.list:
            return True
        else: return False   

def locate (location):
    # checks if location is in the locations dict, and if it is return corresponding building(s)
    for loc, builds in Building.locations.items():   
        if location == loc:
            return builds
    return "None"
