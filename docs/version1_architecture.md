
# Version 1 Architecture — The Mysterious Library

```mermaid
flowchart TD
    A[Player] --> B[Streamlit Web Interface]
    B --> C[Python Game Logic]
    C --> D[Streamlit Session State]
    C --> E[Gemini API]
    E --> F[AI Game Master Narration]
    E --> G[Fallback Narration if API Fails]
    D --> B
    F --> B
    G --> B
```

## Component Description

- Player: Enters natural-language actions.
- Streamlit: Displays the game interface.
- Python Game Logic: Validates puzzle solutions and controls game rules.
- Session State: Stores inventory, action history, and escape progress.
- Gemini API: Attempts to generate atmospheric Game Master narration.
- Fallback Narration: Keeps the game playable if Gemini is unavailable.
