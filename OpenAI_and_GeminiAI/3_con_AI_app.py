import streamlit as st 
from openai import OpenAI

model=OpenAI(api_key="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")

st.title("AI Chatbot with OpenAI")

if "memory" not in st.session_state:
    st.session_state["memory"]=[]
#memory =[]

st.chat_message("ai").write("Hi, How may I help you today?")

for msg in st.session_state["memory"]:
    st.chat_message(msg["role"]).write(msg["content"])
    
user_input=st.chat_input()

if user_input:
    st.session_state["memory"].append({"role":"user","content":user_input})
    st.chat_message("user").write(user_input)
    
    history = st.session_state["memory"]
    
    response = model.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = history + [
            {"role":"system","content": """
             you are helpfull AI Assistant who answer all the user queries politely. 
             If some one asks your name tell them that your name is "Chiti The Robot." """},
            {"role":"user","content":user_input}
        ]
    )
    #st.chat_message("ai").write(response.choices[0].message.content)
        
    st.session_state["memory"].append({"role":"assistant","content": response.choices[0].message.content}) 
    
    st.chat_message("ai").write(response.choices[0].message.content)
    

    
    #st.chat_message("ai").write(response.choices[0].message.content)


