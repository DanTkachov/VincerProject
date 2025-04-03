# Purpose

This project gives the probabilities of 5 job related stressors being present given a conversation between people. The 5 stressors are:
1. Role Ambiguity
2. Role Conflict
3. Role Overload
4. Interpersonal Conflict
5. Perceived Lack of Control

It uses Claude on the backend to make API calls to determine the likelyhood of the stressors appearing, and Streamlit on the frontend for an easy-to-use, polished UI for users to interact with.

# Usage

1. Click on the "Set API Key" tab at the top.
2. Input your Claude API key and hit enter to save it.
3. Go to the "File Upload & Process" tab
4. Upload your conversation as a .txt file.

    4.5. Each line of the conversation file should be of the format \[Speaker's Name\]\: \[Their Words\]. If a line is empty or starts with a '#', it is ignored.
5. Click the "Analyze" button that appears after uploading a file.
6. Wait for a response and view the stressors!

# Running this repo locally

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

    `streamlit run frontend.py`

6. Navigate to the localhost found in the console output.



# Dependencies

 - anthropic
 - python-dotenv
 - requests
 - streamlit



# Assumptions made
1. Names only contain alphabetic characters, spaces, and/or hyphens.
2. Script1 contains titles for the individuals before starting the conversation. I added '#' characters to denote them as comments so that my processScript file ignores them.
3. There is a set and hashmap that contain the names of the people in the conversation. Since Vincer offers digital products, I am assuming that each person, even if they have the same name, has their own microphone (with an ID) that could be used for some hash function so that they are always different in this set. Alternatively, name them "Chris 1" and "Chris 2."