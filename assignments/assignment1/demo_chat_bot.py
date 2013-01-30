def respond(user, text):
    text = text.lower()
    if text == "hey" or text == "hello":
        return "hey! how are you?"
    elif text[-1] == "?":
        if text.split(" ")[0] == "why":
            return "because i love crocodiles"
        else:
            return "i'm not sure how to answer that question"
    elif text.split(" ")[0] == "you're" or text.split(" ")[0] == "you":
        return "no, " + text + "!"
    elif "good" in text:
        return "that's good!"
    elif "bye" in text:
        return "cya later, alligator ;)"
    elif text == "tell me why":
        return "it ain't nothing but a heartache"
    elif len(text.split(" ")) == 1:
        return text + " indeed"
    else:
        return "so what?"



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
