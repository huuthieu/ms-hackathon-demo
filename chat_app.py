import streamlit as st
import datetime

def get_current_time():
    return datetime.datetime.now().strftime("%H:%M")

def main():
    st.set_page_config(page_title="Streamlit Chat App", page_icon=":speech_balloon:")

    st.title("Streamlit Chat App")

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(f"{message['name']} - {message['time']}")
            st.write(message["content"])

    # User input
    user_name = st.text_input("Your Name", value="User")
    user_input = st.chat_input("Type your message here...")

    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({
            "role": "user",
            "content": user_input,
            "name": user_name,
            "time": get_current_time()
        })

        # Display user message
        with st.chat_message("user"):
            st.write(f"{user_name} - {get_current_time()}")
            st.write(user_input)

        # Simulate a response (you can replace this with actual chat logic)
        response = f"Echo: {user_input}"
        
        # Add response to chat history
        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "name": "Assistant",
            "time": get_current_time()
        })

        # Display assistant response
        with st.chat_message("assistant"):
            st.write(f"Assistant - {get_current_time()}")
            st.write(response)

if __name__ == "__main__":
    main()
