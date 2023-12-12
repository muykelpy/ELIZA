## NAME

## NetID

import re
import random
import string  

def eliza_chatbot():
    print("Hello! I'm ELIZA, your virtual therapist. How can I help you today? (Type 'quit' to exit.)")

    while True:
        user_input = input("> ")

        # Exit condition
        if user_input.lower() == 'quit':
            print("Goodbye! Take care.")
            break

        # Patterns and responses
        responses = {
            r"I need (.*)": [
                "Why do you need %1?",
                "Would obtaining %1 really help you?",
                "Are you sure you need %1?"   
            ],
            
            r"Why don't you (.*)\??": [
                "Do you really think I don't %1?",
                "Perhaps eventually I will %1.",
                "Do you want me to %1?"    
            ],
            
            r"Why can't I (.*)\??": [
                "Do you think you should be able to %1?",
                "If you could %1, what would you do?",
                "What would help you %1?"    
            ],
            
            r"I am (.*)": [
                "Did you come to me because you are %1?",
                "How long have you been %1?",
                "How do you feel about being %1?"
            ],    

            # Add more patterns here
            

            
        }

        # This is the default response if no pattern matches
        default_response = "Tell me more."

        # This checks each pattern and selecting a response
        for pattern, pattern_responses in responses.items():
            match = re.fullmatch(pattern, user_input, re.IGNORECASE)
            if match:
                # This removes punctuation from the captured group
                captured_group = match.group(1).translate(str.maketrans('', '', string.punctuation))
                response = random.choice(pattern_responses)
                # This replaces the placeholder with the cleaned captured group
                response = response.replace('%1', captured_group)
                break
        else:
            response = default_response

        print(response)

# Run the chatbot
eliza_chatbot()
