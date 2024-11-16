import streamlit as st
import random

# Function to generate a story based on user-provided words
def generate_story(words):
    intro = "Once upon a time, in a land full of"
    story = intro + " " + ", ".join(words[:-1]) + f", and {words[-1]}. "
    
    # Your generated story content
    story += "There was an adventure waiting to unfold. "
    story += "Brave heroes embarked on a quest to find the magical " + random.choice(words) + ". "
    story += "Their journey took them through " + random.choice(words) + " forests and across " + random.choice(words) + " mountains. "
    story += "Finally, they reached the majestic " + random.choice(words) + " where the legendary " + random.choice(words) + " dwelled. "
    story += "And so, with courage and determination, they began their remarkable tale."

    return story

# Streamlit app
st.title('Story Generator')

user_input = st.text_input("Enter words or phrases (separated by commas):")
user_words = [word.strip() for word in user_input.split(",")]

if st.button('Generate Story'):
    if len(user_words) > 1:
        generated_story = generate_story(user_words)
        st.write("### Generated Story:")
        st.write(generated_story)
    else:
        st.write("Please enter more word or phrases to generate a story.")
