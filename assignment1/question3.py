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

# did not implement part g

class Person:
    def __init__(self, first_name, last_name, gender):
        self.firstname = first_name
        self.lastname = last_name
        self.gender = gender
        if self.firstname[0].isupper() == False or self.lastname[0].isupper() == False:
            raise Exception ("First letter not capitalized")  
        elif self.gender != 'M' and self.gender != 'F':
            raise Exception ("Not a gender")
        pass

from collections import defaultdict

class Building(object):
    locations = defaultdict(list)
    
    def __init__(self, location):
        self.d = defaultdict(list)
        # sorts dict by room num
        sorted(self.d, key=lambda key: self.d[key])
        Building.locations[self].append(location)
    
    def enter(self, person, room_no):
        self.room_no = room_no
        for room, per in self.d.items():
            if person in per:
                self.d[room].remove(person)
        self.d[self.room_no].append(person)
        pass

    def where_is(self, person):
        for room, per in self.d.items():
            if person in per:
                return room
        return "Not in building"
    
    def locate(self, location):
        return 
        
class Office(Building):
    def __init__(self, emplist):
        self.emplist = emplist
        super(Office, self).__init__()
        
    def enter(self, person, room_no):
        if person in self.emplist:
            super(Office, self).enter()
        else:
            return "Cannot enter"
            
class House(Building):
    def __init__(self):
        super(House, self).__init__()
        self.d = []
        
    def enter(self, person):
        self.list.append(person)
    
    def at_home(self, person):
        if person in self.list:
            return True
        else: return False   

def locate (location):
    # checks if location is in the locations dict, and if it is return corresponding building
    for build, loc in Building.locations.items():   
        if location in loc:
            return build
    return "None"
