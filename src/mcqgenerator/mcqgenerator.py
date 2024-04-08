import os
import json
from dotenv import load_dotenv

from langchain.llms import AI21
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain


load_dotenv()

os.environ['AI21_API_KEY']

# load the model
llm = AI21(temperature = 0.7)

# Create the template
template = """
Text: {text}
You are expert MCQ maker, Given the above text. It is your job to create a QUIZ of {number} of multiple choice questions for
{subject} students in {tone}.
Make sure the question are correct and not repeated questions.
Make sure the format of your response in RESPONSE_JSON below, use it as a guide.

Ensure to make {number} of MCQ's
###RESPONSE_JSON
{response_json}

"""



prompt1 = PromptTemplate(input_variables = ['text','number','subject','tone','response_json'],
                          template = template)

chain1 = LLMChain(llm = llm, prompt = prompt1, output_key = 'quiz', verbose = True)


template2 = """
you are exper in english grammar & writer. Given the MCQ question for {subject} students. \
you need to evaluate the complexity of the MCQ question according to the MCQ grammar and complete analysis of the quiz. \
Only use max 50 words for complexity analysis. If the quiz is not as per the congitive and analytical abilties \
of the students,update the quiz questions which needs to be changed & change the tone which needs to be changed, \
which perfectly fits the student abilities. 

QUIZ MCQ : 
{quiz}

Check from an expert English Writer of the above quiz:
"""

prompt2 = PromptTemplate(input_variables = ['subject','quiz'],template = template2)

chain2 = LLMChain(llm = llm, prompt = prompt2, output_key = 'quiz2', verbose = True)

final_chain = SequentialChain( chains = [chain1, chain2], input_variables = ['text','number','subject','tone','response_json'],
                 output_variables = ['quiz','quiz2'], verbose = True)


if __name__ == '__main__':
    print(final_chain)
