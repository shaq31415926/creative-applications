import streamlit as st
from transformers import AutoProcessor, MusicgenForConditionalGeneration
import datetime
import scipy

# create a title on a streamlit app
st.title("Text to Music Generator 🎵")

# create a box
prompt = st.text_area("What are you in the mood to listen to?")
print(prompt)
# create a slider
duration = st.slider("Select time duration (in seconds)", 0, 20, 10)

# if the user enters a prompt or adjusts the slider
if prompt and duration:
    # load the pretrained model
    model_name = "facebook/musicgen-small"
    processor = AutoProcessor.from_pretrained(model_name)
    model = MusicgenForConditionalGeneration.from_pretrained(model_name)

    # add the prompt text that we want to convert to music
    inputs = processor(text=prompt,
                       padding=True,
                       return_tensors="pt")
    # this will create the prompt into music
    # you can adjust the max_new_tokens to change the length of the song
    duration_final = round(duration * (256/5))
    audio_values = model.generate(**inputs, max_new_tokens=duration_final)

    # write the audio file to a location of your choice
    # add a timestamp parameter
    current_timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    scipy.io.wavfile.write(f"music/music_{current_timestamp}.wav",
                           rate=model.config.audio_encoder.sampling_rate,
                           data=audio_values[0, 0].numpy())

    # this displays the music on the app
    def display_music(audio_filepath):
        audio_file = open(audio_filepath, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes)

    display_music(f"music/music_{current_timestamp}.wav")