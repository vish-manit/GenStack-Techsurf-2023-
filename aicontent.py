import openai
import pinecone
import config
from flask_session import Session
from urllib import response

openai.api_key = config.OPENAI_API_KEY
pinecone.init(api_key=config.PINECONE_API_KEY)
conversation_memory = []

def openAIQuery(query):
    global conversation_memory

    conversation_memory.append(f"User: {query}")

    
    # Creating a prompt using conversation history
    prompt = "\n".join(conversation_memory[-2:])  

    response = openai.Completion.create(
        engine="davinci-instruct-beta-v3",
        prompt=prompt,
        temperature=0.7,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = 'Oops, sorry, you beat the AI this time'
    
    return answer

# Enter your Open API Key here
OPENAI_API_KEY = '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'
PINECONE_API_KEY = 'cd1506a2-8f6b-4235-8416-7f5285fb50eb'
