# mood-song-suggester
Based on your correct mood a python bot suggests songs
import streamlit as st

# Mood to song mapping
mood_songs = {
    "Happy": "🎵 Happy – Pharrell Williams",
    "Sad": "🎵 Let Her Go – Passenger",
    "Angry": "🎵 In The End – Linkin Park",
    "Relaxed": "🎵 Weightless – Marconi Union",
    "Romantic": "🎵 Perfect – Ed Sheeran",
    "Energetic": "🎵 Can't Stop The Feeling! – Justin Timberlake",
    "Motivated": "🎵 Believer – Imagine Dragons"
}

# Streamlit UI
st.title("🎧 Mood Song Suggester")
st.write("Tell me how you're feeling, and I'll suggest a song for you!")

mood = st.selectbox("How are you feeling?", list(mood_songs.keys()))

if st.button("Suggest a Song"):
    st.success(f"Here's a song for your mood: {mood_songs[mood]}")
