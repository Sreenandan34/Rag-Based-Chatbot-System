import asyncio
import streamlit as st
from agent import run_agent

st.title("RAG LangChain Agent")

query = st.text_input("Ask your question")

if st.button("Run"):

    if query.strip() == "":
        st.warning("Please enter a query")
    else:
        answer, source = asyncio.run(run_agent(query))

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Source")
        st.write(source)