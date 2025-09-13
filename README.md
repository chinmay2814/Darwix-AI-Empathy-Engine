# The Empathy Engine 🎙️

A sophisticated text-to-speech application that analyzes emotional sentiment in text and generates human-like speech with appropriate emotional modulation using AI-powered voice synthesis.

## 🌟 Overview

The Empathy Engine combines sentiment analysis with advanced text-to-speech technology to create emotionally intelligent voice synthesis. By analyzing the emotional content of input text using VADER sentiment analysis, the system dynamically adjusts voice parameters to match the detected emotion, resulting in more natural and expressive speech output.

[![The-Empathy-Engine-visual-selection.png](https://i.postimg.cc/FRWzV4bW/The-Empathy-Engine-visual-selection.png)](https://postimg.cc/bDnqq4Bk)

## 🛠️ Technology Stack

### Backend
- **Flask**: Python web framework for server-side logic
- **VADER Sentiment**: Advanced sentiment analysis library
- **ElevenLabs API**: State-of-the-art text-to-speech synthesis
- **Python-dotenv**: Environment variable management

### Frontend
- **HTML5**: Semantic markup structure
- **CSS3**: Modern styling with animations and transitions
- **JavaScript**: Dynamic user interface interactions
- **Google Fonts**: Typography (Poppins font family)

## 📊 System Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Input    │───▶│  Flask Server    │───▶│  Sentiment      │
│   (Text)        │    │  (app.py)        │    │  Analysis       │
└─────────────────┘    └──────────────────┘    │  (VADER)        │
                                               └─────────────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Audio Output  │◀───│  Static Files    │◀───│  ElevenLabs     │
│   (MP3)         │    │  Storage         │    │  TTS API        │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                ▲
                                │
                       ┌─────────────────┐
                       │  Voice Settings │
                       │  Modulation     │
                       └─────────────────┘
```
## Application Flow
## 🔄 Application Flow

1. **Input Processing**: User enters text through the web interface
2. **Sentiment Analysis**: VADER analyzes emotional content and generates compound score
3. **Emotion Classification**: System categorizes emotion as Positive, Negative, or Neutral
4. **Voice Modulation**: Voice stability parameters are adjusted based on sentiment:
   - **Positive**: Lower stability (0.25-0.5) for more expressive delivery
   - **Negative**: Medium stability (0.6) for controlled emotional expression
   - **Neutral**: Higher stability (0.75) for clear, steady delivery
5. **Speech Synthesis**: ElevenLabs API generates audio with modulated voice settings
6. **File Management**: Audio saved as timestamped MP3 file in static directory
7. **Response Delivery**: Web interface displays results with audio player
## 📁 Project Structure

```
empathy-text-to-speech/
├── 📂 static/
│   └── 📂 audio/              # Generated audio files
├── 📂 templates/
│   └── 📄 index.html          # Main web interface
├── 📂 __pycache__/            # Python cache files
├── 📂 venv/                   # Virtual environment
├── 📄 .env                    # Environment variables (API keys)
├── 📄 .gitignore             # Git ignore rules
├── 📄 app.py                 # Flask application entry point
├── 📄 engine_logic.py        # Core sentiment analysis & TTS logic
├── 📄 requirements.txt       # Python dependencies
└── 📄 README.md             # This file
```

## 🔧 Core Components

### 1. Sentiment Analysis Engine (`engine_logic.py`)
- Implements VADER sentiment analysis
- Maps sentiment scores to voice parameters
- Manages ElevenLabs API integration
- Handles audio file generation and storage

### 2. Web Application (`app.py`)
- Flask server setup and routing
- Request handling and response generation
- Template rendering with dynamic content
- Static file serving for audio playback

### 3. User Interface (`templates/index.html`)
- Responsive design with modern styling
- Real-time feedback and loading states
- Audio player integration
- Form handling and validation

## ⚙️ Configuration

### Environment Variables
Create a `.env` file in the project root:

```env
ELEVENLABS_API_KEY=your_api_key_here
```

### Voice Settings Mapping
- **Positive Sentiment**: Dynamic stability (0.25-0.5 range)
- **Negative Sentiment**: Fixed stability (0.6)
- **Neutral Sentiment**: High stability (0.75)
- **Similarity Boost**: Consistent 0.75 for all emotions

## 🎯 Use Cases

- **Educational Tools**: Creating engaging narrated content
- **Accessibility**: Assistive reading with emotional context
- **Content Creation**: Generating voiceovers for videos/podcasts
- **Prototype Development**: Testing emotional AI applications
- **Research**: Studying sentiment-speech correlation

## 📋 Prerequisites

Before setting up the Empathy Engine, ensure you have:

- **Python 3.7+** installed on your system
- **ElevenLabs API account** and API key
- **Git** for version control (optional)
- **Modern web browser** for testing

## 🚀 Installation & Setup

### Step 1: Clone or Download the Project

```bash
# If using Git
git clone <your-repository-url>
cd empathy-text-to-speech

# Or download and extract the ZIP file
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install flask python-dotenv vaderSentiment elevenlabs
```

### Step 4: Set Up Environment Variables

1. Create a `.env` file in the project root directory:

```bash
touch .env  # On macOS/Linux
# On Windows, create the file manually
```

2. Add your ElevenLabs API key:

```env
ELEVENLABS_API_KEY=your_actual_api_key_here
```

**To get your ElevenLabs API key:**
- Sign up at [ElevenLabs](https://elevenlabs.io/)
- Navigate to your profile settings
- Copy your API key from the developer section

### Step 5: Create Required Directories

```bash
mkdir -p static/audio
```

### Step 6: Run the Application

```bash
python app.py
```

### Step 7: Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

## 🎮 Usage Instructions

1. **Enter Text**: Type or paste your text in the textarea
2. **Submit**: Click "Synthesize Voice" button
3. **Wait**: The system processes your text (loading indicator appears)
4. **Review**: Check the detected emotion and VADER score
5. **Listen**: Use the audio player to hear the generated speech
6. **Experiment**: Try different texts with varying emotional content

### Example Inputs

- **Positive**: "This is absolutely amazing! I couldn't be happier!"
- **Negative**: "I am incredibly frustrated with this situation."
- **Neutral**: "The weather forecast shows partly cloudy skies tomorrow."

## 🐛 Troubleshooting

### Common Issues

**1. API Key Errors**
```
Error: Invalid API key
Solution: Verify your .env file contains the correct ElevenLabs API key
```

**2. Audio Generation Fails**
```
Error: Failed to generate audio
Solution: Check internet connection and API quota limits
```

**3. Missing Dependencies**
```
Error: ModuleNotFoundError
Solution: Ensure all packages are installed: pip install -r requirements.txt
```

**4. Port Already in Use**
```
Error: Address already in use
Solution: Stop other applications using port 5000 or change port in app.py
```

### Performance Tips

- **Text Length**: Keep input under 500 characters for optimal processing speed
- **File Cleanup**: Periodically clean the `static/audio/` directory
- **API Limits**: Monitor your ElevenLabs usage to avoid quota exceeded errors

## 🔒 Security Considerations

- **API Key Protection**: Never commit `.env` files to version control
- **Input Validation**: The application validates text input length and content
- **File Management**: Audio files are timestamped to prevent conflicts
- **Error Handling**: Graceful error handling prevents application crashes

## 🚀 Future Enhancements

- **Multiple Voice Options**: Support for different voice personalities
- **Advanced Emotions**: Detection of complex emotions (sarcasm, excitement, etc.)
- **Batch Processing**: Multiple text inputs simultaneously
- **Audio Export**: Download functionality for generated audio
- **User Accounts**: Save and manage personal audio library
- **Real-time Streaming**: Live audio generation without file storage

## 📄 License

This project is open source. Please ensure you comply with ElevenLabs API terms of service when using their text-to-speech capabilities.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📞 Support

For technical issues or questions:
1. Check the troubleshooting section above
2. Review ElevenLabs API documentation
3. Open an issue in the project repository

---

**Built with ❤️ using Python, Flask, and ElevenLabs AI**
