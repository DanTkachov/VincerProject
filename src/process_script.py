import os
from collections import defaultdict

class ProcessScript:
    '''
    This class processes a .txt file that serves as a script.
    It expect each line to have a name, followed by a colon, followed by what was said.

    Names are assumed to only contain alphabetic characters, spaces, and hyphens.
    '''
    def __init__(self, file):
        self.file = file
        self.current_speaker = None
        self.current_line = ""
        self.speakers = set()
        self.speaker_to_speech = defaultdict(list) # name of speaker -> what they have said.
        self.organize()

    def organize(self):
        '''
        Processes a file and organizes it into a hashmap
        Hashmap has the following structure: {name -> list}. List contains the speakers speech.
        '''
        for line in self.file:
            line = line.strip()

            # Script1 contains titles, so we comment those out.
            if not line or line[0] == '#':
                continue

            # Try to get name and what they said. 
            # If no name, consider it a continuation of the last speaker.
            try:
                name, text = line.split(":", 1)
                
                # We may encounter a situation where a time is given in a new line.
                # In this case, make sure it has no numbers.
                if any(not char.isalpha() and char != '-' and char != " " for char in name):
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

        self.speakers = set(name for name in self.speaker_to_speech.keys())

    def display(self):
        '''
        Displays the hashmap of speakers and their words in a more human-readable format.
        Returns the same display, which is optional.
        '''
        res = ""
        for speaker, speech in self.speaker_to_speech.items():
            width = 20
            print("#" * width)
            res += "#" * width + '\n'
            print(f"{speaker}".center(width))
            res += f"{speaker}".center(width) + '\n'
            print("#" * width)
            res += "#" * width + '\n'

            for line in speech:
                print(line)
                res += line + '\n'
            print("END OF LINES".center(width, '-'))
            res += "END OF LINES".center(width, '-') + '\n'
        return res
    
    def raw_display(self, speaker):
        '''Shows raw list of words from a speaker. Used for debugging.'''
        if speaker in self.speaker_to_speech.keys():
            return self.speaker_to_speech[speaker]
        else:
            return None
    
    def return_speakers(self):
        '''Debug function for listing speakers in the hashmap.'''
        return self.speakers