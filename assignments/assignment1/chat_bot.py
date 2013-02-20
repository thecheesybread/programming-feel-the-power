def respond(text):
    if text == "hey" or text == "hello":
        return "hey, how are you?"
    elif text == "tell me why":
        return "it ain't nothing but a heartache"
    elif text == "bye":
        return "bye"
    elif text == "big baby":
        return "you are a big baby"
    else:
        return "some random response"



# Don't worry about these until you're ready to run your
# program through gmail
gmail_username = ""
gmail_password = ""

# This function makes the program run
# You'll learn about all this stuff later
def main():
    while True:
        user_input = raw_input('You: ');
        if user_input == 'quit':
            break;
        print 'Computer: ' + respond(user_input)


if __name__ == '__main__':
    main();
