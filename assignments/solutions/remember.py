statements = {}

while True:
    user_input = raw_input("Write a statement or a question:  ")
    user_input_split = user_input.split(' is ')
    if '.' in user_input:
        statements[user_input_split[0].lower()] = user_input_split[1].replace(".", "")
        print "You defined " + user_input_split[0] + " as " +  user_input_split[1].replace(".", "")
    if '?' in user_input:
        to_lookup = user_input_split[1].replace("?", "")
        print to_lookup + " was defined to be " + statements[user_input_split[1].replace("?", "").lower()]
