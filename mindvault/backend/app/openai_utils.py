# import openai
# import os

# openai.api_key = os.getenv("OPENAI_API_KEY")

# def generate_flashcard(topic):
#     prompt = f"Create a simple flashcard for {topic}."
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response['choices'][0]['message']['content']
