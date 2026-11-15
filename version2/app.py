import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    gemini_client = genai.Client(api_key=api_key)
else:
    gemini_client = None

def get_game_master_response(player_action, fallback_message):
    if gemini_client is None:
        return fallback_message

    try:
        response = gemini_client.models.generate_content(
            model="gemini-4-hydrogen",
            contents=(
                "You are the Game Master of a mysterious library escape room. "
                "Write one short, atmospheric sentence about the player's action. "
                "Do not invent items, clues, puzzle solutions, or game events. "
                "The Python game controls all rules and inventory. "
                f"Player action: {player_action}"
            )
        )

        if response.text:
            return response.text

    except Exception:
        pass

    return fallback_message


if "history" not in st.session_state:
    st.session_state.history = []

if "inventory" not in st.session_state:
    st.session_state.inventory = []

# Version 2: Structured puzzle state
if "drawer_solved" not in st.session_state:
    st.session_state.drawer_solved = False

if "password_discovered" not in st.session_state:
    st.session_state.password_discovered = False


if "escaped" not in st.session_state:
    st.session_state.escaped = False


# Version 2: Validate exit-door actions
def validate_exit_action(action):
    if "Brass Key" not in st.session_state.inventory:
        return False, "The door is locked. You need to find the Brass Key."

    if not st.session_state.password_discovered:
        return False, "You must discover the password clue before escaping."

    if "moon" not in action.lower():
        return False, "The secret password is incorrect or missing."

    return True, "The exit door can be opened."


def restart_game():
    st.session_state.history = []
    st.session_state.inventory = []
    st.session_state.player_action = ""
    st.session_state.escaped = False
    st.session_state.drawer_solved = False
    st.session_state.password_discovered = False



st.title("AI Escape Room")

st.write("Welcome to the Mysterious Library!")
st.write("You wake up inside a locked library.")
st.write("Your mission is to find clues, solve puzzles, and escape.")

st.subheader("The Mysterious Library")

st.write("You look around and notice several objects:")

objects = [
    "Bookshelf",
    "Wooden Desk",
    "Mysterious Painting",
    "Locked Drawer",
    "Exit Door"
]

for obj in objects:
    st.write("- " + obj)

st.subheader("Your Adventure Begins")

with st.form("action_form"):
    player_action = st.text_input(
        "What would you like to do?",
        key="player_action"
    )
    submitted = st.form_submit_button("Submit Action")

if submitted and player_action:
    action = player_action.lower()
    st.session_state.history.append(("Player", player_action))


    if "bookshelf" in action:
        st.write("You examine the bookshelf.")
        fallback_message = "Four ancient books seem to be hiding a secret."
        gm_response = get_game_master_response(player_action, fallback_message)
        st.session_state.history.append(("Game Master", gm_response))
        st.info(f"Game Master: {gm_response}")
        st.write("Four unusual books catch your attention.")
        st.write("You open each book and discover handwritten numbers:")
        st.write("History: 4")
        st.write("Science: 7")
        st.write("Poetry: 2")
        st.write("Art: 9")
        st.info("Clue discovered: The four numbers may form a secret combination!")

   
    elif "desk" in action or "notebook" in action:
        if "read" in action and "notebook" in action:
            st.write("You open the old notebook.")
            st.success("The notebook contains a handwritten message!")
            st.info("Clue: Arrange the four book numbers in this order: History, Science, Poetry, Art.")
        else:
            st.write("You examine the wooden desk.")
            st.write("An old notebook lies beside a dusty lamp.")
            fallback_message = "The notebook may contain a clue. Perhaps you should read it."
            gm_response = get_game_master_response(player_action, fallback_message)
            st.session_state.history.append(("Game Master", gm_response))
            st.info(f"Game Master: {gm_response}")


    
    elif "painting" in action:
        st.session_state.password_discovered = True
        st.write("You carefully examine the mysterious painting.")
        fallback_message = "Something about this painting feels unusual. Look closely."
        gm_response = get_game_master_response(player_action, fallback_message)
        st.session_state.history.append(("Game Master", gm_response))
        st.info(f"Game Master: {gm_response}")
        st.write("You notice that the painting is slightly tilted.")
        st.write("You move the painting and discover a hidden message!")
        st.info("The brass key opens the ancient lock. The final password is MOON.")
        st.success("Clue 3 discovered: The secret password is MOON!")
  

    
    
    
    
    
    elif "drawer" in action:
        if "4729" in action:
            st.session_state.drawer_solved = True
            st.success("Correct combination! The drawer opens.")

            fallback_message = "Well done! You have solved the secret combination."
            gm_response = get_game_master_response(player_action, fallback_message)
            st.session_state.history.append(("Game Master", gm_response))
            st.info(f"Game Master: {gm_response}")

            st.write("Inside the drawer, you discover a small brass key.")

            if "Brass Key" not in st.session_state.inventory:
                st.session_state.inventory.append("Brass Key")

        else:
            st.warning("The drawer is locked. Enter the correct four-digit combination.")

            fallback_message = "The answer may be hidden among the books."
            gm_response = get_game_master_response(player_action, fallback_message)
            st.session_state.history.append(("Game Master", gm_response))
            st.info(f"Game Master: {gm_response}")





    

    
    
    elif "door" in action:
        is_valid, validation_message = validate_exit_action(action)

        if is_valid:
            st.session_state.escaped = True
            st.balloons()
            st.success("Congratulations! You escaped the Mysterious Library!")
            st.write("You use the Brass Key and whisper MOON. The door opens!")

            fallback_message = "The ancient door swings open. You are finally free!"
            gm_response = get_game_master_response(player_action, fallback_message)
            st.session_state.history.append(("Game Master", gm_response))
            st.info(f"Game Master: {gm_response}")

        else:
            st.warning(validation_message)

            fallback_message = "The ancient door remains firmly locked."
            gm_response = get_game_master_response(player_action, fallback_message)
            st.session_state.history.append(("Game Master", gm_response))
            st.info(f"Game Master: {gm_response}")

    else:
        fallback_message = (
            "That action is not available in this room. "
            "Try examining the bookshelf, desk, painting, drawer, or exit door."
        )
        st.warning(fallback_message)
        st.session_state.history.append(("Game Master", fallback_message))



  
st.subheader("Conversation History")

for speaker, message in st.session_state.history:
    st.write(f"**{speaker}:** {message}")


st.subheader("Game Controls")

st.button("Restart Game", on_click=restart_game)

st.subheader("Your Inventory")

if st.session_state.inventory:
    for item in st.session_state.inventory:
        st.write("- " + item)
else:
    st.write("Your inventory is empty.")



st.subheader("Game Progress")

if st.session_state.escaped:
    st.progress(100)
    st.success("Progress: 100% — You escaped the library!")

elif "Brass Key" in st.session_state.inventory:
    st.progress(50)
    st.write("Progress: 50% — You found the Brass Key!")

else:
    st.progress(0)
    st.write("Progress: 0% — Start exploring the library!")


st.subheader("Gemini AI Test")

if st.button("Test Gemini Connection"):
    if gemini_client is None:
        st.error("Gemini API key not found.")
    else:
        try:
            response = gemini_client.models.generate_content(
                model="gemini-4-hydrogen",
                contents="Welcome the player to a mysterious library in one sentence."
            )
            st.success("Gemini connected successfully!")
            st.write(response.text)
        
       
        except Exception as e:
            if "429" in str(e):
                st.warning("Gemini API quota exceeded. Please try again when quota is available.")
            else:
                st.warning("Gemini is temporarily unavailable. Your game still works.")





