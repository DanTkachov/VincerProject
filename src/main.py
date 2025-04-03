import streamlit as st
import random
import time 
from io import StringIO
from process_script import ProcessScript
from api_calls import CallAPI
from prompts import make_prompt

def display_stressor_progress_bars(stressors, speaker_name):
    """
    Display stressors as progress bars where the fill corresponds to the percentage,
    with percentages displayed at the end of each bar.
    """
    import streamlit as st
    
    # Add speaker name as header
    st.subheader(f"{speaker_name}")
    
    # Sort stressors by value (highest first)
    sorted_stressors = dict(sorted(stressors.items(), key=lambda item: item[1], reverse=True))
    
    # Custom CSS for better looking progress bars
    st.markdown("""
    <style>
    .stressor-label {
        font-weight: bold;
        margin-bottom: 5px;
        margin-top: 15px;
    }
    .stressbar-container {
        display: flex;
        align-items: center;
        margin-bottom: 5px;
    }
    .stressbar-progress {
        flex-grow: 1;
        margin-right: 10px;
    }
    .stressbar-percent {
        width: 45px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Display each stressor as a progress bar with percentage at the end
    for stressor, percentage in sorted_stressors.items():
        # Display stressor name
        st.markdown(f"<p class='stressor-label'>{stressor}</p>", unsafe_allow_html=True)
        
        # Create a container with flexbox to put progress bar and percentage side by side
        col1, col2 = st.columns([9, 1])
        
        with col1:
            # Choose color based on percentage
            if percentage < 30:
                color = "green"
            elif percentage < 70:
                color = "orange"
            else:
                color = "red"
            
            # Display progress bar without text
            st.progress(percentage / 100.0)
        
        with col2:
            # Display percentage at the end
            st.markdown(f"<div style='text-align: right; font-weight: bold;'>{percentage}%</div>", unsafe_allow_html=True)


# Session variables
# api_key_saved -> tracks if an API key has been saved
# api_key -> stores the actual API key
if 'api_key_saved' not in st.session_state:
    st.session_state.api_key_saved = False


file_upload_tab, api_key_tab = st.tabs(['File Upload & Process', 'Set API Key'])

# Helper function to show a notification on saving a key.
def save_api_key():
    if st.session_state.api_key != None and st.session_state.api_key.strip():
        st.session_state.api_key_saved = True
        # st.session_state.api_key = st.session_state.api_key
        st.toast("API key saved successfully!", icon=":material/check_circle:")

# Code for the File Upload tab
with file_upload_tab:

    st.title('Probabilities of Stressors in a Conversation')

    if not st.session_state.api_key_saved:
        st.warning("You don't have an API key set. Set it before selecting a file.", icon=":material/warning:")

    uploaded_file = st.file_uploader("Choose a file", type=['txt'],accept_multiple_files=False)
    if uploaded_file is not None:
        file_details = {
            "FileName": uploaded_file.name,
            "FileSize": uploaded_file.size
        }
        st.success(f'Uploaded \'{uploaded_file.name}\' Successfully!')

        if st.button(label="Analyze"):
            file_text = StringIO(uploaded_file.getvalue().decode("utf-8"))
            # script = ProcessScript(file_text)

            with st.spinner(f'Processing API calls for all speakers...'):
                speaker_api_call = CallAPI("", '', False, st.session_state.api_key, file_text)
                claude_response = speaker_api_call.message()
                stressors = speaker_api_call.parse_response(claude_response)

            for person, stressors in stressors.items():
                display_stressor_progress_bars(stressors=stressors, speaker_name=person)


with api_key_tab:
    # Set success message to now show
    st.title("Set API Key")

    if st.session_state.api_key_saved:
        current_value = st.session_state.api_key
    else:
        current_value = None

    api_key = st.text_input("Set Api Key:", 
        value=current_value,
        on_change=save_api_key,
        key="api_key",
        placeholder="Copy-Paste your API key here.",
        type="password")

    if st.session_state.api_key != None:
        st.info("You have a saved API key.", icon=":material/info:")
