# TaleR Swift - Creating Children's Tales Swiftly

![App screenshot](screenshot.png)

## Description

TaleR Swift is a storytelling application designed to generate engaging stories for children. The application offers a range of genres and languages, and it allows users to create personalised stories with illustrations and audio narration. 

This project uses Streamlit for the user interface, OpenAI's model for generating stories, and the Google Text-to-Speech (gTTS) engine for audio narration. The app is a creative and interactive platform for children’s storytelling.

You will need an OpenAI API key and Ollama with Llama3:8b running in the background for this project.

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
   git clone https://github.com/clarencemun/GA_capstone_talerswift.git
   ```

2. Navigate to the project directory:

   ```bash
   cd GA_capstone_talerswift
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your API key

   MacOS
   Open Terminal: You can find it in the Applications folder or search for it using Spotlight (Command + Space).

   Edit Bash Profile: Use the command nano ~/.bash_profile or nano ~/.zshrc (for newer MacOS versions) to open the profile file in a text editor.

   Add Environment Variable: In the editor, add the line below, replacing your-api-key-here with your actual API key:

   export OPENAI_API_KEY='your-api-key-here'
   Save and Exit: Press Ctrl+O to write the changes, followed by Ctrl+X to close the editor.

   Load Your Profile: Use the command source ~/.bash_profile or source ~/.zshrc to load the updated profile.

   Verification: Verify the setup by typing echo $OPENAI_API_KEY in the terminal. It should display your API key.

   Windows
   Open Command Prompt: You can find it by searching "cmd" in the start menu.

   Set environment variable in the current session: To set the environment variable in the current session, use the command below, replacing your-api-key-here with your actual API key:

   setx OPENAI_API_KEY "your-api-key-here"
   This command will set the OPENAI_API_KEY environment variable for the current session.
   Permanent setup: To make the setup permanent, add the variable through the system properties as follows:

   Right-click on 'This PC' or 'My Computer' and select 'Properties'.
   Click on 'Advanced system settings'.
   Click the 'Environment Variables' button.
   In the 'System variables' section, click 'New...' and enter OPENAI_API_KEY as the variable name and your API key as the variable value.
   Verification: To verify the setup, reopen the command prompt and type the command below. It should display your API key: echo %OPENAI_API_KEY%

5. Run the Streamlit application:

   ```bash
   streamlit run talerswift.py
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

The application's appearance can be customised through CSS injected via the Streamlit markdown functionality. The background image, text styling, and fonts are defined within the `talerswift.py` file under the `<style>` tag.

## Dependencies

- **Streamlit**: A framework for creating interactive web applications.
- **OpenAI**: A library for interfacing with OpenAI's API.
- **Ollama**: A module for interacting with the Ollama language models.
- **gTTS**: A text-to-speech conversion tool.
- **Pillow**: A Python Imaging Library (PIL fork).
- **Requests**: A library for sending HTTP requests.

## Credits

Developed by Clarence Mun.