## Michael Kahen

## mkahen

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
            # Given
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

            # Written
            #1
            r"(.*)(ing)? excites me": [
                "What about %1 excites you?",
                "How does the excitement manifest in your life?",
                "Have you shared your excitement about %1 with other people?"
            ],

            #2
            r"I feel (.*)": [
                "Why do you feel %1?",
                "How long have you been feeling %1?",
                "What do you think caused you to feel %1?"
            ],

            #3
            r"Tell me about (.*)": [
                "What would you like to know about %1?",
                "Do you have feelings about %1?",
                "Is %1 a significant part of your life?"
            ],
            
            #4
            r"How do you feel about (.*)\??": [
                "I'm here to discuss your feelings, not mine.",
                "Let's focus on your feelings about %1.",
                "Why do you want to know my feelings about %1?"
            ],

            #5
            r"I want to (.*)": [
                "Why do you want to %1?",
                "What would it mean to you if you %1?",
                "Have you thought about the consequences of %1?"
            ],

            #6
            r"(.*)(ing)? frustrates me": [
                "Why does %1 frustrate you?",
                "How do you usually cope with frustration?",
                "Have you discussed this frustration with anyone?"
            ],

            #7
            r"I love (.*)": [
                "What is it about %1 that you love?",
                "How does %1 make you feel?",
                "Have you spoken to anyone about your feelings for %1?"
            ],

            #8
            r"(.*)(ing)? makes me happy": [
                "Why does %1 make you happy?",
                "How does your happiness manifest when %1?",
                "Do you usually experience joy in %1?"
            ],

            #9
            r"I can't stop thinking about (.*)": [
                "Why do you think %1 occupies your thoughts?",
                "What emotion do you feel when you think about %1?",
                "Have you tried to distract yourself from %1?"
            ],

            #10
            r"I don't know (.*)": [
                "It's okay not to know %1. What do you think about this uncertainty?",
                "Are you comfortable with not knowing about %1?",
                "What steps could you take to understand %1 better?"
            ],
        }

        # This is the default response if no pattern matches
        default_response = "Tell me more."

        # This checks each pattern and selects a response
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
