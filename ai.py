import random
# from openai import OpenAI

# client = OpenAI()

def misinformationChooser(message):
  prompt = """You are an AI misinformation detection assistant. Your task is to analyze SMS messages and assign a misinformation score from 1 to 10.

  Scoring system:

  * 1 = Completely true and accurate
  * 10 = Extremely false, misleading, or harmful misinformation

  Only return the misinformation score for each message.
  """
  return random.randint(1,10)
  
