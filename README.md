
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


## Running the Application

To start Version 1, open a terminal in the project folder and run:

```powershell
streamlit run version1/app.py
```

To start Version 2, run:

```powershell
streamlit run version2/app.py
```

Run one version at a time.

Streamlit will open the AI Escape Room in your web browser.
Enter natural-language commands to explore the library,
solve puzzles, collect items, and escape.


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

## Version 1 vs Version 2

| Feature | Version 1 | Version 2 |
|---|---|---|
| Streamlit interface | Yes | Yes |
| Gemini AI Game Master | Yes | Yes |
| Inventory management | Yes | Yes |
| Conversation history | Yes | Yes |
| Drawer puzzle | Yes | Yes |
| Painting password clue | Yes | Yes |
| Structured puzzle flags | No | Yes |
| Password discovery validation | No | Yes |
| Reset puzzle flags on restart | No | Yes |

### Version 1 Challenges

- Players could guess the password without examining the painting.
- Game state tracked inventory and escape status but did not
  explicitly track whether individual puzzles were completed.
- Maintaining correct Python indentation during development
  required debugging and testing.
- Gemini API responses could be unavailable due to usage limits,
  so fallback narration was necessary.

### Version 2 Improvements

- Added `drawer_solved` to track drawer puzzle completion.
- Added `password_discovered` to track painting clue discovery.
- Updated exit-door validation to require password discovery.
- Updated Restart Game to reset both puzzle flags.
- Tested attempts to bypass puzzle requirements.

### Testing Evidence

Six gameplay test cases, including adversarial tests,
are documented in [Test Cases](docs/test_cases.md).

### Architecture Diagrams

- [Version 1 Architecture](docs/version1_architecture.md)
- [Version 2 Architecture](docs/version2_architecture.md)

### Gameplay Screenshots

Screenshots of Version 1 gameplay, puzzle clues, inventory,
incorrect answers, and successful escape are available
in [Gameplay Screenshots](docs/screenshots/).
