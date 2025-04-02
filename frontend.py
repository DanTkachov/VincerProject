import streamlit as st
import random
import time 
from io import StringIO
from process_script import ProcessScript


api_key_default_message = "Copy-Paste your API key here."

if 'api_key_saved' not in st.session_state:
    st.session_state.api_key_saved = False
if "api_key" not in st.session_state:
    st.session_state.api_key = api_key_default_message
if "show_api_key_success" not in st.session_state:
    st.session_state.show_api_key_success = False


def mock_response():
    responses = [
        "Response 1: 98%",
        "Response 2: 23%",
        "Response 3: 60%"
    ]
    return random.choice(responses)


file_upload_tab, api_key_tab = st.tabs(['File Upload & Process', 'Set API Key'])


def save_api_key():
    if st.session_state.api_key != api_key_default_message and st.session_state.api_key.strip():
        st.session_state.api_key_saved = True
        st.session_state.show_api_key_success = True
        # st.session_state.api_key_value = st.session_state.api_key
        st.session_state.api_key = st.session_state.api_key


with file_upload_tab:

    st.title('Probabilities of Stressors in a Conversation')

    if not st.session_state.api_key_saved:
        st.warning("You don't have an API key set. Set it before selecting a file.", icon=":material/warning:")

    # if 'api_key_saved' in st.session_state:
    #     st.write(st.session_state.api_key)

    uploaded_file = st.file_uploader("Choose a file", type=['txt'],accept_multiple_files=False)
    if uploaded_file is not None:
        file_details = {
            "FileName": uploaded_file.name,
            "FileSize": uploaded_file.size
        }
        st.success(f'Uploaded \'{uploaded_file.name}\' Successfully!')

        if st.button(label="Analyze"):
            file_text = StringIO(uploaded_file.getvalue().decode("utf-8"))
            script = ProcessScript(file_text)

            st.write("File Content:")
            st.text(script.display())
            st.write(script.return_speakers())

    st.write('API Response: ', mock_response())

with api_key_tab:
    # Set success message to now show
    st.title("Set API Key")

    current_value = st.session_state.api_key if st.session_state.api_key_saved else api_key_default_message

    api_key = st.text_input("Set Api Key:", 
        value=current_value,
        on_change=save_api_key,
        key="api_key")

    if st.session_state.api_key != api_key_default_message:
        st.info("You have a saved API key.", icon=":material/info:")
