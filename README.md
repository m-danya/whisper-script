### whisper-script

Transcribe multiple audio files using the OpenAI API.

An OpenAI API key is required. Proxy support is available.

### Usage

1. Create venv, install dependencies

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Create a .env file with the following content:

```
OPENAI_API_KEY=sk-proj-....
HTTPS_PROXY=socks5://127.0.0.1:2080 (optional)
```

3. Execute the script

```
python main.py <audio_files>
```
