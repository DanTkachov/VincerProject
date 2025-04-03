# Stressor Probability Predictor

## Purpose

This project gives the probabilities of 5 job related stressors being present given a conversation between people. The 5 stressors are:
1. Role Ambiguity
2. Role Conflict
3. Role Overload
4. Interpersonal Conflict
5. Perceived Lack of Control

It uses Claude on the backend to make API calls to determine the likelihood of the stressors appearing, and Streamlit on the frontend for an easy-to-use, polished UI for users to interact with.

## Usage

1. Click on the "Set API Key" tab at the top.
2. Input your Claude API key and hit enter to save it.
3. Go to the "File Upload & Process" tab
4. Upload your conversation as a .txt file.

    4.5. Each line of the conversation file should be of the format \[Speaker's Name\]\: \[Their Words\]. If a line is empty or starts with a '#', it is ignored.
5. Click the "Analyze" button that appears after uploading a file.
6. Wait for a response and view the stressors!

## Running this repo locally

1. Clone the repo:

    `git clone https://github.com/DanTkachov/VincerProject`

2. Set working directory to the cloned repo:

    `cd VincerProject`

3. Create a venv for the project:

    ```
    python -m venv .venv
    source .venv/bin/activate
    ```

4. With the venv activated, install the requirements:

    `pip install -r requirements.txt`

5. With the venv activated, run streamlit:

    `streamlit run src/main.py`

6. Navigate to the localhost found in the console output.

If you would like to use a .env file to store a key instead of pasting it into the "Set API Key" tab:
1. After cloning, create a `.env` file. Use the format in the `.env.example` as a template. 
2. Change Line 109 in `src/main.py` from

 ```
 speaker_api_call = CallAPI("", '', False, st.session_state.api_key, file_text)
 ```
 to:

 ```
 speaker_api_call = CallAPI("", '', True, st.session_state.api_key, file_text)
 ```

## How this works

A file is given by the user (`src/main.py`), which is then turned into a raw string in `src/process_script.py` before being passed on to `src/api_calls.py` which creates a message and sends it to Claude. After which, the response is parsed in `asrc/pi_calls.py` to create a hashmap of stressors to their percentages, which is then caught in `src/main.py` and displayed as bars.

## Structure
Code is located in the `/src` directory. 
- `src/api_calls.py` handles making API calls, 
- `src/main.py` contains the Streamlit frontend code, 
- `src/process_script.py` processes a given script and outputs it in a format that makes it easier for the AI to analyze.
- `conversations` contains example conversations.
```
├── conversations
│   ├── script1.txt
│   ├── script2.txt
│   ├── script3.txt
│   ├── script4.txt
│   └── script5.txt
├── README.md
├── requirements.txt
└── src
    ├── api_calls.py
    ├── main.py
    ├── process_script.py
    └── prompts.py
```

## Dependencies

 - anthropic
 - python-dotenv
 - requests
 - streamlit



## Assumptions made
1. Names only contain alphabetic characters, spaces, and/or hyphens.
2. Script1 contains titles for the individuals before starting the conversation. I added '#' characters to denote them as comments so that my processScript file ignores them.
3. There is a set and hashmap that contain the names of the people in the conversation. Since Vincer offers digital products, I am assuming that each person, even if they have the same name, has their own microphone (with an ID) that could be used for some hash function so that they are always different in this set. Alternatively, name them "Chris 1" and "Chris 2."

## AI Use

AI was primarily used for the bars showing the percentages of each stressor. Specifically, this is the `display_stressor_progress_bars()` function in `src/main.py`. 

## Areas of improvement
To make the project more robust:
 - Store the key in a safer location
 - Use cookies instead of session stores to store the API key, to persist it between page visits
 - Validate the API key before using it
 - Handle errors better during processing and making API calls.
 - Handle edge cases like extremely large files by processing speakers one at a time instead of all at once, or empty files.
 - Add rate limiting just in case.

 ## Potential Future Features:
  - Store previous analyses
  - Export or save analyses
  - Allow the user to modify the prompt