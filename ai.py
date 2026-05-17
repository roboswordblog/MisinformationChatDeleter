from openai import OpenAI

client = OpenAI()


def misinformationChooser(message):
  prompt = """You are an AI misinformation detection assistant. Your task is to analyze SMS messages and assign a misinformation score from 1 to 10.

  Scoring system:

  * 1 = Completely true and accurate
  * 8 = Misinformation that includes wars that aren't true, social trends that are not true, ect
  * 10 = Extremely false, misleading, or harmful misinformation

  Only return the misinformation score for each message.
  """
  response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
      {"role": "system", "content": prompt},
      {"role": "user", "content": message}
    ]
  )

  return response.choices[0].message.content
