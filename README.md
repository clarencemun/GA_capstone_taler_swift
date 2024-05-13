# TaleR Swift - Storytelling Application

## Description

TaleR Swift is a storytelling application designed to generate engaging stories for children. The application offers a range of genres and languages, and it allows users to create personalised stories with illustrations and audio narration. 

This project uses Streamlit for the user interface, OpenAI's model for generating stories, and the Google Text-to-Speech (gTTS) engine for audio narration. The app is a creative and interactive platform for children’s storytelling.

## Features

- **Story Generation**: Create personalised stories for children across various genres.
- **Multi-language Support**: Generate stories in English, Chinese, or Malay.
- **Illustrations**: Generate visual illustrations for stories.
- **Audio Narration**: Create audio versions of the stories using gTTS.
- **Random Story Generator**: Generate random stories for quick entertainment.
- **Manual Story Generator**: Customise and generate stories based on user input.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/clarencemun/talerswift_streamlit.git
   ```

2. Navigate to the project directory:

   ```bash
   cd taler-swift
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit application:

   ```bash
   streamlit run talerswift_streamlit.py
   ```

## Usage

Once the application is running, users can interact with the application via the web interface. The main features are accessible through two tabs:

1. **TaleR Swift**: 
   - Generate random stories with random settings, conflicts, and resolutions.
   - Choose a genre and main character manually or let the app select randomly.

2. **TaleR-Made**:
   - Customise all aspects of the story, including the setting, conflict, and resolution.
   - Define a moral lesson and adjust the age and length of the story.

Both tabs share a common sidebar for language selection, illustration, and audio options.

## Customisation

The application's appearance can be customised through CSS injected via the Streamlit markdown functionality. The background image, text styling, and fonts are defined within the `talerswift_streamlit.py` file under the `<style>` tag.

## Dependencies

- **Streamlit**: A framework for creating interactive web applications.
- **OpenAI**: A library for interfacing with OpenAI's API.
- **Ollama**: A module for interacting with the Ollama language models.
- **gTTS**: A text-to-speech conversion tool.
- **Pillow**: A Python Imaging Library (PIL fork).
- **Requests**: A library for sending HTTP requests.

## Credits

Developed by Clarence Mun.