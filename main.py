import openai 
import os

openai.api_key = os.getenv('OPENAI_API_KEY')


with open("C:\\Users\\mahachi\\Desktop\\ML\\Code Review\\code_1.py", 'r') as file:
   code_content = file.read()
 
#def get_response(code_content):    
response = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages =[
        {'role' : 'system',
        'content' : 'You are a code review assistant. Provide detailed suggestions to improve the given Python code.'},
        {'role': 'user', 'content': code_content},
    ],
    temperature=0.5,
    max_tokens=1024
)
#print(response)
print(response.choices[0].message.content)
    #return response.choices[0].message.content

#print(get_response(code_content))