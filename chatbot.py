import gradio
from groq import Groq

client = Groq(
    api_key="empty",
)

def initialize_messages():
    return [{"role": "system",
             "content": """
             You are an experienced investor who has a long time industry 
             experience in stocks and investing.Your role is to assist people 
             by providing guidance in investing, trading and stock tips in a 
             professional and simple manner.
             """}]

messages_prmt = initialize_messages()
print(type(messages_prmt))

def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama-3.3-70b-versatile",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply

iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=300),
                     textbox=gradio.Textbox(placeholder="Ask me a question related to investment"),
                     title="Investor ChatBot",
                     description="Chat bot for investment assistance",
                     theme="soft",
                     examples=["hi","What is stocks", "how to buy and sell stocks"]
                     )

iface.launch(share=True)