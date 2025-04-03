# import anthropic
# from dotenv import load_dotenv
# import requests
# import os
# from process_script import ProcessScript
# from prompts import make_prompt
    

# if __name__ == '__main__':
#     # load_dotenv()

#     # CLAUDE_API_KEY = os.getenv("ANTHROPIC_API_KEY")
#     ANTHROPIC_API_KEY="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"
#     client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

#     file = open("conversations/script1.txt", "r")
#     script = ProcessScript(file)

#     for speaker in script.return_speakers():
#         message = client.messages.create(
#             model="claude-3-7-sonnet-20250219",
#             max_tokens=100,
#             temperature=1,
#             system="",
#             messages=[
#                 {
#                     "role": "user",
#                     "content": [
#                         {
#                             "type": "text",
#                             "text": make_prompt(script.raw_display(speaker=speaker))
#                         }
#                     ]
#                 }
#             ]
#         )
#         print(message.content)
