import os
from dotenv import load_dotenv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time
# CHANGE 1: Import Voice and VoiceSettings directly
from elevenlabs import Voice, VoiceSettings
from elevenlabs.client import ElevenLabs


# Load the API key from the .env file
load_dotenv()

# Initialize the tools we need
client = ElevenLabs()
analyzer = SentimentIntensityAnalyzer()

def analyze_and_synthesize(text: str):
    """
    Analyzes text using VADER and generates audio using ElevenLabs.
    """
    # 1. Analyze sentiment with VADER
    sentiment_scores = analyzer.polarity_scores(text)
    compound_score = sentiment_scores['compound']

    if compound_score >= 0.05:
        emotion = "Positive"
    elif compound_score <= -0.05:
        emotion = "Negative"
    else:
        emotion = "Neutral"
        
    print(f"Text: '{text}'")
    print(f"VADER Score: {compound_score:.2f}, Detected Emotion: {emotion}")

    # 2. Map sentiment to ElevenLabs voice stability setting
    if emotion == "Positive":
        stability_setting = 0.5 - (compound_score * 0.25)
    elif emotion == "Negative":
        stability_setting = 0.6
    else: # Neutral
        stability_setting = 0.75

    stability_setting = max(0.0, min(1.0, stability_setting))
    print(f"Applied Voice Stability: {stability_setting:.2f}")

    # 3. Generate audio using the corrected ElevenLabs API method
    audio_data_iterator = client.text_to_speech.convert(
        # CHANGE 2: Use the imported Voice and VoiceSettings classes
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        text=text,
        model_id="eleven_multilingual_v2",
        voice_settings=VoiceSettings(
            stability=stability_setting,
            similarity_boost=0.75
        )
    )

    # The new method returns chunks of audio, so we join them together
    full_audio = b"".join(audio_data_iterator)
    
    # 4. Save the audio to a file
    timestamp = int(time.time())
    relative_path = f'audio/output_{timestamp}.mp3'
    full_path = f'static/{relative_path}'
    
    with open(full_path, 'wb') as f:
        f.write(full_audio)

    # 5. Return results for the web page
    return relative_path, emotion, compound_score