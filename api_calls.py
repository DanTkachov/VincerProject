import anthropic
from dotenv import load_dotenv
import requests
import os
from process_script import ProcessScript
from prompts import make_prompt
    

class CallAPI:
    def __init__(self, system_prompt, user_prompt, dev_mode, api_key, file):
        self.system_prompt = system_prompt
        self.user_prompt = user_prompt
        self.dev_mode = dev_mode
        self.api_key = api_key
        self.file = file

    def message(self, file):
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
            res.append(message.content)
        return res

    def parse_response(self, res):
        text = res[0].text

        lines = text.split('\n')
        stressors = {}
        for line in lines:
            if line.startswith('Analysis'):
                break
            if ':' in line and '%' in line:
                parts = line.split(':')
                stressor = parts[0].strip()
                value = int(parts[1].strip().replace('%', ''))
                stressors[stressor] = value
        return stressors

