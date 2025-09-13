import gradio as gr
import os
from dotenv import load_dotenv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time
from elevenlabs import Voice, VoiceSettings
from elevenlabs.client import ElevenLabs

# Load the API key from the .env file
load_dotenv()
# --- THIS IS THE NEW DEBUG CODE ---
import os
print("Attempting to load API Key...")
print("API Key Loaded:", os.getenv("ELEVENLABS_API_KEY"))
# --- END OF DEBUG CODE ---

# --- Configuration ---
# Initialize the tools we need
client = ElevenLabs()
analyzer = SentimentIntensityAnalyzer()

# Dictionary of high-quality voices to choose from
VOICE_OPTIONS = {
    "Adam (Deep, Male)": "pNInz6obpgDQGcFmaJgB",
    "Antoni (Young, Male)": "ErXwobaYiN019PkySvjV",
    "Freya (Young, Female)": "jsCqWAovK2LkecY7zXl4",
    "Gigi (Playful, Female)": "jBpfuIE2acCO8z3wKNLl",
    "Serena (Pleasant, Female)": "pMsXgVXv3BLzUgSXRplE",
    "Arnold (Strong, Male)": "VR6AewLTigWG4xSOhOim",
    "Josh (Deep, Male)": "TxGEqnHWrfWFTfGW9XjX",
}

# --- Core Logic Function ---
def generate_empathetic_speech(text, voice_name):
    """
    This is the main function that Gradio will call.
    It takes text and a voice name, and returns the analysis and audio file path.
    """
    if not text.strip():
        return "Please enter some text to synthesize.", None

    # 1. Analyze sentiment with VADER
    sentiment_scores = analyzer.polarity_scores(text)
    compound_score = sentiment_scores['compound']

    if compound_score >= 0.05:
        emotion = "Positive"
    elif compound_score <= -0.05:
        emotion = "Negative"
    else:
        emotion = "Neutral"

    # 2. Map sentiment to voice stability
    if emotion == "Positive":
        stability_setting = 0.5 - (compound_score * 0.25)
    elif emotion == "Negative":
        stability_setting = 0.6
    else:  # Neutral
        stability_setting = 0.75
    
    stability_setting = max(0.0, min(1.0, stability_setting))

    # 3. Get the selected voice ID
    voice_id = VOICE_OPTIONS.get(voice_name)
    if not voice_id:
        return f"Error: Voice '{voice_name}' not found.", None

    # 4. Generate audio using ElevenLabs API
    try:
        audio_iterator = client.text_to_speech.convert(
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            text=text,
            model_id="eleven_multilingual_v2",
            voice_settings=VoiceSettings(
                stability=stability_setting,
                similarity_boost=0.75
            )
        )

        full_audio = b"".join(audio_iterator)
        
        # 5. Save the audio to a unique file
        if not os.path.exists('static/audio'):
            os.makedirs('static/audio')
        
        timestamp = int(time.time())
        file_path = f'static/audio/output_{timestamp}.mp3'
        
        with open(file_path, 'wb') as f:
            f.write(full_audio)
            
        # 6. Prepare the output text and return both
        analysis_text = (
            f"Detected Emotion: {emotion}\n"
            f"VADER Score: {compound_score:.2f}\n"
            f"Applied Voice Stability: {stability_setting:.2f}"
        )
        
        return analysis_text, file_path

    except Exception as e:
        return f"An error occurred: {str(e)}", None


# --- Gradio UI Definition ---
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# The Empathy Engine 🎙️")
    gr.Markdown("An AI voice generator that modulates its tone based on the text's emotion. Select a voice and type some text to begin.")
    
    with gr.Row():
        with gr.Column(scale=2):
            text_input = gr.Textbox(
                label="Text to Synthesize",
                placeholder="e.g., This is the best news I've heard all day!",
                lines=4
            )
            voice_dropdown = gr.Dropdown(
                label="Choose a Voice",
                choices=list(VOICE_OPTIONS.keys()),
                value="Serena (Pleasant, Female)"
            )
            submit_button = gr.Button("Generate Audio", variant="primary")
            
        with gr.Column(scale=1):
            analysis_output = gr.Textbox(label="Sentiment Analysis")
            audio_output = gr.Audio(label="Generated Voice")
    
    submit_button.click(
        fn=generate_empathetic_speech,
        inputs=[text_input, voice_dropdown],
        outputs=[analysis_output, audio_output]
    )

# --- Launch the App ---
if __name__ == "__main__":
    demo.launch()