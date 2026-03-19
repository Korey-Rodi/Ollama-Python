import ollama
##this is a locally hosted version of ollama mistral AI
print("I am a locally hosted AI chat bot...")
text = input("What can I help you with? \n")

instructions = [
    {'role': 'system', 'content': "You are a AI chatbot, always be kind and thorough with your responses."
    },
]

response = ollama.chat(model='mistral', messages = instructions + [
    {
        'role': 'user',
        'content': text,
    },
])
print("You said " + text)
print(response['message']['content'])