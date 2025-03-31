import os
from collections import defaultdict

class ProcessScript:
    def __init__(self, file):
        self.file = file
        self.current_speaker = None
        self.current_line = ""
        self.speakers = set()
        self.speaker_to_speech = defaultdict(list) # name of speaker -> what they have said.
        self.organize()

    def organize(self):
        for line in self.file:
            line = line.strip()

            # Script1 contains titles, so we comment those out.
            if not line or line[0] == '#':
                continue

            # Try to get name and what they said. 
            # If no name, thats a continuation of the last speaker.
            try:
                name, text = line.split(":", 1)
                
                # We may encounter a situation where a time is given in a new line.
                # In this case, make sure it has no numbers.
                if any(char.isdigit() for char in name):
                    self.current_line = self.current_line + name + text
                    continue

                if self.current_speaker == name:
                    self.current_line += text
                else:
                    if self.current_speaker:
                        self.speaker_to_speech[self.current_speaker].append(self.current_line)
                    self.current_line = text
                    self.current_speaker = name

            except:
                self.current_line += line
            # print(line)
            # print("_______")
        self.speakers = set(name for name in self.speaker_to_speech.keys())

    def display(self):
        for speaker, speech in self.speaker_to_speech.items():
            width = 20
            print("#" * width)
            print(f"{speaker}".center(width))
            print("#" * width)

            for line in speech:
                print(line)
            print("END OF LINES".center(width, '-'))
    
    def raw_display(self, speaker):
        if speaker in self.speaker_to_speech.keys():
            return self.speaker_to_speech[speaker]
        else:
            return None
    
    def return_speakers(self):
        return self.speakers