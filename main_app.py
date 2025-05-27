import streamlit as st
from datetime import datetime
from actions import follow, unfollow
from login import login
from io import StringIO
from time import sleep

def get_user_file(action_type):
    if action_type.lower() == "follow":
        return "users_follow.txt"
    elif action_type.lower() == "unfollow":
        return "users_unfollow.txt"
    else:
        raise ValueError("Invalid action type")

def read_file(file_path):
    with open(file_path, "r") as file:
        return [username.strip() for username in file.readlines()]

st.set_page_config(page_title="Instagram Dashboard", layout="centered")
st.title("📱 Instagram Follow/Unfollow Bot")

participant_id = st.number_input("Participant ID", min_value=1, step=1)
action_type = st.selectbox("Action", ["Follow", "Unfollow"])
start_button = st.button("🚀 Start")

status_box = st.empty()
progress_bar = st.progress(0)
log_output = st.empty()

if start_button:
    try:
        condition = "subtract" if participant_id % 2 else "add"
        date_str = datetime.now().strftime("%Y-%m-%d")
        log_id = f"{participant_id}_{condition}_{date_str}_{action_type.lower()}"

        user_file = get_user_file(action_type)
        usernames = read_file(user_file)

        status_box.info("🔐 Launching browser and logging in...")
        login()
        sleep(30)
        status_box.success("✅ Logged in!")

        # Log storage for display
        log_buffer = StringIO()

        def callback(username, status, reason, index, total):
            msg = f"[{index+1}/{total}] {username} → {status.upper()} ({reason})\n"
            log_buffer.write(msg)
            log_output.text_area("📄 Run Log", log_buffer.getvalue(), height=300)
            progress_bar.progress((index + 1) / total)

        if action_type.lower() == "follow":
            follow(usernames, user_id=log_id, callback=callback)
        else:
            unfollow(usernames, user_id=log_id, callback=callback)

        status_box.success(f"✅ Done! Log saved as `{log_id}.csv`")

    except Exception as e:
        status_box.error(f"❌ Error: {e}")
