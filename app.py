

# mood-song-suggester
Based on your correct mood a python bot suggests songs
import streamlit as st

# Mood to song mapping
mood_songs = {
    "Happy": "🎵 Watermelon Sugar - Harry Styles",
    "Sad": "🎵 Wicked Game - Chris Isaak",
    "Angry": "🎵 Another Love - Tom Odell",
    "Relaxed": "🎵 Fourth Of July - Sufijan Stevens",
    "Romantic": "🎵 Lovers Rock - TV Girl",
    "Energetic": "🎵 FASHION - Britney Manson",
    "Motivated": "🎵 I Ain't Worried - OneRepublic"
}

# Streamlit UI
st.title("🎧 Mood Song Suggester")
st.write("Tell me how you're feeling, and I'll suggest a song for you!")

mood = st.selectbox("How are you feeling?", list(mood_songs.keys()))

if st.button("Suggest a Song"):
    st.success(f"Here's a song for your mood: {mood_songs[mood]}")
