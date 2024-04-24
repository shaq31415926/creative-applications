from transformers import AutoProcessor, MusicgenForConditionalGeneration
import scipy
import datetime

# load the pretrained model
model_name = "facebook/musicgen-small"
processor = AutoProcessor.from_pretrained(model_name)
model = MusicgenForConditionalGeneration.from_pretrained(model_name)

# add the prompt text that we want to convert to music
prompt = ["the simpsons the simpsons"]
inputs = processor(text=prompt,
                   padding=True,
                   return_tensors="pt")
# this will create the prompt into music
# you can adjust the max_new_tokens to change the length of the song
audio_values = model.generate(**inputs, max_new_tokens=512)

# write the audio file to a location of your choice
# add a timestamp parameter
current_timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
scipy.io.wavfile.write(f"music/music_{current_timestamp}.wav",
                       rate=model.config.audio_encoder.sampling_rate,
                       data=audio_values[0, 0].numpy())
