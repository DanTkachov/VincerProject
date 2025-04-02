import streamlit as st
import random
import time 
from io import StringIO
from process_script import ProcessScript


def mock_response():
    responses = [
        "Response 1: 98%",
        "Response 2: 23%",
        "Response 3: 60%"
    ]
    return random.choice(responses)


st.title('Probabilities of Stressors in a Conversation')

uploaded_file = st.file_uploader("Choose a file", type=['txt'],accept_multiple_files=False)
if uploaded_file is not None:
    file_details = {
        "FileName": uploaded_file.name,
        "FileSize": uploaded_file.size
    }
    st.write(file_details)

    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # text_content = stringio.read()

    script = ProcessScript(stringio)

    st.write("File Content:")
    st.text(script.display())

st.write('API Response: ', mock_response())