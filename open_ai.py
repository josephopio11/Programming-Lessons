# Import the necessary modules
import openai
import random
import time

# Set the OpenAI API key
openai.api_key = "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"

running = True
while running:
    # Set the prompt for the AI model
    print("Enter your query")
    prompt = input()

    # Use the OpenAI API to generate a response to the prompt
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5
    )

    # Print the response
    print(response)
    # for i in len(response):
    #     print(response["choices"][i]["text"])
