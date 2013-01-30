gmail_username = "progbot0@gmail.com"
gmail_password = "closetotheedge"
def respond(user, text):
    print user
    if text == "hello":
        return "hi"
    elif text == "bye":
        return "good bye"
    elif text == "tell me why":
        return "it ain't nothing but a heartache"
    else:
        return "some random response"


def main():
    while True:
        user_input = raw_input('You: ');
        if user_input == 'quit':
            break;
        print 'Computer: ' + respond("terminal", user_input)


if __name__ == '__main__':
    main();
