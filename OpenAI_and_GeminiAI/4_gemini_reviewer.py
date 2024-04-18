import streamlit as st
import google.generativeai as genai

f = open(".geminiai_api_key.txt")
key = f.read()

genai.configure(api_key=key)
st.title("AI Chatbot with GeminiAI....")

#genai.configure(api_key = config["gemini"])
ai=genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
    system_instruction="""You're an AI Teaching Assistant that provides answers to user queries related to data science topics. 
                         If 'hai'or 'hi' in the users request, respond with politely. Otherwise, if the user's query is unrelated to 
                         data science, respond with 'I'm sorry, I don't have information about that.' If the user's query is not a greeting 
                         and is related to data science, provide an appropriate answer.""")
if "chat_history" not in st.session_state:
    st.session_state["chat_history"]=[]

chat = ai.start_chat(history=st.session_state['chat_history'])
for msg in chat.history:

    st.chat_message(msg.role).write(msg.parts[0].text)

user_prompt=st.chat_input()

if user_prompt:
    st.chat_message("user").write(user_prompt)
    response=chat.send_message(user_prompt)
    st.chat_message("ai").write(response.text)
    print(chat.history)
    st.session_state["chat_history"]=chat.history

 
#for m in genai.list_models():
    #if 'generateContent' in m.supported_generation_methods:
        #print(m.name)