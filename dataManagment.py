import ai

def getAllChatMessages():
  pass

def addChatMessage(username,message):
  ms = ai.misinformationChooser(message)
  if ms > 5:
    message = message + " (This seems to be minor misinformation)"
  if ms > 8:
    message = "this message seems to contain deep misinformation that can be harmful, please stop sending these messages"
  file = open("data/chatMessages.txt", "a")
  file.write(username + "|" + message + "\n")
  file.close()

def resetChat():
  file = open("data/chatLogs", "w")
  file.write("")
  file.close()
