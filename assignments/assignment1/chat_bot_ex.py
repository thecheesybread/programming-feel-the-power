def respond(user, text):
    #text = text.lower()
    if text == "hey" or text == "hello":
        return "hey"
    elif text == "tell me why":
        return "it ain't nothing but a heartache"
    elif "bye" in text:
        return "bye"
    else:
        return "some random response"



# Don't worry about these until you're ready to run your
# program through gmail
gmail_username = "progbot0@gmail.com"
gmail_password = "closetotheedge"

# This function makes the program run
# You'll learn about all this stuff later
def main():
    while True:
        user_input = raw_input('You: ');
        if user_input == 'quit':
            break;
        print 'Computer: ' + respond("terminal", user_input)


if __name__ == '__main__':
    main();
