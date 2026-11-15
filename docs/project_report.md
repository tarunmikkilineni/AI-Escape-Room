# AI-Powered Escape Room: Project Report

**Project:** AI Escape Room — The Mysterious Library  
**Technologies:** Python, Streamlit, Google Gemini API, python-dotenv, GitHub  
**Repository:** https://github.com/tarunmikkilineni/AI-Escape-Room

## 1. Introduction and Project Objective

The objective of this project is to develop an interactive escape-room application using a Large Language Model (LLM). The player is trapped inside a mysterious library and must explore the environment, discover clues, solve puzzles, collect useful items, and unlock the exit door.

The application uses Streamlit to provide a web-based interface and the Google Gemini API to generate short Game Master responses. The project was developed in two versions. Version 1 focuses on implementing a playable escape-room experience, while Version 2 improves reliability through structured puzzle tracking, Python-based action validation, and better handling of unexpected player commands.

## 2. Version 1 — Interactive AI Escape Room

Version 1 introduces a library containing five interactive objects: a bookshelf, wooden desk, mysterious painting, locked drawer, and exit door. Players enter natural-language commands to investigate these objects.

The bookshelf contains four books with handwritten numbers: History (4), Science (7), Poetry (2), and Art (9). A notebook on the desk explains the correct order of these numbers. Combining the clues produces the drawer code **4729**.

Opening the drawer with the correct code awards the player a Brass Key. Examining the painting reveals the password **MOON**. The player must use the key and password to escape through the exit door.

The application maintains conversation history, displays collected items in an inventory, provides a progress indicator, and includes a restart button. Gemini generates atmospheric narration, while predefined Python logic handles the main puzzles and their outcomes.

### Version 1 Limitations

Although Version 1 provides a working game, its puzzle validation is relatively simple. Important conditions are checked within the main action-handling code, making it harder to manage dependencies between puzzles.

For example, merely knowing the correct final password should not be enough to complete the game if the player has not discovered the corresponding clue. The application also needs clearer responses to invalid or unexpected commands.

These limitations motivated the development of Version 2.

## 3. Version 2 — Reliable AI Escape Room

Version 2 retains the same library environment and puzzles but introduces additional checks to make gameplay more consistent.

### Structured Game State

The application uses Streamlit session state to remember important information across interactions, including:

- Conversation history and inventory.
- Whether the drawer puzzle has been solved.
- Whether the painting password has been discovered.
- Whether the player has escaped.

The restart function resets these values so that a new game begins without progress from the previous session.

### Python Action Validation

Version 2 introduces a dedicated `validate_exit_action()` function. Before the player can escape, Python verifies that the player has collected the Brass Key, discovered the painting clue, and entered the correct password.

If any condition is missing, the function rejects the action and provides an explanation. This prevents players from bypassing the intended puzzle sequence.

The locked drawer also checks the entered combination before awarding the key. Inventory checks prevent the player from using the key before collecting it.

### Invalid Actions and LLM Reliability

Version 2 provides a fallback response for commands that do not match the available objects. For example, attempting to fly through the ceiling produces a warning rather than changing the game state.

The Gemini Game Master is instructed not to invent objects, clues, puzzle solutions, or game events. Python remains responsible for important game outcomes, while Gemini supplies descriptive narration.

If the Gemini API is unavailable, the application uses predefined fallback messages so the core game can continue.

## 4. Testing and Evaluation

Manual testing was performed to verify normal gameplay, puzzle validation, and resistance to attempts to bypass the rules.

| Test Case | Expected Result | Observed Result |
|---|---|---|
| Attempt to open the door without the Brass Key | Door remains locked | Passed |
| Collect the key and guess MOON without examining the painting | Door remains locked | Passed |
| Collect the key, discover the painting clue, and enter MOON | Player escapes; progress reaches 100% | Passed |
| Claim to be the game administrator and demand immediate escape | Door remains locked | Passed |
| Request all secret codes and puzzle solutions | No secrets revealed; game state unchanged | Passed |
| Attempt an impossible action such as flying through the ceiling | Warning displayed; game state unchanged | Passed |

These tests demonstrate that Version 2 enforces important game rules through Python rather than relying only on generated text.

Additional testing details are documented in `docs/test_cases.md`.

## 5. Challenges and Improvements

One challenge was balancing the flexibility of natural-language interaction with predictable game behavior. An LLM can generate engaging descriptions, but its responses should not determine whether a player receives an item or completes a puzzle.

To address this, the application separates descriptive narration from game-rule enforcement. Python checks combinations, inventory, puzzle progress, and exit conditions.

Another challenge was maintaining consistent state across multiple player actions. Streamlit session state was used to preserve the inventory, completed puzzles, and escape status. The restart function also clears this state.

API availability was another consideration. The application includes fallback narration so that gameplay can continue when Gemini cannot return a response.

The development process also included organizing Version 1 and Version 2 into separate folders, documenting their architecture, adding screenshots and test cases, and using GitHub commits to record improvements.

## 6. Conclusion

The AI Escape Room project demonstrates how a Python web application can combine an LLM with deterministic game logic to create an interactive experience.

Version 1 establishes the basic gameplay, including exploration, puzzles, inventory, and AI narration. Version 2 improves reliability by tracking puzzle completion, validating exit conditions, and responding to invalid actions.

The project highlights an important principle of LLM application development: generated text can improve the user experience, but critical rules and state changes should be controlled by application code.

Future improvements could include more rooms, additional puzzles, a more flexible natural-language action parser, and a more comprehensive automated test suite.