import streamlit as st
import random

# Streamlit app title
st.markdown(
    """
    <span style="font-size: 36px; color: black;">Rock - </span>
    <span style="font-size: 36px; color: orange;">Paper - </span>
    <span style="font-size: 36px; color: darkgreen;">Scissors </span>
    <span style="font-size: 36px; color: blue;">Game</span>
    <h3 style="font-size: 18px; color: darkblue;">Welcome to the Best of 5 Rounds</h3>
    """,
    unsafe_allow_html=True
)

# Initialize session state for game data
if "rounds" not in st.session_state:
    st.session_state.rounds = 0
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.ties = 0
    st.session_state.last_result = ""
    st.session_state.player_choice = None
    st.session_state.computer_choice = None
    st.session_state.game_over = False

# Game choices
choices = ["rock", "paper", "scissors"]
max_rounds = 5

# Sidebar for score display
st.sidebar.header("Scoreboard")
st.sidebar.write(f"Player: {st.session_state.player_score}")
st.sidebar.write(f"Computer: {st.session_state.computer_score}")
st.sidebar.write(f"Ties: {st.session_state.ties}")
st.sidebar.write(f"Rounds Played: {st.session_state.rounds}/{max_rounds}")

# Show final result if game is over
if st.session_state.game_over:
    st.write("**Game Over!**")
    st.write(f"Final Score - Player: {st.session_state.player_score}, Computer: {st.session_state.computer_score}, Ties: {st.session_state.ties}")
    if st.session_state.player_score > st.session_state.computer_score:
        st.success("Congratulations! You are the overall winner!")
    elif st.session_state.computer_score > st.session_state.player_score:
        st.error("Computer is the overall winner!")
    else:
        st.warning("It's a tie overall!")
    st.write("Click 'Reset Game' to play again.")
else:
    # Player's choice via selectbox
    st.session_state.player_choice = st.selectbox(
        "Choose Rock, Paper, or Scissors:", ["", "Rock", "Paper", "Scissors"]
    )

    # Play button to submit choice
    if st.button("Play Round"):
        if st.session_state.player_choice == "":
            st.warning("Please select Rock, Paper, or Scissors before playing!")
        elif st.session_state.rounds >= max_rounds:
            st.session_state.game_over = True
            st.write("Game has already reached 5 rounds!")
        else:
            # Convert player choice to lowercase
            player = st.session_state.player_choice.lower()
            # Computer's random choice
            st.session_state.computer_choice = random.choice(choices)

            # Display choices
            st.write(f"**Round {st.session_state.rounds + 1}**")
            st.write(f"You chose: **{player}**")
            st.write(f"Computer chose: **{st.session_state.computer_choice}**")

            # Determine winner
            if player == st.session_state.computer_choice:
                st.session_state.ties += 1
                st.session_state.last_result = "It's a tie!"
            elif (
                (player == "rock" and st.session_state.computer_choice == "scissors")
                or (player == "paper" and st.session_state.computer_choice == "rock")
                or (player == "scissors" and st.session_state.computer_choice == "paper")
            ):
                st.session_state.player_score += 1
                st.session_state.last_result = "You win this round!"
            else:
                st.session_state.computer_score += 1
                st.session_state.last_result = "Computer wins this round!"

            # Increment round counter
            st.session_state.rounds += 1

            # Display result
            st.write(f"**Result**: {st.session_state.last_result}")

            # Check for early win
            if st.session_state.player_score >= 3 or st.session_state.computer_score >= 3 or st.session_state.rounds >= max_rounds:
                st.session_state.game_over = True

# Display last round's result (if any)
if st.session_state.last_result and not st.session_state.game_over:
    st.write(f"**Last Round**: {st.session_state.last_result}")

# Reset game button
if st.button("Reset Game"):
    st.session_state.rounds = 0
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.ties = 0
    st.session_state.last_result = ""
    st.session_state.player_choice = ""
    st.session_state.computer_choice = None
    st.session_state.game_over = False
    st.write("Game has been reset!")

# Stop playing button
if st.button("Stop Playing"):
    st.write("Nice playing with you! Bye!")