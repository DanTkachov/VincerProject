import anthropic
from dotenv import load_dotenv
import requests
import os
from process_script import ProcessScript
from prompts import make_prompt
    

class CallAPI:
    """Handles API calls to Anthropic's Claude for script analysis.
    
    This class processes script data and sends it to Claude for analysis,
    returning results for each speaker in the script.
    """
    def __init__(self, system_prompt: str, user_prompt: str, dev_mode: bool, api_key: str, file: str):
        self.system_prompt = system_prompt
        self.user_prompt = user_prompt
        self.dev_mode = dev_mode
        self.api_key = api_key
        self.file = file

    def message(self):
        '''Send an API call for each speaker for analysis.'''
        if self.dev_mode:
            load_dotenv()
            CLAUDE_API_KEY = os.getenv("ANTHROPIC_API_KEY")
        else:
            CLAUDE_API_KEY = self.api_key
        
        client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

        file = self.file

        script = ProcessScript(file)

        res = []
        for speaker in script.return_speakers():
            message = client.messages.create(
                model="claude-3-7-sonnet-20250219",
                max_tokens=100,
                temperature=1,
                system=self.system_prompt,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": make_prompt(script.raw_display(speaker=speaker))
                            }
                        ]
                    }
                ]
            )
            res.append([speaker, message.content])
        # print("RESULTS FORM MESSAGE:")
        # print(res)
        return res

    def parse_response(self, res: list):
        '''Parse the response that was returned from Claude'''
        stressors_dict = {} # list of (speaker -> stressors dict)
        for speaker, response in res:

            stressors = {}

            for item in response:
                if hasattr(item, 'text'):
                    text = item.text
                    lines = text.split('\n')
                    for line in lines:
                        if line.startswith('Analysis'):
                            break
                        if ':' in line and '%' in line:
                            parts = line.split(':')
                            stressor = parts[0].strip()
                            value = int(parts[1].strip().replace('%', ''))
                            stressors[stressor] = value
            stressors_dict[speaker] = stressors
        return stressors_dict

