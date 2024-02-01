from langchain_experimental.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st


def main():
    load_dotenv()


    # Load the OpenAI API key from the environment variable
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    st.set_page_config(page_title="Ask your CSV")
    custom_image = "./client-img.png"
    image_width = 50
    st.image(custom_image, width=image_width)
    st.header("Asistent Virtual Decolandia")


    csv_file = st.file_uploader("Upload a CSV file", type="csv")
    if csv_file is not None:

        agent = create_csv_agent(
            OpenAI(temperature=0), csv_file, verbose=True)


        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                language_prefix = "Răspundeți în limba română: "
                full_question = language_prefix + user_question
                st.write(agent.run(full_question))


if __name__ == "__main__":
    main()



