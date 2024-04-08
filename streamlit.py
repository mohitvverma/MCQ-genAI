import streamlit as st
import pandas as pd
import os
import json
import traceback
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file,get_data
from src.mcqgenerator.mcqgenerator import final_chain
from src.mcqgenerator.logger import logging

load_dotenv()

key = os.environ["AI21_API_KEY"]

with open('/Users/mohitverma/Documents/Dcoument/ML/Langchain/MCQ-genAI/response.json','r') as f:
    response_json = json.load(f)


# add title
st.title("MCQ Generator Application")

# form create
with st.form('user_input'):
    # file upload
    uploaded_file = st.file_uploader("Upload File in pdf or text format only")

    #input fields
    mcq_count = st.number_input("No. of MCQs", min_value=3, max_value=10)

    #Subject
    subject = st.text_input("Insert Subject", max_chars=100)

    #Quiz-tone
    tone = st.text_input("Complexity Level of Question", max_chars=30, placeholder="Enter Complexity Level of Question")

    # add button
    button = st.form_submit_button("Create MCQ")

    # check if the button is clicked & all field inputs, This is our main code
    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("loading..."):

            try:
                text = read_file(uploaded_file)
                #
                response = final_chain(
                    {
                        'text': text,
                        'number':mcq_count,
                        'subject':subject,
                        'tone':tone,
                        'response':json.dumps(response_json)
                    }
                )

            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error('error')

            else:
                if isinstance(response,dict):

                    # Extract the quiz data from the response
                    quiz = response.get("quiz", None)

                    # converting the data into dataframe
                    if quiz is not None:
                        table_data = get_data(quiz)
                        if table_data is not None:
                            data = pd.DataFrame(table_data)
                            data.index = data.index + 1
                            st.table(data)
                            # display review in text boz as well
                        else:
                            st.error("Error in table data")

                else:
                    st.write(response)








