import ai


def makeChat(code):
    file = open(f"data/chats/{code}", "w")
    file.write("System|Hello, this is your new chat")
    file.close()


def getChat(code):
    try:
        file = open(f"data/chats/{code}", "r")
    except FileNotFoundError:
        return False

    chatMessages = {}
    for line in file.read().split("\n"):
        chatMessages[line.split("|")[0]] = line.split("|")[1]
    return chatMessages


def getAllChatMessages(code):
    chatMessages = {}
    file = open(f"data/chats/{code}", "r")
    for line in file.read().split("\n"):
        chatMessages[line.split("|")[0]] = line.split("|")[1]
    return chatMessages


def addChatMessage(username, message, code):
    ms = ai.misinformationChooser(message)
    if ms > 5:
        message = message + " (This seems to be minor misinformation)"
    if ms > 8:
        message = "this message seems to contain deep misinformation that can be harmful, please stop sending these messages"
    file = open(f"data/chats/{code}", "a")
    file.write("\n" + username + "|" + message)
    file.close()


def resetChat():
    file = open("data/chatLogs", "w")
    file.write("")
    file.close()
