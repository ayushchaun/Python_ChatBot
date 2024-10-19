from openai import OpenAI
client = OpenAI()

command = ''' 
[6:16 PM, 9/20/2024] AYUSH: hii
[6:17 PM, 9/20/2024] Sis: Hello
[6:17 PM, 9/20/2024] AYUSH: what are you doing?
[6:17 PM, 9/20/2024] Sis: Nothing
[6:17 PM, 9/20/2024] AYUSH: you look like buffelo
[6:17 PM, 9/20/2024] Sis: Ya you look like monkey
[6:18 PM, 9/20/2024] AYUSH: one time one monkey set on tree branch and laugh at all
[6:18 PM, 9/20/2024] Sis: Haaaaa
[6:18 PM, 9/20/2024] AYUSH: ok 
'''

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a person named AYUSH who speaks gujarati as well as english. He is a coder from India. You analyze chat history and respond like AYUSH"},
        {
            "role": "user",
            "content": command
        }
    ]
)

print(completion.choices[0].message.content)