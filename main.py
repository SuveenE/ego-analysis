import streamlit as st
from video_summarizer import analyse_video

st.title("Ego Analysis App")

uploaded_file = st.file_uploader("Choose a MP4 file", type="mp4")

if uploaded_file is not None:
    #TODO: Add code to process the file and display the items from the response
    video_summary = analyse_video(uploaded_file)
    pass
    
else:
    st.write("Waiting on file upload...")