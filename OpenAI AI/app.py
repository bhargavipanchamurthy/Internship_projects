import streamlit as st
from openai import OpenAI

st.title('GenAI App - AN AI Code Reviewer')
st.header('Code Reviewer....')

f = open('.open_api_key.txt')
OPENAI_API_KEY = f.read()
client = OpenAI(api_key = OPENAI_API_KEY)

query = st.text_area('Enter Your Query : ')
if st.button('Generate'):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "analyze the submitted code and identify potential bugs, errors, or areas of improvement"},
            {"role": "user", "content": query}
        ]
    )
    st.write(response.choices[0].message.content)
