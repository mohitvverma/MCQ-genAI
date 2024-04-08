# It is a utils file for utility, we use as a helper, It is helping file

import os
from langchain.document_loaders import PyPDFLoader
import json
import traceback
import PyPDF2


# method 1
def read_file(filename):

    if filename.endswith('.pdf'):
        try:
            loader = PyPDF2.PdfFileReader(filename)
            text = ""

            for page in loader.pages:
                text += page.extractText()
            return text

        except Exception as e:
            print(e.with_traceback())

    elif filename.name.endswith('.txt'):
        return filename.read().decode('utf-8')

    else:
        raise Exception(
            "Unsupported file type. Only .pdf and .txt are supported.")


def get_data(quiz):

    try:
        # convert the str into dict
        quiz = json.loads(quiz)

        table_data  = []

        #iterate over the quiz dict & get the data into dataframe
        for key, value in quiz.items():
            mcq = value['mcq']

            option = "||".join(
                [
                    f"{option} - {option_value}" for option, option_value in value['options'].items()
                ]
            )

            correct = value['correct']
            table_data.append({"MCQ": mcq, "Option": option, "Correct": correct})

        return table_data

    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False

















