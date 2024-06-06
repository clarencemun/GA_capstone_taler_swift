import streamlit as st
import os
import requests
from openai import OpenAI
import ollama  # Import the ollama module
import random
from gtts import gTTS
from PIL import Image

# Set base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the banner image using a relative path
image_path = os.path.join(BASE_DIR, "banner.png")
image = Image.open(image_path)

# Display the banner image
st.image(image, use_column_width=True)

# Combined HTML to inject custom CSS for the background, text backgrounds, font color, font sizes, and element styling
st.markdown(
    """
    <style>
    /* Change background image */
    [data-testid="stAppViewContainer"] {
        background-image: url("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/47d533ba-5efc-4a69-9746-e1ca266f86cc/dgntfvr-f5796db2-7e9a-4285-b4cb-4a2816bda42f.jpg/v1/fill/w_894,h_894,q_70,strp/fairytale_forest_background_stock_by_children7_dgntfvr-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTAyNCIsInBhdGgiOiJcL2ZcLzQ3ZDUzM2JhLTVlZmMtNGE2OS05NzQ2LWUxY2EyNjZmODZjY1wvZGdudGZ2ci1mNTc5NmRiMi03ZTlhLTQyODUtYjRjYi00YTI4MTZiZGE0MmYuanBnIiwid2lkdGgiOiI8PTEwMjQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.eDDTWZNXp__HhI4gcBbRyAK2nJJSZCYL5RTB0YO4j4k&width=1000");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: local;
    }

    /* Adding semi-transparent backgrounds to text widgets for better readability */
    .stTextInput, .stTextArea, .stSelectbox, .stButton, .stSlider, .big-font, .stMarkdown, .stTabs, .stRadio {
        background-color: rgba(255, 255, 255, 0.75); /* Semi-transparent white */
        border-radius: 5px; /* Rounded borders */
        padding: 5px; /* Padding around text */
        margin-bottom: 5px; /* Space between widgets */
        color: #333333; /* Dark grey font color */
        font-size: 25px; /* Increased font size for inputs and buttons */
    }

    /* Specific font size increases for the sidebar elements */
    [data-testid="stSidebar"] .stTextInput, [data-testid="stSidebar"] .stSelectbox, [data-testid="stSidebar"] .stButton, [data-testid="stSidebar"] .stSlider {
        font-size: 18px; /* Larger font size for sidebar elements */
    }

    /* You can customize font color specifically for titles and headers */
    .stTitle, .stHeader, .big-font {
        color: #2E4053; /* Example: darker shade of blue-grey */
        font-size: 30px; /* Larger font size for titles */
    }

    /* Style for big-font class used for larger text */
    .big-font {
        font-size: 30px !important; /* Ensuring it overrides other styles */
        font-weight: bold;
    }

    /* Style for medium-font class used for medium text */
    .medium-font {
        font-size: 20px !important; /* Ensuring it overrides other styles */
        font-weight: bold;
    }

    /* Style for small-font class used for small text */
    .small-font {
        font-size: 12px !important; /* Ensuring it overrides other styles */
        font-weight: bold;
    }

    /* Ensuring the rest of the container is also covered */
    [data-testid="stSidebar"], [data-testid="stHeader"] {
        background-color: transparent;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add developer credit
st.markdown("""
    <div style="text-align: left;">
        <p class="small-font">Developed by Clarence Mun</p>
    </div>
""", unsafe_allow_html=True)

# Initialise OpenAI client
client = OpenAI()

# Define the list of available genres and languages
genres = [
    "Children's Educational Story", "Fairy Tale", "Adventure Story",
    "Science Fiction for Kids", "Fantasy Story", "Mystery and Detective Story", "Superhero Story"
]
languages = ['English', '中文', 'Melayu']

characters = "random main character"

# Initialise message history and image counter
message_history = []
image_counter = 1

# Generate a filename for saving an image
def generate_filename():
    global image_counter
    filename = os.path.join(BASE_DIR, "images", f"generated_image_{image_counter}.jpg")
    image_counter += 1
    return filename

# Get language prefix for story generation
def get_language_prefix(language):
    if language == '中文':
        return "请用纯中文写一个故事"
    elif language == 'Melayu':
        return "Sila tulis cerita dalam bahasa Melayu penuh, tiada perkataan Inggeris"
    else:
        return "Create a story"

# Generate speech from text using gTTS
def generate_speech(text, filename='story.mp3', language='en', directory="audio"):
    directory = os.path.join(BASE_DIR, directory)
    if selected_language == '中文':
        language = 'zh'
    elif selected_language == 'Melayu':
        language = 'id'
    else:
        language = 'en'

    # Create the text-to-speech object
    myobj = gTTS(text=text, lang=language, slow=False)

    # Check if the directory exists, and create it if it doesn't
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Full path for the mp3 file
    file_path = os.path.join(directory, filename)

    # Save the converted audio
    myobj.save(file_path)

    # Play the converted file using 'open' on macOS
    st.audio(file_path, format='audio/mp3', start_time=0)

# Chat with the language model
def chat_with_model(input_text, language):
    global message_history
    language_prefix = get_language_prefix(language)
    full_input_text = f"{language_prefix} about {input_text}"
    message_history.append({'role': 'user', 'content': full_input_text})
    stream = ollama.chat(
        model='llama3:8b',
        messages=message_history.copy(),
        stream=True
    )
    story_text = ""
    for chunk in stream:
        story_text += chunk['message']['content']
    return story_text

# Generate images from the story
def generate_images_from_story(story_text):
    paragraphs = story_text.split('\n\n')
    images = []
    for paragraph in paragraphs:
        if paragraph.strip():
            prompt = f"Illustrate a charming scene in the style of Enid Blyton, featuring a whimsical setting with colourful characters. Include playful animals and children interacting in a magical, yet inviting environment. The scene should evoke a sense of adventure and joy, capturing the imagination of young readers. The colours should be bright and inviting, with soft and rounded shapes to create a gentle, comforting atmosphere. The overall style should be reminiscent of classic children's books, with a touch of fantasy and magic. Full story context: {story_text.strip()} Current focus: {paragraph.strip()}"
            image_path = generate_image(prompt)
            images.append((paragraph.strip(), image_path))
    return images

# Generate an image from a description using DALL-E
def generate_image(description):
    global image_counter
    response = client.images.generate(
        model="dall-e-3",
        prompt=description,
        size="1024x1024",
        quality="standard",
        n=1
    )
    image_url = response.data[0].url
    image_path = generate_filename()
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        with open(image_path, "wb") as image_file:
            image_file.write(image_response.content)
    return image_path

# Generate a story with the specified parameters
def generate_story(story_type, main_character, setting, conflict, resolution, moral, age, length_minutes, include_illustrations, include_audio, selected_language):
    prompt = (
        f"{story_type} about {main_character}, set in {setting}."
        f"The main conflict is {conflict}, and it resolves {resolution}."
        f"The moral of the story is '{moral}'."
        f"This story is intended for children aged {age}. Please use clear and simple language with basic words suitable for a {age}-year-old."
        f"Use short sentences and include familiar, everyday concepts."
        f"Craft the story to be about {200 * length_minutes} words long."
        f"Display only the story."
    )
    
    # Using the spinner to show processing state for story generation
    with st.spinner(f"Generating your story..."):
        story_text = chat_with_model(prompt, selected_language)
    
    if story_text:
        st.success("Story generated successfully!")
        
        # Check if illustrations are included
        if include_illustrations == "Yes":
            with st.spinner("Generating illustrations..."):
                paragraph_image_pairs = generate_images_from_story(story_text)
            for paragraph, image_path in paragraph_image_pairs:
                if image_path:  # Ensure the image was generated successfully
                    st.image(image_path, caption=paragraph)
            st.success("Illustrations generated successfully!")

            # Generating speech without displaying the text
            if include_audio == "Yes":
                with st.spinner("Generating audio..."):
                    generate_speech(story_text)
                st.success("Audio generated successfully!")

        else:
            # Display the story text when no illustrations are included
            st.write(story_text)
            # Generating speech for the plain text
            if include_audio == "Yes":
                with st.spinner("Generating audio..."):
                    generate_speech(story_text)
                st.success("Audio generated successfully!")
        
    else:
        st.error("The story generation did not return any text. Please try again.")

# Sidebar for input configuration (shared across tabs)
with st.sidebar:
    st.title("Configuration")
    selected_language = st.selectbox("Select Language:", languages)
    include_illustrations = st.radio("Include Illustrations?", ["No", "Yes"])
    include_audio = st.radio("Include Audio?", ["No", "Yes"])
    age = st.slider("Age of audience (years old):", 1, 12, 5)
    length_minutes = st.slider("Length of story (minutes):", 1, 10, 5)

# Genre Configuration
genre_choice = st.sidebar.radio("Genre:", ["Random", "Manual"])
if genre_choice == "Manual":
    story_type = st.sidebar.selectbox("Select Genre", genres)
else:
    story_type = random.choice(genres)
    st.sidebar.write(f"Random Genre: {story_type}")

# Main Character Configuration
character_choice = st.sidebar.radio("Main Character:", ["Random", "Manual"])
if character_choice == "Manual":
    main_character = st.sidebar.text_input("Enter Main Character's Name", "")
else:
    main_character = characters
    st.sidebar.write(f"Random Main Character")

# Main tabs
tab1, tab2 = st.tabs(["TaleR Swift", "TaleR-Made"])

# Tab 1: Generate Random Story
with tab1:
    if st.button("Generate Random Story"):
        random_setting = 'random setting'
        random_conflict = 'random conflict'
        random_resolution = 'random resolution'
        random_moral = 'a random moral lesson'
        generate_story(story_type, main_character, random_setting, random_conflict, random_resolution, random_moral, age, length_minutes, include_illustrations, include_audio, selected_language)

# Tab 2: Generate Story
with tab2:
    setting = st.text_input("Where the story takes place:")
    conflict = st.text_input("Main plot challenge:", help="Describe the central conflict or challenge that drives the story.")
    resolution = st.text_input("Story Climax and Conclusion:", help="Explain how the plot reaches its peak and resolves.")
    moral = st.text_input("Moral of the story:")
    if st.button("Generate Custom Story"):
        generate_story(story_type, main_character, setting, conflict, resolution, moral, age, length_minutes, include_illustrations, include_audio, selected_language)
