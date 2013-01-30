gmail_username = "programmingdecal@gmail.com"
gmail_password = "benbenben"
def respond(input):
    if input == "victor":
        return "sucks dick"
    if input == "anders":
        return "cup"


def main():
    while True:
        user_input = raw_input('You: ');
        if user_input == 'quit':
            break;
        print 'Computer: ' + respond(user_input)


if __name__ == '__main__':
    main();
