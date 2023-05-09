"""8-12 Sending messages send_messages() prints each message and moves
 each message to sent_messages list """


def send_messages(message_list, sent_list):
    """ print list and passed message to new list """
    while message_list:
        for string in message_list:
            print("sending message and adding to sent messages list:")
            current = message_list.pop()
            print(current)
            sent_list.append(string)
        show_sent_messages(sent_list)


def show_sent_messages(sent2_list):
    """ print sent list """
    print("----------------sent----------------------")
    for sent in sent2_list:
        print(sent)
    print("-------------original messages---------------")
    print(messages)
    print("-------------copy messages---------------")
    print(messages_copy)


messages = ["Hello there!", "This is a message", "Secret message"]
messages_copy = messages[:]
sent_messages = []

send_messages(messages_copy, sent_messages)
print(messages_copy)
