import moviepy.editor
import streamlit as st 



def audiofile(vid):
    video = moviepy.editor.VideoFileClip(vid)
    duration = video.duration
    st.write(f'Video Duration is: {duration}')
    audio = video.audio
    audio.write_audiofile('OutputAudio.mp3')



# Create a file uploader widget
st.title('Extract Audio From Video Here')
uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])
if uploaded_file is not None:
    file_name = uploaded_file.name
    with open('InputVideo.mp4','wb')as f:
        f.write(uploaded_file.read())

    vid = 'InputVideo.mp4'
    audiofile(vid)
    st.title('Output Audio')
    audio_file = open('OutputAudio.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes)

