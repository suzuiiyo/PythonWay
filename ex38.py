states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print '_' * 10
print "NY state has: ", cities['NY']
print "MI state has: ", cities['MI']

#print out some state
print '_' * 10
print "Michigan's abbreviation is %s" % states['Michigan']
print "Florida's abbreviation is %s" % states['Florida']

#do it by using the state then cities dict
print '_' * 10
print "New York state has the city: ", cities[states['New York']]
print "Florida state has the city: ", cities[states['Florida']]

# print every state abbreviation
print '_' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '_' * 10
for abbrev in cities.items():
    print "%s has the city %s" % (abbrev, cities)

# now do both at the same time
print '_' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '_' * 10
# safely get a abbreviation by state that might not be there
city = cities.get('Texas', None)

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

