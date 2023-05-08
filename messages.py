"""8-9 list of short messages, pass to show_messages()"""


def show_messages(messages_list):
    """ Print the passed list """
    for message in messages_list:
        print(message)


messages = ["Hello there!", "This is a message", "Secret message"]
show_messages(messages)
