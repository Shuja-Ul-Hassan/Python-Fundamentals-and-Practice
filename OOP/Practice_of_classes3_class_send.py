def send_messages(first_list, sent_messages):
    while first_list:
        message=first_list.pop(0)
        print(f"Sending message: {message}")
        sent_messages.append(message)
