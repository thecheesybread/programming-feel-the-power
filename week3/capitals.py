state_capitals = {}
state_capitals['California'] = 'Sacramento'
state_capitals['Illinois'] = 'Springfield'
state_capitals['Nevada'] = 'Las Vegas' #just kidding it's actually Carson City... let's fix that!
state_capitals['Nevada'] = 'Carson City' #we fixed it. state_capitals['Nevada'] is now equal to Carson City instead of Las Vegas
state_capitals['West Virginia'] = 'Charleston'

#<b>fill out a few more capitals here, but you get the point!</b>

state = raw_input("Which state do you want to know the capital of? ")
if state in state_capitals:
    print "The capital of " + state + " is " + state_capitals[state]
else:
    print "The computer doesn't know the capital of this state... yet"
