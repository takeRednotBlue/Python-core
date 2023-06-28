import openai

# Set up your OpenAI API key
openai.api_key = "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"

# Define a conversation with the model
conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
]

# Send the conversation to the model
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation
)

# Get the model's reply
reply = response['choices'][0]['message']['content']
print("Model:", reply)

"""
"""
