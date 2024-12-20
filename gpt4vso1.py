import streamlit as st
from openai import OpenAI
import time


openai_api_key = "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"

st.session_state.client = OpenAI(api_key=openai_api_key)
st.session_state.o1 =   'o1-mini'
st.session_state.gpt = 'gpt-4o-mini'


st.session_state.user_prompt = st.text_input("Write your prompt")


def get_chat_completion(model,prompt):
    
    st.session_state.response = st.session_state.client.chat.completions.create(
        model = model,
        messages= [{"role":"user","content":prompt}],
    )

    return st.session_state.response.choices[0].message.content

if st.session_state.user_prompt:
    st.session_state.start = time.time()
    st.session_state.model_o1 = get_chat_completion(st.session_state.o1, st.session_state.user_prompt)
    st.session_state.end = time.time()
    st.session_state.o1_time = st.session_state.end - st.session_state.start  # time o1

    st.session_state.start = time.time()
    st.session_state.model_gpt = get_chat_completion(st.session_state.gpt,st.session_state.user_prompt)
    st.session_state.end = time.time()
    st.session_state.gpt_time = st.session_state.end - st.session_state.start   # time of gpt

    print("GPT MODEL",st.session_state.model_gpt)
    print("o1 Model ",st.session_state.model_o1)
    st.write(f"GPT4 MODEL RESPONSE :-\n Time taken :- {st.session_state.o1_time:.6f} \n {st.session_state.model_gpt}")
    st.write(f"O1 MODEL RESPONSE :-\n Time taken :- {st.session_state.gpt_time:.6f} \n{st.session_state.model_o1}")




