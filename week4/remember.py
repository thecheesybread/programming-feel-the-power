


while True:
    user_input = raw_input("Write a statement or a question:  ")
    user_input_split = user_input.split(' is ')
    if '.' in user_input:
        print "You defined " + user_input_split[0] + " as " +  user_input_split[1].replace(".", "")
    if '?' in user_input:
        print "You are asking what " + user_input_split[1].replace("?", "") + " is"
