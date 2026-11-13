
# AI Escape Room — The Mysterious Library

## Project Description

The Mysterious Library is a web-based escape room game built using Python and Streamlit.

Players explore a mysterious library, discover clues, solve puzzles, collect a Brass Key, and unlock the Exit Door.

## Version 1 Features

- Natural-language text input
- Five interactive objects
- Hidden clues and puzzles
- Inventory tracking
- Game progress tracking
- Restart Game button
- Gemini AI Game Master integration with fallback narration

## Interactive Objects

1. Bookshelf
2. Wooden Desk
3. Mysterious Painting
4. Locked Drawer
5. Exit Door

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- python-dotenv

## Installation

1. Install Python.
2. Open a terminal in the project folder.
3. Install the required packages:

   pip install -r requirements.txt

4. Create a `.env` file using `.env.example` as a guide.
5. Add your own Gemini API key to `.env`.

## Run Version 1

From the main project folder, run:

   python -m streamlit run version1/app.py

Open the local Streamlit URL displayed in the terminal.

## Testing

Five Version 1 test cases have passed:

1. Incorrect drawer combination
2. Correct drawer combination
3. Exit Door without the Brass Key
4. Incorrect Exit Door password
5. Successful escape

## AI Availability

The game includes Gemini API integration. If the API is unavailable or its quota is exhausted, the game uses predefined fallback narration.

Successful live Gemini narration has not yet been verified.

## Version 2

Version 2 will introduce structured game state, validated actions, and stronger protection against invalid or malicious inputs.
